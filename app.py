from flask import Flask,render_template,jsonify,request
from flask_cors import CORS
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv

from src.prompt import *
import os

load_dotenv()

app=Flask(__name__)
CORS(app)

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY =os.getenv("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"]=PINECONE_API_KEY
os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY
chatmodel=ChatOpenAI(model="gpt-4o")

embeddings=download_embeddings()
index_name="medical-chatbot"

docsearch=PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
retriever=docsearch.as_retriever(search_type="similarity",search_kwargs={"k":3})
prompt=ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),
        ("human","{input}")
    ]
)
question_answer_chain=create_stuff_documents_chain(chatmodel,prompt)
rag_chain=create_retrieval_chain(retriever,question_answer_chain)

@app.route("/")
def index():
    return jsonify({"message": "Medical Chatbot API is running"})

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_input = data.get("message", "")
        
        if not user_input:
            return jsonify({"error": "Message is required"}), 400
        
        response = rag_chain.invoke({"input": user_input})
        return jsonify({
            "success": True,
            "answer": response.get("answer", ""),
            "question": user_input
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)