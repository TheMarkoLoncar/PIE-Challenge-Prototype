import speech_recognition as sr

problem = ''
attempted_solutions = ''
r = sr.Recognizer()
mic = sr.Microphone()

def get_problem():
    global problem
    print('What is your problem?')
    with mic as source:
        problem_audio = r.listen(source)

    problem = str(r.recognize_google(problem_audio))
    print('got it!')
    return problem

def get_attempted_solutions():
    global attempted_solutions
    print('What solutions have you tried?')
    with mic as source:
        attempted_solutions_audio = r.listen(source)

    attempted_solutions = str(r.recognize_google(attempted_solutions_audio))
    print('got it!')
    return attempted_solutions