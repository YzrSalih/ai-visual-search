from sqlalchemy import Column, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime
import os

# SQLite dosyası backend/ klasöründe app.db olarak dursun
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "app.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

# Engine + Session
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Image(Base):
    __tablename__ = "images"
    id = Column(String, primary_key=True, index=True)        # uuid
    filename = Column(String, index=True)                    # orijinal isim
    stored_name = Column(String, unique=True, index=True)    # diske kaydedilen isim
    filepath = Column(String)                                # tam path
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
