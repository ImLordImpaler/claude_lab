from dataclasses import dataclass, field

@dataclass
class Conversation:
    id: str
    messages: list[dict[str, str]] = field(default_factory=list)


class ConversationStore:
    # This will act like a conversation store interface

    def __init__(self):
        self._conversations: dict[str, Conversation] = {}

    def get_or_create(self, conversation_id) -> Conversation:
        if conversation_id not in self._conversations:
            self._conversations[conversation_id] = Conversation(id = conversation_id)
        
        return self._conversations[conversation_id]
    
get_conversation_store = ConversationStore()

