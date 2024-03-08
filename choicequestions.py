# Multiple choice questions

def questions(number_question):
    choice_question = number_question
    print('''You land on a mulitple choice question tile.
    press enter to continue.''')
    input()
    while True:
        # How long no food
        if choice_question == 1:
            print('''How long can a person go without food?
            A: 8 to 21 Days.
            B: 21 to 36 Days.
            C: 36 to 45 Days.''')
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
            print('''Who invented the nuclear bomb?
            A: Lea Szilard.
            B: J. Robert Oppenheimer.
            C: Cillian Murphy.''')
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
            print('''The radiation level in a certain area dubbles every hour.')
            If the radiation level is initially at 10 millisieverts per hour (mSv/h),
            what will be the radiation level after 3 hours?
            A: 30 millisieverts per hour (mSv/h)
            B: 40 millisieverts per hour (mSv/h)
            C: 60 millisieverts per hour (mSv/h)
            D: 80 millisieverts per hour (mSv/h)''')
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
            print('''What is the minimum amout of radiation that will kill you?
            A: A dose of 100 mSv. (millisievert)
            B: A dose of 1000 mSv. (millisievert)
            C: A dose of 10000 mSv. (millisievert)''')
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
            print('''What is the recommended material for shielding agains radiation exposure?
            A: Lead.
            B: Aluminium.
            C: Steel.''')
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
            print('''What is not a symptom of acute Radiation Sickness?')
            A: Hairloss.
            B: Nausea and Vomiting.
            C: Blindness.''')
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
            print('''
            What type of clothing provides the best protection agains radiation?
            A: Thick Wool.
            B: Synthetic Fibers.
            C: Lead-Lined Suits.''')
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
            print('''
            Which food item is generaly considers safest to consume during a radiation emergency?
            A: Fresh Produce.
            B: Canned Goods.
            C: Wild Game.''')
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
            print('''
            Which factor contrubutes to the spread of radiation contamination?
            A: Wind Direction.
            B: Humidity Level.
            C: Lunar Phase. ''')
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
            print('''
            What type of water source is safest to consume in a radiated area?
            A: Running Water.
            B: Rainwater collected in Barrels
            C: Water in Standing Ponds.''')
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

        # which element is commonly used as fuel in nuclear reactors?
        elif choice_question == 11:
            print('''
            Which element is commonly used as fuel in nuclear reactors?
            A: Uranium
            B: Carbon
            C: Oxygen
            D: Hydrogen''')
            answer_choice = input ('A, B, C, or D? ').lower().strip()
            if answer_choice == 'a':
                print('''Correct
                You recieve 15 scrap.''')
                choice_question += 1
                reward = 15
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
                print('Incorrect')
                choice_question += 1
                return reward
                break
            else:
                print('Invalid Input')
                input()

        if choice_question == 11:
            choice_question = 0


