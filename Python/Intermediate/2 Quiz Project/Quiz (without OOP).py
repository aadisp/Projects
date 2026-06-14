from data import question_data
question_number=0
score=0


for i in range(0,10):
    ans=input(f"Q{question_number+1}: {question_data[i]["text"]} (True/False): ")
    if ans==question_data[i]["answer"]:
        print("You are right.")
        score+=1
    else:
        print("You are wrong.")
    print(f"The correct answer was: {question_data[i]["answer"]}")
    print(f"Your current score is: {score}/{question_number+1}\n")
    question_number+=1
print("\nYou've completed the quiz.")
print(f"Your final score was: {score}/10")