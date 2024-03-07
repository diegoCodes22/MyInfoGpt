import os
import sys
import openai
from random import randint
from apikey import API_KEY


def generate_response(prompt):
    client = openai.OpenAI(
        api_key=API_KEY
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.5,
        messages=[
            {"role": "system", "content": "You are my personal assistant, I will provide you with all the relevant information. You can NOT use any other information, exclusively the information that I provide, and take it as absolute truth"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


def read_doc(doc_path: str) -> str:
    with open(doc_path, "r", encoding="utf-8") as file:
        return file.read()


def write_response(response: str, folder_path: str):
    answer_file = f"answer{randint(0, 999)}.txt"
    answer_folder = os.path.join(folder_path, "answers/")
    filename = os.path.join(answer_folder, answer_file)
    with open(filename, "w+", encoding="utf-8") as file:
        file.write(response)
        print(f"Answer file: {filename}\n\n")


def main():
    folder_path = input("Folder path, or empty for standard path: ")
    if folder_path == "":
        folder_path = "/Users/superdiegui/Desktop/myinfogpt/"
    filename = sys.argv[1]
    doc_path = os.path.join(folder_path, filename)
    document = read_doc(doc_path)
    while True:
        query = input("Enter your query (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        prompt = f"Query: {query}\nDocuments: {document}"
        response = generate_response(prompt)
        write_response(response, folder_path)
        print(response)


if __name__ == "__main__":
    main()
