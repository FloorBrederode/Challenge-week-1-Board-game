# Multiple choice questions
choice_question = 0

def questions():
    # How long no food
    if choice_question == 0:
        print('How long can a person go without food?')
        print('A: 8 to 21 Days.')
        print('B: 21 to 36 Days.')
        print('C: 36 to 45 Days.')
        answer_choice = input('A, B, or C?').lower().strip()
        if answer_choice == 'a':
            print('Correct')
            choice_question += 1
        elif answer_choice == 'b':
            print('Incorrect')
            choice_question += 1
        elif answer_choice == 'c':
            print('Incorrect')
            choice_question += 1

    # how much radiation?
    if choice_question == 1:
        print('Who invented the nuclear bomb')
        print('A: Lea Szilard.')
        print('B: J. Robert Oppenheimer.')
        print('C: Cillian Murphy.')
        answer_choice = input('A, B, or C?').lower().strip()
        if answer_choice == 'a':
            print('Incorrect')
            choice_question += 1
        elif answer_choice == 'b':
            print('Correct')
            choice_question += 1
        elif answer_choice == 'c':
            print('Incorrect')
            choice_question += 1
    # correct j. Robert Oppenheimer
    # incorrect Lea Szilard
    # incorrect Cillan Murphy

    # mafths
    print('The radiation level in a certain area dubbles every hour.')
    print('If the radiation level is initially at 10 millisieverts per hour (mSv/h),')
    print('what will be the radiation level after 3 hours?')
    # correct 80 millisieverts per hour (mSv/h)
    # incorrect 40 millisieverts
    # incorrect 60 millisieverts
    # incorrect 30 millisieverts


    # Who invented nuclear bomb
    print('What is the minimum amout of radiation that will kill you?')
    # correct a dose of 1000 mSv (millisievert)
    # incorrect a doese of 100 mSv
    # incorrect a dose of 10000 mSv