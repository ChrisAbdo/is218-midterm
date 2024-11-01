from dotenv import load_dotenv
import os
load_dotenv()

settings = {key: value for key, value in os.environ.items()}

print(settings.get('DATABASE_USERNAME'))