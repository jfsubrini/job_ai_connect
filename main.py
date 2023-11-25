#!/usr/bin/env python3
# pylint: disable=
"""job_ai_connect project.
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  # take environment variables from .env.
# Access the API key using the variable name defined in the .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return completion.choices[0].message.content

user_prompt = input("Your prompt : ")
response = get_completion(user_prompt)
print(response)
