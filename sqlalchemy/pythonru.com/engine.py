from sqlalchemy import  create_engine

engine = create_engine('sqlite:///sqlite3.db', echo=True)
engine.connect()

print(engine)