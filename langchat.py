from langchain.chat_models import init_chat_model 
from langchain_core.messages import HumanMessage, SystemMessage

class LangChat:
    
    def __init__(self, system_message:str, model_name:str="gpt-4o", model_provider:str="openai"):
        self.model = init_chat_model(model=model_name, model_provider=model_provider)
        self.system_message = system_message

    def translate_text(self, text: str) -> str:
        """Translate text from English to Arabic."""
        messages = [
            SystemMessage(self.system_message),
            HumanMessage(text)
        ]

        # Invoke the model with the messages
        response = self.model.invoke(messages)

        return response.content
