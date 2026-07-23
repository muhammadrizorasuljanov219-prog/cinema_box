import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

TOKEN = os.getenv("TOKEN")
ADMIN_ID = 8003780362

print("Current folder:", os.getcwd())
print(".env exists:", os.path.exists(".env"))
print("TOKEN =", TOKEN)