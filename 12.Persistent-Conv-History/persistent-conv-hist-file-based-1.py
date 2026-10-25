import os
import json

from langchain_openai import ChatOpenAI

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

from langchain_core.chat_history import (
    BaseChatMessageHistory
)

from langchain_core.messages import (
    BaseMessage,
    message_to_dict,
    messages_from_dict
)

from langchain_core.runnables.history import (
    RunnableWithMessageHistory
)


# ========================================
# 1. PERSISTENT CHAT HISTORY
# ========================================

class FileChatMessageHistory(
    BaseChatMessageHistory
):

    def __init__(
        self,
        session_id,
        storage_path="chat_history"
    ):

        # Python doesn't require you to declare instance attributes in advance. 
        # If self.session_id doesn't already exist, this assignment creates it. 
        # If it already exists, the assignment updates its value.
        self.session_id = session_id
        
        # chat_history folder does not exist: Creates the folder.
        # chat_history folder already exists: Does nothing; no error is raised.
        # exist_ok=False and folder already exists	Raises a FileExistsError.
        
        os.makedirs(
            storage_path,
            exist_ok=True
        )
        # This statement only creates the path string. It does not create the folder or the JSON file.
        # output: chat_history/mouli.json
        self.file_path = os.path.join(
            storage_path,
            f"{session_id}.json"
        )


    # ------------------------------------
    # LOAD MESSAGES
    # ------------------------------------

    @property
    def messages(self):

        if not os.path.exists(
            self.file_path
        ):
            return []

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return messages_from_dict(
            data
        )

    # ------------------------------------
    # SAVE MESSAGES
    # ------------------------------------

    def add_messages(
        self,
        messages: list[BaseMessage]
    ) -> None:

        all_messages = list(
            self.messages
        )

        all_messages.extend(
            messages
        )

        serialized = [
            message_to_dict(message)
            for message in all_messages
        ]

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                serialized,
                file,
                ensure_ascii=False,
                indent=2
            )


    # ------------------------------------
    # CLEAR HISTORY
    # ------------------------------------

    def clear(self) -> None:

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file
            )


# ========================================
# 2. CREATE MODEL
# ========================================

llm = ChatOpenAI(
    model="gpt-5.6-luna",
    api_key=os.getenv("OPENAI_API_KEY")
)


# ========================================
# 3. CREATE PROMPT
# ========================================

prompt = ChatPromptTemplate.from_messages(

    [
        (
            "system",
            """
            You are a helpful AI assistant.
            Answer in simple English.
            """
        ),

        MessagesPlaceholder(
            variable_name="history"
        ),

        (
            "human",
            "{question}"
        )
    ]
)


# ========================================
# 4. CREATE LCEL CHAIN
# ========================================

chain = (
    prompt
    | llm
)

# ========================================
# 5. GET SESSION HISTORY
# ========================================

def get_session_history(
    session_id
):

    return FileChatMessageHistory(
        session_id
    )


# ========================================
# 6. ADD MESSAGE HISTORY
# ========================================

chatbot = RunnableWithMessageHistory(

    chain,
    get_session_history,

    input_messages_key="question",

    history_messages_key="history"
)


# ========================================
# 7. GET SESSION ID
# ========================================

session_id = input(
    "Enter session id: "
)


print("\nAI Chatbot")
print("Type 'exit' to stop")
print("------------------------")
# ========================================
# 8. CHAT LOOP
# ========================================

while True:

    user_input = input(
        "\nYou: "
    )


    if user_input.lower() == "exit":

        print(
            "Chat ended."
        )

        break


    response = chatbot.invoke(

        {
            "question": user_input
        },

        config={
            "configurable": {
                "session_id":
                session_id
            }
        }
    )


    print(
        "AI:",
        response.content
    )