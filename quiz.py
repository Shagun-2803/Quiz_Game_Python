import json

def load_questions():
  try:
    with open("questions.json","r") as file:
      data = json.load(file)
      return data
  
  except FileNotFoundError:
    return []

questions = load_questions()

for qnum,question in enumerate(questions, start = 1):
  print(f'Question {qnum}: {question["question"]}')
  for oletter,oname in question["options"].items():
    print(f"{oletter} : {oname}")
  




# print("Welcome to this quix game!")

# print("Rules of this quiz game are: ")
# print("1. Each questions has 4 options and 1 is the correct answer.")
# print("2. Choose only one option by writing the option letter as only one answer exists.")
# print("3. Each correct option gives only one point.")

# print('Click Enter to start')

# name = input("Enter your name: ")
# print(f"Hello, {name}.\nPress Enter to Start.")

