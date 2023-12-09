from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from model.User import UserProfile, UserInfo, UserUpdate
from model.Comment import Comment
from model.entity import Fruit
from model.Text import TextRequest, SignsRequest
from typing import Annotated
from utils.security import login_plugin, register_plugin, get_current_user
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from utils.dependency import oauth2_scheme, get_comment_with_username, check_admin_access
import requests, json
from utils.gateway import mongo_conn, el_conn, el_con_qa, r,  AI_DOCKER_SERVICE
from utils.cache import cache
#from ai.utils import predict_medicine


app = FastAPI()


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def ping():
    return {"message": "True"}


@app.post("/register")
async def register(user: UserInfo):
    user_dict = register_plugin(user)
    user_id = mongo_conn.create_user(user_dict)
    return {"message": f"User {user_id} registered successfully"}


@app.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_db = mongo_conn.get_user(form_data.username)
    access_token =login_plugin(user_db, form_data.username, form_data.password)
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/current_user")
async def get_secure_user(token: str = Depends(oauth2_scheme)):
    username = get_current_user(token)
    user_db = mongo_conn.get_user(username)
    if user_db is None:
        raise HTTPException(status_code=401, detail="User not found")
    return UserProfile(**user_db)


@app.put("/user/update")
async def update_user_info(user_update: UserUpdate, token: str = Depends(oauth2_scheme)):
    username = get_current_user(token)
    user = mongo_conn.update_user(username, user_update)
    if user:
        return UserProfile(**user)
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.get("/fruits")
async def get_all_fruits():
    return mongo_conn.get_all_fruits()


@app.get("/fruits/{fruit_id}")
async def get_fruit(fruit_id: int):
    return mongo_conn.get_fruit(fruit_id)


@app.post("/fruits/{fruit_id}/comments/add")
async def fruits_add_comment(fruit_id: int, comment: dict = Depends(get_comment_with_username)):
    mongo_conn.add_comment_fruit(fruit_id, comment)
    return {"message": f"Comment {fruit_id} created successfully"}


@app.get("/medicines")
async def get_all_medicines():
    return mongo_conn.get_all_medicines()


@app.get("/medicines/{medicine_id}")
async def get_medicine(medicine_id: int):
    return mongo_conn.get_medicine(medicine_id)


@app.post("/medicines/{medicine_id}/comments/add")
async def medicines_add_comment(medicine_id: int, comment: dict = Depends(get_comment_with_username)):
    mongo_conn.add_comment_medicine(medicine_id, comment)
    return {"message": f"Comment {medicine_id} created successfully"}


@app.get("/illness")
async def get_all_illness(page: int):
    return mongo_conn.get_illness_by_page(page)


@app.get("/illness/{illnes_id}")
async def get_illnes(illnes_id: int):
    return mongo_conn.get_illnes(illnes_id)


@app.post("/illness/{illnes_id}/comments/add")
async def illness_add_comment(illnes_id: int, comment: dict = Depends(get_comment_with_username)):
    mongo_conn.add_comment_illnes(illnes_id, comment)
    return {"message": f"Comment {illnes_id} created successfully"}


@app.get("/trad_posts")
async def get_posts_by_page(page: int):
    return mongo_conn.get_posts_by_page(page)


@app.get("/trad_posts/{post_id}")
async def get_trad_post(post_id: int):
    return mongo_conn.get_trad_post(post_id)


@app.post("/trad_posts/{post_id}/comments/add")
async def posts_add_comment(post_id: int, comment: dict = Depends(get_comment_with_username)):
    mongo_conn.add_comment_post(post_id, comment)
    return {"message": f"Comment {post_id} created successfully"}


@app.get("/get_items_by_tag")
async def get_items_by_tag(tag: str):
    return el_conn.get_tag_items(tag)


@app.get("/search")
async def search_items(keyword: str):
    result = cache(keyword)
    if result:
        return result
    result = el_conn.search_items(keyword)
    r.setex(keyword, 3600, json.dumps(result))
    return result


@app.get("/qa")
async def search_questions(keyword: str):
    result = el_con_qa.search_questions(keyword)
    return result


@app.post("/get_signs_by_text")
async def get_prediction_medicines(req: TextRequest):
    p = requests.post(f"{AI_DOCKER_SERVICE}/get_signs_by_text",
                      json.dumps({"text": req.text}))
    return json.loads(p.content.decode())


@app.post("/get_signs_by_signs_w2c")
async def get_signs_by_signs_w2c(sr: SignsRequest):
    p = requests.post(f"{AI_DOCKER_SERVICE}/get_signs_by_signs_w2c",
                      json.dumps({"signs": sr.signs, "l": sr.l}))
    signs = json.loads(p.content.decode())
    signs = [sign['sign'] for sign in signs[:4]]
    return signs


@app.post("/get_medicine_by_illnes_w2c")
async def get_medicine_by_illnes_w2c(sr: SignsRequest):
    p = requests.post(f"{AI_DOCKER_SERVICE}/get_medicine_by_illnes_w2c",
                      json.dumps({"signs": sr.signs}))
    return json.loads(p.content.decode())


@app.get("/admin/access")
async def user_access(is_access: bool = Depends(check_admin_access)):
    return {"access": 1}


@app.post("/admin/fruits/create")
async def create_fruit(fruit: Fruit, is_access: bool = Depends(check_admin_access)):
    fruit_id = mongo_conn.create_fruit(fruit.dict())
    return {"message": f"fruit {fruit_id} created successfully"}


@app.put("/admin/fruits/{fruit_id}/update")
async def update_fruit(fruit_id: int, fruit: Fruit, is_access: bool = Depends(check_admin_access)):
    fruit = mongo_conn.update_fruit(fruit_id, fruit)
    return fruit

@app.delete("/admin/fruits/{fruit_id}/delete")
async def update_fruit(fruit_id: int, is_access: bool = Depends(check_admin_access)):
    _ = mongo_conn.delete_fruit(fruit_id)
    return {"message": "fruit deleted"}

# @app.get("/get_medicine_by_sign_sign_w2c")
# async def get_medicine_by_sign_sign_w2c(s1: str = "", s2: str = ""):
#     return mysql.get_medicine_by_sign_sign_w2c(s1, s2)

# @app.get("/get_medicine_by_sign_illnes_w2c")
# async def get_medicine_by_sign_illnes_w2c(s: str = "", i: str = ""):
#     return mysql.get_medicine_by_sign_illnes_w2c(s, i)


# @app.get("/get_medicine_by_sign_sign_glove")
# async def get_medicine_by_sign_sign_glove(s1: str = "", s2: str = ""):
#     return mysql.get_medicine_by_sign_sign_glove(s1, s2)

# @app.get("/get_medicine_by_sign_illnes_glove")
# async def get_medicine_by_sign_illnes_glove(s: str = "", i: str = ""):
#     return mysql.get_medicine_by_sign_illnes_glove(s, i)


# @app.get("/get_medicine_by_sign_sign_agg")
# async def get_medicine_by_sign_sign_agg(s1: str = "", s2: str = ""):
#     return mysql.get_medicine_by_sign_sign_agg(s1, s2)

# @app.get("/get_medicine_by_sign_illnes_agg")
# async def get_medicine_by_sign_illnes_agg(s: str = "", i: str = ""):
#     return mysql.get_medicine_by_sign_illnes_agg(s, i)

# @app.get("/predict_medicine")
# async def get_prediction_medicines(text: str = ""):
#     return predict_medicine(mysql, text)


