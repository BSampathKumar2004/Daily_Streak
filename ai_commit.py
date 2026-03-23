import os
import random
from datetime import datetime

BASE_PATH = "/home/criativo/Documents/Coding/Daily_Streak_GitHub/Daily_Streak"

# Different categories (acts like AI brain)
templates = [
    {
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
        "lang": "py",
        "content": """# Utility: Fibonacci
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a
"""
    },
    {
        "lang": "sql",
        "content": """-- SQL Query
SELECT name, COUNT(*) 
FROM users 
GROUP BY name;
"""
    },
    {
        "lang": "js",
        "content": """// Node.js API
const express = require('express');
const app = express();

app.get('/', (req, res) => res.send('Hello'));
app.listen(3000);
"""
    },
    {
        "lang": "py",
        "content": """# Background Task Simulation
import time

def process():
    time.sleep(2)
    print("Task Done")
"""
    }
]

def generate_file():
    item = random.choice(templates)
    ext = item["lang"]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{BASE_PATH}/ai_{timestamp}.{ext}"

    with open(filename, "w") as f:
        f.write(item["content"])

    return filename, ext


def git_commit(file, ext):
    os.chdir(BASE_PATH)
    message = f"feat({ext}): add {os.path.basename(file)}"

    os.system("git add .")
    os.system(f'git commit -m "{message}"')


def main():
    commits = random.randint(3, 6)

    for _ in range(commits):
        file, ext = generate_file()
        git_commit(file, ext)

    os.system("git push origin main")


if __name__ == "__main__":
    main()