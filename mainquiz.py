from quiz import Quiz
quiz_list = []
user_ans = []
correct_ans = []
def DisplayHeader():
    Title = "Python Quizzes Test"
    ch = '*'
    sp = ' '
    print(f"{ch * (len(Title) + 40)}")
    print(f"*{sp * 19}{Title}{sp * 19}*")
    print(f"{ch * (len(Title) + 40)}")
    print()

def loadQuiz():
    with open('question.txt','r') as f:
        while True:
            quest = f.readline()
            if quest == 'End Of Quiz\n':
                break
            opts = [f.readline(), f.readline(), f.readline(), f.readline()]
            correct_ans.append(opts[0])
            quiz = Quiz(quest,opts)
            quiz_list.append(quiz)
            f.readline()
def getuserans():
    ans = input('enter your answer: ')
    while ans not in '1234':
        print('invaild answer')
        ans = input('enter: ')
    return int(ans)
def displayquiz():
    no = 0
    for quiz in quiz_list:
        no += 1
        print(f'q{no}){quiz}')
        user_index = getuserans()-1
        user_ans.append(quiz.options[user_index])
def displayresult():
    marks = 0
    for i in range(len(quiz_list)):
        if user_ans[i] == correct_ans[i]:
            marks += 1
    print(f'Your mark: {marks}/{len(quiz_list)}')
def main():
    DisplayHeader()
    loadQuiz()
    displayquiz()
    displayresult()
main()




