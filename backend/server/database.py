import sqalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("")

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = DBSession()
