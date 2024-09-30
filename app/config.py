import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')
    # Start Database block
    host = os.getenv('MYSQL_HOST')
    port = os.getenv('MYSQL_PORT', 3306)  # Default to 3306 if not set
    database = os.getenv('MYSQL_DATABASE')
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASSWORD', '')
    SQLALCHEMY_DATABASE_URI= f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
    # End Database
    SQLALCHEMY_TRACK_MODIFICATION=False
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')

obj = Config()
print(obj.SQLALCHEMY_DATABASE_URI)
