from pydantic import BaseModel
from itertools import combinations
import pandas as pd
from mysql_connection import MySqlConnection


mysql = MySqlConnection()

def predict_medicine(text_input):
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


text_input = {"matched_signs": [],
            "matched_illness": []}

print(predict_medicine(text_input))