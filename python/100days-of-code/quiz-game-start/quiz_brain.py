class QuizBrain:

    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number} {current_question.text}\n\n(True/False): ")
        if user_answer == "t":
            user_answer = "True"
        elif user_answer == "f":
            user_answer = "False"
        else:
            print("your answer shoudl be True/False")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right! ")
            self.score += 1
        else:
            print(f"That's not the right answer!\nThe correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
