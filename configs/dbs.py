from sqlalchemy import create_engine, MetaData
import pymysql
# import configs

engine = create_engine("mysql+pymysql://root:41526374@localhost:3306/test")
meta = MetaData()
conn = engine.connect()
