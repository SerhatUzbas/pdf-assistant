from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3")

system_prompt = (
    "You are an experienced content creator."
    "Use the following pieces of retrieved context to create a blog post"
    "The content must be interesting,appealed and readable for user."
    "if you do not know about question context, say you don't know and do not request for more information."
    "Your blog post must be two paragraph maximum."
    "answer concise."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)
