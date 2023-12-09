from fastapi import FastAPI
from functions import (predict_medicine, TextRequest, IllnessRequest,
                       SignsRequest, extract_keywords)
from mysql_connection import MySqlConnection


app = FastAPI()
mysql = MySqlConnection()


@app.get("/")
async def ping():
    return {"message": "True"}


@app.post("/get_signs_by_text")
async def get_signs_by_text(req: TextRequest):
    signs = extract_keywords(req.text)
    return signs


@app.post("/get_signs_by_signs_w2c")
async def get_signs_by_signs_w2c(sr: SignsRequest):
    result = mysql.get_illness_by_signs_w2c(sr.signs, sr.l)
    illness = [item['illness'] for item in result]
    signs = mysql.get_signs_by_illness_w2c(illness, sr.signs)
    return signs


@app.post("/get_medicine_by_illnes_w2c")
async def get_medicine_by_illnes_w2c(sr: SignsRequest):
    res = {}
    illnes = mysql.get_illness_by_signs_w2c(sr.signs, 1)[0]['illness']
    res['illness'] = illnes
    res['medicines'] = mysql.get_medicine_by_illnes_w2c(illnes)
    return res


# @app.get("/get_medicine_by_sign_sign_w2c")
# async def get_medicine_by_sign_sign_w2c(s1: str = "", s2: str = ""):
#     return mysql.get_medicine_by_sign_sign_w2c(s1, s2)

# @app.get("/get_sign_by_illness_sign_w2c")
# async def get_sign_by_illness_sign_w2c(s1: str = "", s2: str = ""):
#     return mysql.get_sign_by_illness_sign_w2c(s1, s2)

# @app.get("/get_medicine_by_sign_illnes_w2c")
# async def get_medicine_by_sign_illnes_w2c(s: str = "", i: str = ""):
#     return mysql.get_medicine_by_sign_illnes_w2c(s, i)


# @app.get("/get_medicine_by_sign_sign_glove")
# async def get_medicine_by_sign_sign_glove(s1: str = "", s2: str = ""):
#     return mysql.get_medicine_by_sign_sign_glove(s1, s2)

# @app.get("/get_medicine_by_sign_illnes_glove")
# async def get_medicine_by_sign_illnes_glove(s: str = "", i: str = ""):
#     return mysql.get_medicine_by_sign_illnes_glove(s, i)


@app.get("/get_medicine_by_sign_sign_agg")
async def get_medicine_by_sign_sign_agg(s1: str = "", s2: str = ""):
    return mysql.get_medicine_by_sign_sign_agg(s1, s2)

@app.get("/get_medicine_by_sign_illnes_agg")
async def get_medicine_by_sign_illnes_agg(s: str = "", i: str = ""):
    return mysql.get_medicine_by_sign_illnes_agg(s, i)

@app.post("/predict_medicine")
async def get_prediction_medicines(req: TextRequest):
    signs = extract_keywords(text_input)
    return predict_medicine(mysql, req.text)
