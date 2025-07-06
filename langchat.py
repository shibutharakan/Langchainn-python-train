from langchain.chat_models import init_chat_model 
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
import asyncio

class LangChat:
    
    def __init__(self, system_message:str, model_name:str="gpt-4o", model_provider:str="openai"):
        self.model = init_chat_model(model=model_name, model_provider=model_provider)
        self.system_message = system_message

    def generate_joke(self, text: str) -> str:
        messages = [
            SystemMessage(self.system_message),
            HumanMessage(text)
        ]

        # Invoke the model with the messages
        response = self.model.invoke(messages)

        return response.content

    async def generate_joke_async(self, text: str) -> str:
        messages = [
            SystemMessage(self.system_message),
            HumanMessage(text)
        ]

        async for chunk in self.model.astream(messages):
            print(chunk.content, end="|", flush=True)
            await asyncio.sleep(0.5)  # Add a 0.5 second delay after each chunk

    def generate_joke_chat_template(self, system_template: str, subject:str) -> str:
        prompt_template = ChatPromptTemplate.from_messages(
            [("system", system_template), ("user", "{text}")])
        prompt = prompt_template.invoke(input=subject)
        prompt.to_messages()
        response = self.model.invoke(prompt)
        return response.content;