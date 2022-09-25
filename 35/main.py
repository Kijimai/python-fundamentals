import os
from dotenv import load_dotenv

load_dotenv()

print(print(os.getenv("OWM_API_KEY")))