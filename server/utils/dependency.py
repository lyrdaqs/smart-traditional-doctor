from fastapi.security import OAuth2PasswordBearer
from utils.security import get_current_user
from model.Comment import Comment
from datetime import datetime
from persiantools.jdatetime import JalaliDate
from pytz import timezone
from fastapi import Depends, HTTPException
from utils.gateway import mongo_conn


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_current_utc_time():
    utc_now = datetime.now(timezone('UTC'))
    tehran_time = utc_now.astimezone(timezone('Asia/Tehran'))
    formatted_date = JalaliDate(tehran_time.date()).strftime('%A - %d %B %Y')
    formatted_time = f"ساعت {tehran_time.strftime('%H:%M')}"
    timestamp = f"{formatted_date} {formatted_time}"
    return timestamp


def get_comment_with_username(comment: Comment, token: str = Depends(oauth2_scheme)):
    username = get_current_user(token)
    comment_dict = comment.dict()
    comment_dict['username'] = username
    comment_dict['timestamp'] = get_current_utc_time()
    return comment_dict


def check_admin_access(token: str = Depends(oauth2_scheme)):
    username = get_current_user(token)
    user_db = mongo_conn.get_user(username)
    if 'role' in user_db:
        if user_db['role'] == "admin":
            return True
    raise HTTPException(status_code=400, detail="User not access")