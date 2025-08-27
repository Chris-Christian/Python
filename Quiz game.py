questions=("Which is the closest planet to the Sun in our Solar system? ",
          "Which is the hottest planet in our Solar system? ",
          "Which living being lays the largest eggs? ",
          "Which is the largest ocean on planet Earth? ",
          "How many continents are there in the world? ")
options=(("A. Earth", "B. Venus", "C. Mars", "D. Mercury"),
         ("A. Mercury", "B. Venus", "C. Jupiter", "D. Mars"),
         ("A. Blue Whale", "B. Ostrich", "C. Falcon", "D. Pigeon"),
         ("A. Indian", "B. Pacific", "C. Atlantic", "D. Arctic"),
         ("A. 6", "B. 8", "C. 7", "D. 9"))
answers=("D","B","B","B","C")
guesses=[]
score=0
question_num=0

for question in questions:
    print("----------------------------------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter (A/B/C/D): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1

results=0
print("-----------------------------")
print("|          Results          |")     
print("-----------------------------")   
print(f"Your Total score is: {score}")
results=(score/question_num)*100
print(f"Percentage: {results}%")
if results>80:
    print("Excellent!")
elif results>60:
    print("Very Good!")
elif results>40:
    print("Good")
else:
    print("Keep practicing")
print(f"Your choices: {guesses}")
print(f"Correct answers: {answers}")
