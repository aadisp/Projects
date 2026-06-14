# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain
#
# question_bank=[]
#
# for questions in question_data:
#     question_bank.append(Question(questions["text"],questions["answer"]))
#
# quiz=QuizBrain(question_bank)
# quiz.next_question()

from data import question_data
from question_model import Question
from quiz_brain import QuestionBank

question_list=[]
for question in question_data:
    txt=question["text"]
    ans=question["answer"]
    new_question = Question(txt, ans)
    question_list.append(new_question)

questions=QuestionBank()
questions.quiz(question_list)
