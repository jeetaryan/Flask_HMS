# main.py

from app import create_app
import os
from dotenv import load_dotenv

app=create_app()
load_dotenv()

if __name__=="__main__":
    app.run(debug=os.getenv('FLASK_DEBUG'),port='0.0.0.0')