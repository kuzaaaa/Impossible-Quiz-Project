

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "How many cubes are in GD?\n(a) m8 they aint coobs\n(b)69\n(c)how should I know",
     "How many squares do you see?\n(a) none what are you talking about\n(b)2\n(c)uhhhhhh",
     "What is actually near Turkey?\n(a) THIS IS THE FRENCH\n(b)THIS IS SPARTA\n(c)no",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "b"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)
