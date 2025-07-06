import asyncio
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
    subject = "Carrot"
    system_template = "You are a helpful assistant that generates jokes " \
    "based on the input text."

    langchat = LangChat(system_template)

    print("Original:", subject)
    print("\n")

    joke = langchat.generate_joke(subject)
    print("Joke:", joke)
    print("\n")

    print("Asyn joke:")
    asyncio.run(langchat.generate_joke_async(subject))
    print("\n")

    joke = langchat.generate_joke_chat_template(
        system_template,
        subject
    )
    print("Joke from chat template:", joke)
    print("\n")
    
if __name__ == "__main__":
    main()