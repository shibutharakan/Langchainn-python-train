import os
from dotenv import load_dotenv
from langchat import LangChat

env = os.getenv('APP_ENV', 'development')

try:
        dotenv_path = f'.env.{env}'
        load_dotenv(dotenv_path)
except:
        print("Failed to load environment variables from .env file. "
              "Ensure the file exists and is correctly formatted.")
        
print(f"Running in {env} environment")

def main():
    text = "Hello, how are you?"
    langchat = LangChat("Translate the following from English into Arabic")
    translated = langchat.translate_text(text)

    print("Translated:", translated)

if __name__ == "__main__":
    main()