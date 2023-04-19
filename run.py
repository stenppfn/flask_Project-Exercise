from app import create_app
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app("testing")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)