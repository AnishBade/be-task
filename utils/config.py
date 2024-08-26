import os
from dotenv import load_dotenv

class Settings:
    load_dotenv()
    EMAIL_HOST_USER: str = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD: str = os.getenv("EMAIL_HOST_PASSWORD")



settings = Settings()
