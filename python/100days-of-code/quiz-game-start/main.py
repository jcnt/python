from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    q_text = i["text"]
    q_answer = i["answer"]
    new_question = Question(q_text, q_answer)
    # question_bank.append(Question(i['text'], i['answer']))
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz!")
print(f"\n\n\n==== Your final score is {quiz.score}/{quiz.question_number} ====")
