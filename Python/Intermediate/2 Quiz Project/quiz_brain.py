# class QuizBrain:
#     def __init__(self,q_list):
#         self.question_number = 0
#         self.question_list =q_list
#
#     def next_question(self):
#         input(f"Q{self.question_number+1}. {self.question_list[self.question_number].text} (True/False): ")
#         self.question_number+=1

class QuestionBank:
    def __init__(self):
        self.question_number=0
        self.score=0

    def quiz(self,q_list):
        for q_object in q_list:
            self.question_number += 1
            answr=input(f"Q{self.question_number}: {q_object.text} (True/False): ")
            if answr==q_object.answer:
                print("You are right.")
                self.score+=1
            else:
                print("You are wrong.")
            print(f"The correct answer was: {q_object.answer}.")
            print(f"Your current score is: {self.score}/{self.question_number}\n")
        print("\nYou've completed the quiz.")
        print(f"Your final score was: {self.score}/{self.question_number}")
