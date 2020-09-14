prompts = [
    "Erick's favorite champ?\n(a) Talon\n(b) Renekton\n(c) Riven\n\n",
    "Steven's favorite champ?\n(a) Gragas\n(b) Nunu\n(c) Thresh\n\n",
    "River's favorite champ?\n(a) Zed\n(b) Lee Sin\n(c) Lucian\n\n"
]

class quest:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    quest(prompts[0],"c"),
    quest(prompts[1], "a"),
    quest(prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print ("Score: " + str(score) + " out of " + str(len(questions)) + " questions correct!")

run_test(questions)