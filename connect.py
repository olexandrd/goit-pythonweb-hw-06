"""
This module is used to connect to the database.
"""

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from settings import DB_URL

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()
