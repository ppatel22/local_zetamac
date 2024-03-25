import random

operations = ['+', '-', '//', '*']  # Add '*' for multiplication

def generate_question():
    operation = random.choice(operations)
    
    if operation == '+':
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000 - num1)
        return f"{num1} {operation} {num2}"
    elif operation == '-':
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, num1)
        return f"{num1} {operation} {num2}"
    elif operation == '*':  # Multiplication
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        return f"{num1} {operation} {num2}"
    else:  # Division
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, num1)
        while num1 % num2 != 0 or num1 // num2 > 12:  # Ensure divisible and result <= 12
            num1 = random.randint(1, 1000)
            num2 = random.randint(1, num1)
        return f"{num1} {operation} {num2}"

def generate_valid_question():
    question = generate_question()
    answer = eval(question)
    while not (isinstance(answer, int) and answer > 0 and answer < 1000):
        question = generate_question()
        answer = eval(question)
    return question, answer

def generate_multiple_questions():
    questions = []
    answers = []
    for i in range(200):
        question = generate_question()
        answer = eval(question)
        while not (isinstance(answer, int) and answer > 0 and answer < 1000):
            question = generate_question()
            answer = eval(question)
        questions.append(question)
        answers.append(answer)
    return questions, answers

# Example usage
question, answer = generate_valid_question()
print(question)