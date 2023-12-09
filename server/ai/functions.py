from pydantic import BaseModel
from hazm import *
from itertools import combinations
import pandas as pd


class TextRequest(BaseModel):
    text: str


class IllnessRequest(BaseModel):
    illness: list


class SignsRequest(BaseModel):
    signs: list
    l: int = 10


def get_data_from_file(file_path):
    with open(file_path, "r") as file:
        data = [line.strip() for line in file]
    return data


def extract_ngrams(text_input, n):
    ngrams = []
    words = word_tokenize(text_input)
    if len(words) >= n:
        for i in range(len(words) - n + 1):
            ngram = tuple(words[i:i+n])
            ngrams.append(ngram)
    return ngrams


def filter_phrases(text_input, phrase_list, n):
    stemmer = Stemmer()
    matched_phrases = []
    ngrams = extract_ngrams(text_input, n)

    for ngram in ngrams:
        phrase = " ".join(ngram)
        stem_phrase = " ".join([stemmer.stem(gram) for gram in ngram])
        phrase_ws = "".join(ngram)
        stem_phrase_ws = "".join([stemmer.stem(gram) for gram in ngram])

        if stem_phrase in phrase_list:
            matched_phrases.append(stem_phrase)
        if phrase in phrase_list:
            matched_phrases.append(phrase)

        if stem_phrase_ws in phrase_list:
            matched_phrases.append(stem_phrase_ws)
        if phrase_ws in phrase_list:
            matched_phrases.append(phrase_ws)

        for gram in ngram:
            if gram in phrase_list:
                matched_phrases.append(gram)

            stem_gram = stemmer.stem(gram)
            if stem_gram in phrase_list:
                matched_phrases.append(stem_gram)

    matched_phrases = list(set(matched_phrases))
    return matched_phrases



def extract_keywords(text_input):
    signs = get_data_from_file("signs.txt")
    #illness = get_data_from_file("illness.txt")
    matched_signs = filter_phrases(text_input, signs, 2)
    #matched_illness = filter_phrases(text_input, illness, 2)

    #matched_phrases = {"matched_signs": matched_signs,
    #                   "matched_illness":matched_illness}
    return matched_signs


def predict_medicine(mysql, text):
    text_input = extract_keywords(text)
    final_result = pd.DataFrame()

    if len(text_input["matched_signs"]) == 1:
        if len(text_input["matched_illness"]) == 0:
            signs_sings = [("", text_input["matched_signs"][0])]
        else:
            signs_sings = []
    else:
        signs_sings = list(combinations(text_input["matched_signs"], 2))

    for sign_sing in signs_sings:
        medicines = mysql.get_medicine_by_sign_sign_agg(sign_sing[0], sign_sing[1])
        df_new = pd.json_normalize(medicines)
        final_result = pd.concat([final_result, df_new], ignore_index=True)

    for sign in text_input["matched_signs"]:
        for illnes in text_input["matched_illness"]:
            medicines = mysql.get_medicine_by_sign_illnes_agg(sign, illnes)
            df_new = pd.json_normalize(medicines)
            final_result = pd.concat([final_result, df_new], ignore_index=True)
            
    best_medicines = []
    if not final_result.empty:    
        grouped = final_result.groupby('medicine')['score'].sum().reset_index()
        final_result = grouped.sort_values(by='score', ascending=False)
        top = final_result.head(3)
        best_medicines = top.to_dict(orient='records')
    return best_medicines


