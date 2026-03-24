#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
RAG (Retrieval-Augmented Generation) example using LangGraph.

Demonstrates how to:
- Load web documents and split them into chunks
- Create embeddings using AWS Bedrock (Titan) and store in an in-memory vector store
- Define a retriever tool that the LLM can invoke to search the documents
- Use an Anthropic LLM that decides whether to retrieve or respond directly
"""

import boto3
import datetime
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_aws import BedrockEmbeddings
from langchain.tools import tool

from langgraph.graph import MessagesState
from langchain_anthropic import ChatAnthropic

def get_bedrock_runtime_client():
    """Create and return a Bedrock runtime client using the brd3 profile."""
    session = boto3.Session(profile_name="brd3", region_name="us-east-1")
    client = session.client("bedrock-runtime")

    return client

def get_llm_model():
    """Initialize and return the Anthropic Claude LLM."""
    client = get_bedrock_runtime_client()

    response_model = ChatAnthropic(model="claude-haiku-4-5-20251001",
                                   temperature=0)

    return response_model

# Retriever tool — searches the vector store for blog content relevant to the query.
# The retriever variable is set later after the vector store is created.

@tool
def retrieve_blog_posts(query: str) -> str:
    """Search and return information about Lilian Weng blog posts."""
    docs = retriever.invoke(query)
    return "\n\n".join([doc.page_content for doc in docs])


retriever_tool = retrieve_blog_posts


def load_documents():
    """Fetch blog posts from URLs, flatten, and split into chunks.

    Uses RecursiveCharacterTextSplitter with tiktoken encoding to split
    documents into ~100 token chunks with 50 token overlap.
    """
    urls = [
        "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/",
        "https://lilianweng.github.io/posts/2024-07-07-hallucination/",
        "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/",
    ]

    docs = [WebBaseLoader(url).load() for url in urls]
    docs[0][0].page_content.strip()[:1000]
    docs_list = [item for sublist in docs for item in sublist]

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=100, chunk_overlap=50
    )
    doc_splits = text_splitter.split_documents(docs_list)
    doc_splits[0].page_content.strip()
    print(f"docs len: {len(docs)}, type: {type(docs)}")
    return doc_splits


def create_vectorStore(docSplits):
    """Embed document chunks using Bedrock Titan and store in an in-memory vector store.

    Returns a retriever that performs similarity search over the stored embeddings.
    """
    client = get_bedrock_runtime_client()
    embeddings = BedrockEmbeddings(
        client=client,
        model_id="amazon.titan-embed-text-v1",
        region_name="us-east-1"
    )
    vectorstore = InMemoryVectorStore.from_documents(
        documents=docSplits, embedding=embeddings
    )
    retriever = vectorstore.as_retriever()
    return retriever


def generate_query_or_respond(state: MessagesState):
    """Call the model to generate a response based on the current state. Given
    the question, it will decide to retrieve using the retriever tool, or simply respond to the user.
    """
    response = (
        response_model
        .bind_tools([retriever_tool]).invoke(state["messages"])
    )
    return {"messages": [response]}


docSplits = load_documents()
retriever = create_vectorStore(docSplits)
response_model = get_llm_model()


print(f"Time: 5: {datetime.datetime.now()}")
input = {"messages": [{"role": "user", "content": "hello!"}]}
generate_query_or_respond(input)["messages"][-1].pretty_print()
print(f"Time: 6: {datetime.datetime.now()}")
