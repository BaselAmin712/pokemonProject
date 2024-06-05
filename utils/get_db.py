from constants import db_type
from models.mysql_database import Mysql_database


def get_db():
    if db_type  == "mysql":
        db = Mysql_database()
        return db
    if db_type  =="mongodb":
        pass
