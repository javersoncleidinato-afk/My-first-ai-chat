import requests
import urllib.parse

memory_limit = 10

rules = [
    "not defined"
]

memory = []

def chat(prompt):
    global memory

    context = "\n".join(rules + memory[-memory_limit*2:])  # memory limit applied

    full_prompt = f"""
Context:
{context}
User:
{prompt}
Response:
"""
    url = "https://text.pollinations.ai/" + urllib.parse.quote(full_prompt)

    try:
        response = requests.get(url)
        return response.text
    except:
        return "Request error"

while True:
    message = input("You: ")

    reply = chat(message)

    memory.append(f"User: {message}")
    memory.append(f"AI: {reply}")

    memory = memory[-memory_limit*2:]

    print("AI:", reply)