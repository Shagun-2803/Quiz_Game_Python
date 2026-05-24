import json

def load_questions():
  try:
    with open("questions.json","r") as file:
      data = json.load(file)
      return data
  
  except FileNotFoundError:
    return []


def start(questions):
  points = 0

  for qnum,question in enumerate(questions, start = 1):
    print(f'Question {qnum}: {question["question"]}')
    
    for oletter,oname in question["options"].items():
      print(f"{oletter} : {oname}")
    
    answer = input("Enter your answer: ")
    
    if answer.upper() in question["options"]:

      if(answer.upper() == question["correct_option"]):
        print(f"Your Option is correct!")
        points += 1;
      else:
        print("Incorrect Answer!")
    
    else:
      print("Enter valid option")
    print()
  print(f"Your final score is: {points}")



questions = load_questions()

start(questions)

# def main():
#   print("Welcome to this quix game!")

#   print("Rules of this quiz game are: ")
#   print("1. Each questions has 4 options and 1 is the correct answer.")
#   print("2. Choose only one option by writing the option letter as only one answer exists.")
#   print("3. Each correct option gives only one point.")

#   print()

#   name = input("Enter your name: ")
#   print(f"Hello, {name}.")
  
#   start = input("Press 0 to Start.")

#   try :
#     if(start == 0):
#       questions = load_questions()











# main()


