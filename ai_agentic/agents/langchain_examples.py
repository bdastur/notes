#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import langchain_core.messages as lcmessages
import langchain.tools as lctools
import langchain.agents as lcagents

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrockConverse

@lctools.tool
def get_weather_for_location(city: str) -> str:
    """Get weather for a location."""
    print("Calling tool get_weather_for_location")

    return f"It's always sunny in {city}"


@lctools.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print(f"Add {a} and {b}")
    return a + b


@lctools.tool
def subtract(a: int, b: int) -> int:
    """Subtract the second argument (int) from the first argument (int)"""
    print(f"Subtract {b} from {a}")
    return a - b


def create_llm(profile="brd3", region="us-east-1"):
    """Initialize and return the Bedrock LLM."""

    llm = ChatAnthropic(model="claude-haiku-4-5-20251001")
    return llm


def example_one():
    """Basic LLM invocation with system and human messages.

    Shows how to use SystemMessage to set the LLM's role/behavior
    and HumanMessage to provide user input, then invoke the model
    directly without chains or output parsers.
    """
    llm = create_llm()
    systemPrompt = \
        """You are a helpful assistant that translates English to French.
            Translate the user sentence"""

    messages = [lcmessages.SystemMessage(content=systemPrompt)]
    messages.append(lcmessages.HumanMessage(content="I love programming"))

    aiMsg = llm.invoke(messages)
    print(f"AI Response:  {aiMsg.content}")


def example_two():
    """Example showing use of ChatPromptTemplate.

    """
    llm = create_llm()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a concise assistant. Answer in one sentence."),
        ("human", "{question}"),
    ])

    chain = prompt | llm | StrOutputParser()

    answer = chain.invoke({"question": "What is LangChain?"})
    print(f"Answer: {answer}")


def example_three():
    """Example showing tool use
    """

    # Create the model/llm
    llm = create_llm()
   
    # Specify tools for tool use.
    llmWithTools = llm.bind_tools([get_weather_for_location])

    # a struct defining tool name and function.
    tools = {
        "get_weather_for_location": get_weather_for_location
    }

    SystemPrompt = \
        """You are an agent that will respond to user quries regarding
           weather. Youw ill use tools to get weather information"""

    messages = [lcmessages.SystemMessage(content=SystemPrompt)]

    userQuery = "What is the weather in San Jose right now?"
    messages.append(lcmessages.HumanMessage(content=userQuery))

    answer = llmWithTools.invoke(messages)

    if answer.tool_calls:
        toolName = answer.tool_calls[0]["name"]
        toolArgs = answer.tool_calls[0]["args"]
        toolId = answer.tool_calls[0]["id"]

        tool = tools.get(toolName, None)
        print("Type of tool: ", type(tool))
        if tool:
            val = tool.invoke(toolArgs)
        print("Tool val: ", val)
        messages.append(lcmessages.AIMessage(content=answer.content))
        messages.append(lcmessages.ToolMessage(content=val, tool_call_id=toolId))

        answer = llmWithTools.invoke(messages)
        print(f"Final answer: {answer.content}")
    else:
        print(f"Direct AI Response: {answer.content}")
    

def example_four():
    """Another example of Langchain agent with tool use.

    """
    llm = create_llm()
    llmWithTools = llm.bind_tools([add, subtract])

    systemPrompt = \
        """
        You are a helpful assitant, that helps to perform math operations.
        You will use tools at your disposal to perform operations. If a tool is unavaibale,
        you will return a message indicating your inability to perform the task.
        """
    

    messages = []
    tools = {
        "add": add,
        "subtract": subtract
    }

    userPrompt = ""
    conversationId = 0
    while True:
        userPrompt = input("Enter text: ")

        if not userPrompt:
            continue

        if userPrompt.lower() in ["q", "quit", "exit"]:
            break

        messages.append(HumanMessage(content=userPrompt))
     
        print (f"Conversation {conversationId} ---------------------- ")
        conversationId += 1

        step = 1
        while True:
            response = llmWithTools.invoke(messages)
            messages.append(AIMessage(content=response.content))
             
            if not response.tool_calls:
                # Return this reponse
                print(f" Final Response: {response.content}")
                break
            
            # Tool call is needed.
            toolName = response.tool_calls[0]["name"]
            toolArgs = response.tool_calls[0]["args"]
            toolId = response.tool_calls[0]["id"]
            print(f" #    Step {step} Using tool {toolName} with arguments {toolArgs}")

            tool = tools.get(toolName, None)
            if not tool:
                print("Tool not found ", toolName)
                continue

            val = tool.invoke(toolArgs) 
            messages.append(ToolMessage(content=val, tool_call_id=toolId))
            step += 1

       




EXAMPLES = {
    "1": example_one,
    "2": example_two,
    "3": example_three,
    "4": example_four
}

def build_epilog():
    lines = ["Available examples:"]
    for key, func in EXAMPLES.items():
        desc = func.__doc__.strip().split("\n")[0] if func.__doc__ else "No description"
        lines.append(f"  {key}: {desc}")
    lines.append("\nUsage: ./langchain_examples.py -id 1")
    return "\n".join(lines)

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Run LangChain examples by ID.",
        epilog=build_epilog(),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("-id", required=True, choices=EXAMPLES.keys(),
                        help="Example to run: " + ", ".join(EXAMPLES))
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    
    EXAMPLES[getattr(args, "id")]()


if __name__ == '__main__':
    main()
