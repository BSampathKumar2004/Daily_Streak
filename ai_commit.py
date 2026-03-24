import os
import random
import time
from datetime import datetime

BASE_PATH = "/home/criativo/Documents/Coding/Daily_Streak_GitHub/Daily_Streak"
os.chdir(BASE_PATH)

templates = [
    {
        "type": "fastapi",
        "lang": "py",
        "content": """# FastAPI Example
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
"""
    },
    {
        "type": "algorithm",
        "lang": "py",
        "content": """# Fibonacci
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
"""
    },
    {
        "type": "database",
        "lang": "sql",
        "content": """-- SQL Query
SELECT name, COUNT(*) FROM users GROUP BY name;
"""
    },
    {
        "type": "backend",
        "lang": "js",
        "content": """// Express API
const express = require('express');
const app = express();

app.get('/', (req, res) => res.send('Hello'));
app.listen(3000);
"""
    }
]

def generate_file():
    item = random.choice(templates)

    ext = item["lang"]
    category = item["type"]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"{BASE_PATH}/{category}_{timestamp}.{ext}"

    with open(filename, "w") as f:
        f.write(item["content"])

    return filename, category


def git_commit(file, category):
    message = f"feat({category}): add {os.path.basename(file)}"
    os.system("git add .")
    os.system(f'git commit -m "{message}"')


def main():
    commits = random.randint(3, 6)

    for _ in range(commits):
        file, category = generate_file()
        git_commit(file, category)

        # natural delay
        time.sleep(random.randint(5, 20))

    os.system("git push origin main")


if __name__ == "__main__":
    main()