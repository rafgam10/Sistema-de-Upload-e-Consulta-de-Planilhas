from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = f"mysql_pymysql://{os.getenv("USER_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOST_DB")}:{os.getenv("PORT_DB")}/{os.getenv("NAME_DB")}"
    