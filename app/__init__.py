import os
import base64
from dotenv import load_dotenv

secret_key = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')
print(secret_key)  # This will print a random secret key

load_dotenv()
my_secret_key = os.getenv("MY_SECRET_KEY")