from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from embedder_retriever import retriever
from model import llm, prompt


question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

results = rag_chain.invoke(
    {"input": "Create a blogpost about handbag styles and identities of their owners. "}
)

print(results["answer"], "aaaanssssssweeeer")
