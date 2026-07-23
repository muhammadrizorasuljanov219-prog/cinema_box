import os
from dotenv import load_dotenv

load_dotenv()  # Lokal kompyuterda .env ni o'qiydi, Railway'da esa environment variables ishlaydi

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "8003780362"))

print("Current folder:", os.getcwd())
print("TOKEN =", TOKEN)