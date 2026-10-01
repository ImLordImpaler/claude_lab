from app.llm.factory import get_llm
from app.memory.conversation import get_conversation_store



class ChatService():
    def __init__(self):
        self.llm = get_llm()
        self.store = get_conversation_store

    async def chat(self, message:str, conversation_id:str)-> str:
        
        conversation = self.store.get_or_create(conversation_id=conversation_id)
        
        conversation.messages.append({
            "role":"user",
            "content": message
        })
        
        response = await self.llm.generate(conversation.messages)
        
        conversation.messages.append({
            "role":"agent",
            "content": response,
        })

        return response
