# Multiple choice questions

def questions(number_question):
    choice_question = number_question
    print('''You land on a mulitple choice question tile.
    press enter to continue.''')
    input()
    while True:
        # How long no food
        if choice_question == 1:
            print('How long can a person go without food?')
            print('A: 8 to 21 Days.')
            print('B: 21 to 36 Days.')
            print('C: 36 to 45 Days.')
            answer_choice = input('A, B, or C? ').lower().strip()
            if answer_choice == 'a':
                print('''Correct!
                You recieve: 10 scrap''')
                choice_question += 1
                reward = 10
                return reward
                break
            elif answer_choice == 'b':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'c':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            else:
                print('Invalid Input')
                input()

        # Who invented nuclear bomb
        elif choice_question == 2:
            print('Who invented the nuclear bomb')
            print('A: Lea Szilard.')
            print('B: J. Robert Oppenheimer.')
            print('C: Cillian Murphy.')
            answer_choice = input('A, B, or C? ').lower().strip()
            if answer_choice == 'a':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'b':
                print('''Correct
                You recieve: 5 scrap''')
                choice_question += 1
                reward = 5
                return reward
                break
            elif answer_choice == 'c':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            else:
                print('Invalid Input')
                input()

        # mafths
        elif choice_question == 3:
            print('The radiation level in a certain area dubbles every hour.')
            print('If the radiation level is initially at 10 millisieverts per hour (mSv/h),')
            print('what will be the radiation level after 3 hours?')
            print('A: 30 millisieverts per hour (mSv/h)')
            print('B: 40 millisieverts per hour (mSv/h)')
            print('C: 60 millisieverts per hour (mSv/h)')
            print('D: 80 millisieverts per hour (mSv/h)')
            answer_choice = input ('A, B, C, or D? ').lower().strip()
            if answer_choice == 'a':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'b':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'c':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'd':
                print('''Correct
                You recieve: 10 scrap''')
                choice_question += 1
                reward = 10
                return reward
                break
            else:
                print('Invalid Input')
                input()


        # how much radiation?
        elif choice_question == 4:
            print('What is the minimum amout of radiation that will kill you?')
            print('A: A dose of 100 mSv. (millisievert)')
            print('B: A dose of 1000 mSv. (millisievert)')
            print('C: A dose of 10000 mSv. (millisievert)')
            answer_choice = input ('A, B, or C? ').lower().strip()
            if answer_choice == 'a':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'b':
                print('''Correct
                You recieve: 15 scrap''')
                choice_question += 1
                reward = 15
                return reward
                break
            elif answer_choice == 'c':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            else:
                print('Invalid Input')
                input()



        # What is the reccomended material for shielnidn against radiation exposure
        elif choice_question == 5:
            print('What is the recommended material for shielding agains radiation exposure?')
            print('A: Lead.')
            print('B: Aluminium.')
            print('C: Steel.')
            answer_choice = input ('A, B, or C? ').lower().strip()
            if answer_choice == 'a':
                print('''Correct
                You recieve: 10 scrap''')
                choice_question += 1
                reward = 10
                return reward
                break
            elif answer_choice == 'b':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'c':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            else:
                print('Invalid Input')
                input()


        #what is not a symptom id acute radiation
        elif choice_question == 6:
            print('What is not a symptom of acute Radiation Sickness?')
            print('A: Hairloss.')
            print('B: Nausea and Vomiting.')
            print('C: Blindness.')
            answer_choice = input ('A, B, or C? ').lower().strip()
            if answer_choice == 'a':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'b':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'c':
                print('''Correct
                You recieve: 5 scrap''')
                choice_question += 1
                reward = 5
                return reward
                break
            else:
                print('Invalid Input')
                input()



        #what type of clothing provides better protecton agains radiation
        elif choice_question == 7:
            print('What type of clothing provides the best protection agains radiation?')
            print('A: Thick Wool.')
            print('B: Synthetic Fibers.')
            print('C: Lead-Lined Suits.')
            answer_choice = input ('A, B, or C? ').lower().strip()
            if answer_choice == 'a':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'b':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'c':
                print('''Correct
                You recieve: 10 scrap''')
                choice_question += 1
                reward = 10
                return reward
                break
            else:
                print('Invalid Input')
                input()


        #which food item is generaly considers safer to consume during a radiation emergency
        elif choice_question == 8:
            print('A: Fresh Produce.')
            print('B: Canned Goods.')
            print('C: Wild Game.')
            answer_choice = input ('A, B, or C? ').lower().strip()
            if answer_choice == 'a':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'b':
                print('''Correct
                You recieve: 10 scrap''')
                choice_question += 1
                reward = 10
                return reward
                break
            elif answer_choice == 'c':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            else:
                print('Invalid Input')
                input()


        # which factor contributes to the spread of radiation contamination
        elif choice_question == 9:
            print('A: Wind Direction.')
            print('B: Humidity Level.')
            print('C: Lunar Phase.')
            answer_choice = input ('A, B, or C? ').lower().strip()
            if answer_choice == 'a':
                print('''Correct
                You recieve: 10 scrap''')
                choice_question += 1
                reward = 10
                return reward
                break
            elif answer_choice == 'b':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'c':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            else:
                print('Invalid Input')
                input()


        #what type od water source is asafer to consume in a radiated area
        elif choice_question == 10:
            print('A: Running Water.')
            print('B: Rainwater collected in Barrels')
            print('C: Water in Standing Ponds.')
            answer_choice = input ('A, B, or C? ').lower().strip()
            if answer_choice == 'a':
                print('''Correct
                You recieve: 10 scrap''')
                choice_question += 1
                reward = 10
                return reward
                break
            elif answer_choice == 'b':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            elif answer_choice == 'c':
                print('Incorrect')
                choice_question += 1
                reward = 0
                return reward
                break
            else:
                print('Invalid Input')
                input()

