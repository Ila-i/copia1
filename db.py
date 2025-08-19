from sqlalchemy import create_engine

DB_PATH = r"C:\Users\ilari\Desktop\FARMALINE_1.db"
engine = create_engine(f"sqlite:///{DB_PATH}")
connection = engine.connect()