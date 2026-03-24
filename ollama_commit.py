import os
import requests
import random
from datetime import datetime

BASE_PATH = "/home/criativo/Documents/Coding/Daily_Streak_GitHub/Daily_Streak"

OLLAMA_URL = "http://localhost:11434/api/generate"

TOPICS = [
    "FastAPI CRUD example",
    "Python utility function",
    "SQL query optimization",
    "Data structures in Python",
    "REST API design example",
    "Background task processing",
    "File handling in Python",
    "Algorithm implementation",
]

def generate_code(topic):
    prompt = f"""
Generate a clean, minimal, production-style code snippet for: {topic}

Rules:
- Keep it short (10–30 lines)
- No explanations
- Only code
- Use proper formatting
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


def save_file(code):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{BASE_PATH}/ai_{timestamp}.py"

    with open(filename, "w") as f:
        f.write(code)

    return filename


def git_commit(file):
    os.chdir(BASE_PATH)
    message = f"feat(ai): add {os.path.basename(file)}"

    os.system("git add .")
    os.system(f'git commit -m "{message}"')


def main():
    commits = random.randint(3, 6)

    for _ in range(commits):
        topic = random.choice(TOPICS)
        code = generate_code(topic)

        if code.strip():
            file = save_file(code)
            git_commit(file)

    os.system("git push origin main")


if __name__ == "__main__":
    main()