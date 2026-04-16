import requests

API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = "YOUR_API_KEY"

def ask_ai(question: str) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful study assistant for engineering students."},
            {"role": "user", "content": question}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_question = input("Enter your question: ")
    try:
        answer = ask_ai(user_question)
        print("\nAI Answer:\n")
        print(answer)
    except Exception as e:
        print(f"Error: {e}")
