# Multiple choice questions

def questions(number_question):
    choice_question = number_question
    while True:
        # How long no food
        if choice_question == 1:
            print('How long can a person go without food?')
            print('A: 8 to 21 Days.')
            print('B: 21 to 36 Days.')
            print('C: 36 to 45 Days.')
            answer_choice = input('A, B, or C? ').lower().strip()
            if answer_choice == 'a':
                print('Correct')
                choice_question += 1
            elif answer_choice == 'b':
                print('Incorrect')
                choice_question += 1
            elif answer_choice == 'c':
                print('Incorrect')
                choice_question += 1
            else:
                print('Invalid Input')
            break

        # how much radiation?
        if choice_question == 2:
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
            break

        # mafths
        if choice_question == 3:
            print('The radiation level in a certain area dubbles every hour.')
            print('If the radiation level is initially at 10 millisieverts per hour (mSv/h),')
            print('what will be the radiation level after 3 hours?')
            print('A: 30 millisieverts per hour (mSv/h)')
            print('B: 40 millisieverts per hour (mSv/h)')
            print('C: 60 millisieverts per hour (mSv/h)')
            print('D: 80 millisieverts per hour (mSv/h)')
            answer_choice = input ('A, B, C, or D').lower().strip()
            if answer_choice == 'a':
                print('Incorrect')
                choice_question += 1
            elif answer_choice == 'b':
                print('Correct')
                choice_question += 1
            elif answer_choice == 'c':
                print('Incorrect')
                choice_question += 1
            elif answer_choice == 'd':
                print('Correct')
                choice_question += 1
                break

        # Who invented nuclear bomb
        if choice_question == 4:
            print('What is the minimum amout of radiation that will kill you?')
            print('A: A dose of 100 mSv. (millisievert)')
            print('B: A dose of 1000 mSv. (millisievert)')
            print('C: A dose of 10000 mSv. (millisievert)')


        # What is the reccomended material for shielnidn against radiation exposure
        # lead  !!
        # aluminium
        # steel


        #what is not a symptom id acute radiation
        #haurloss
        # nasea and voliting
        # blindness !!!

        #what type of clothing provides better protecton agains radiation
        # thick wool
        # synthetic fibers
        # lead-lined suits !!!


        #which food item is generaly considers safer to consume during a radiation emergency
        # fresh prodiuce
        # canned goods !!!
        # wild game


        # which factor contributes to the spread of radiation contamination
        # wind direction !!!
        #humidity level
        #lunar phase


        #what type od water source is asafer to consume in a radiated area
        # running water !!!
        # rainwater collected in barrel
        # standing pond
