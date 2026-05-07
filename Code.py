import requests
import urllib.parse
api_key = "your key here(optional)"

rules = [
    "not defined"
]

memory = []

def chat(prompt):
    global memory
    context = "\n".join(rules + memory)
    full_prompt = f"""
Context:
{context}
User:
{prompt}
Response:
"""
    url = "https://text.pollinations.ai/" + urllib.parse.quote(full_prompt)
    response = requests.get(url)
    return response.text


while True:
    message = input("You: ")

    reply = chat(message)

    memory.append(f"User: {message}")
    memory.append(f"AI: {reply}")

    print("IA:", reply)