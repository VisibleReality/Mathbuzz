##    '''
##    Purpose is to provide kids with basic arithmetic practice.
##    
##    Program has been developed in easy stages and, eventually,
##      be made available on awmitchell.com.
##
##    Potential features include the following:
##      * Make the application a function so that it can be run from the python console(?)
##      * options for practice method [how many completed within time, or time to complete set number]
##      * user profiles for preferences and to track progress
##      * Overwrite questions so that students can't look it up.
##      * Results printing shows the questions and answers they got wrong.
##      * Stop the repetition of questions
##
##    Getting this on awmitchell.com is a whole other learning experience which will take some time.
##    The first step is that the program needs to input and output HTML pages and accept input via an HTML form.
##    And then there's CSS and templates and JavaScript to learn about.
##    '''
# import math # do we need this module loaded? Answer: No.
import random
import datetime
from datetime import timedelta

## print python 3 required message
print('Python 3.x is required to run this copy of Mathbuzz. \nIf this is run using Python 2.x, it will cause the program to crash. \nIf it crashes, please run the 2.x version instead')

## print welcome message
version = 2.03
def mathbuzz():
    print('')
    print('')
    print('Welcome to . . . . .')
    print('')
    print('_____________________________________________')
    print('')
    print('   _  _ ____ ___ _  _ ___  _  _ ___  ___  ')
    print('   |\\/| |__|  |  |__| |__] |  |   /    /  ')
    print('   |  | |  |  |  |  | |__] |__|  /__  /__ ')
    print('')
    print('              By VisibleReality              ')
    print('_____________________________________________')
    print('')
    print('Version ' + str(version))

    p_input = None
    rangeup = None

    ## loop until player is done
    player_done = False
    while not player_done:

        ## Initialise some variables. (Helps with recording data)
        p_input = None
        rangeup = None
        
        ## how many questions?
        good_answer = False
        while not good_answer:
            str_answer = input("How many questions would you like (10 is minimum)?   ")
            str_answer = str_answer.strip()
            if str_answer.isdigit() == True and int(str_answer) >= 10: 
                num_questions = int(str_answer)
                good_answer = True
            else:
                print('')
                print("Please try again...")
        ## what does the user want to practice?
        good_answer = False
        while not good_answer:
            qn_type = input("What type of questions would you like?\n    +   for addition\n    -   for subtraction\n    /   for division\n    x   for multiplication\n    t   for times tables, or\n    r   for random            -->   ").lower()
            qn_type = qn_type.strip()
            qn_type = qn_type[0]
            if qn_type == ("+" or  "-" or  "x" or  "*" or  "/" or  "\\" or  "t" or  "r"):
                good_answer = True
            else:
                print('')
                print("Please try again...")
        ## which times tables?
        good_answer = False
        if qn_type == "t":
            while not good_answer:
                str_answer = input("Which times table you would like to pratice (2 is minimum)?   ")
                str_answer = str_answer.strip()
                if str_answer.isdigit() == True and int(str_answer) >= 2: 
                    p_input = int(str_answer)
                    rangeup = 13
                    good_answer = True
                else:
                    print('')
                    print("Please try again...")
        ## what's the range of practice? (if not times tables)
        else:
            while not good_answer:
                str_answer = input("What would you like the upper limit to be (5 is minimum)?   ")
                str_answer = str_answer.strip()
                if str_answer.isdigit() == True and int(str_answer) >= 5: 
                    rangeup = int(str_answer) + 1
                    good_answer = True
                else:
                    print('')
                    print("Please try again...")

        # initialise variables
        qn_type_r = 0
        questions = []
        ans_input = []
        ans_correct = []
        results = []
        i = 0
        qn = 0
        oldarg1 = None
        oldarg2 = None

        ## set up random questions and answers of the right type
        if qn_type != 'r':
            while qn < num_questions:
                arg1 = random.randrange(1, rangeup)
                arg2 = random.randrange(1, rangeup)
                while (arg1 == oldarg1 and arg2 == oldarg2) or (arg1 == oldarg2 and arg2 == oldarg1):
                    arg1 = random.randrange(1, rangeup)
                    arg2 = random.randrange(1, rangeup)
                oldarg1 = arg1
                oldarg2 = arg2
                if qn_type == "+":
                    questions = questions + ["Q" + str(qn + 1) + "\t" + str(arg1) + " + " + str(arg2)]
                    ans_correct = ans_correct + [arg1 + arg2]
                elif qn_type == "x" or qn_type == "*":
                    questions = questions + ["Q" + str(qn + 1) + "\t" + str(arg1) + " x " + str(arg2)]
                    ans_correct = ans_correct + [arg1 * arg2]
                elif qn_type == "-":
                    if arg1 < arg2:
                        temp = arg1
                        arg1 = arg2
                        arg2 = temp
                    questions = questions + ["Q" + str(qn + 1) + "\t" + str(arg1) + " - " + str(arg2)]
                    ans_correct = ans_correct + [arg1 - arg2]
                elif qn_type == "/" or qn_type == "\\":
                    if arg1 < arg2:
                        temp = arg1
                        arg1 = arg2
                        arg2 = temp
                    arg1 = arg1 - arg1 % arg2
                    questions = questions + ["Q" + str(qn + 1) + "\t" + str(arg1) + " / " + str(arg2)]
                    ans_correct = ans_correct + [arg1 // arg2]
                elif qn_type == "t":
                    questions = questions + ["Q" + str(qn + 1) + "\t" + str(arg1) + " x " + str(p_input)]
                    ans_correct = ans_correct + [arg1 * p_input]
                qn = qn + 1
        elif qn_type == "r":
            while qn < num_questions:
                arg1 = random.randrange(1, rangeup)
                arg2 = random.randrange(1, rangeup)
                qn_type_r = random.randrange(0, 4)  ## 0 = +, 1 = * , 2 = -, 3 = /
                if qn_type_r == 0:
                    questions = questions + ["Q" + str(qn + 1) + "\t" + str(arg1) + " + " + str(arg2)]
                    ans_correct = ans_correct + [arg1 + arg2]
                elif qn_type_r == 1:
                    questions = questions + ["Q" + str(qn + 1) + "\t" + str(arg1) + " x " + str(arg2)]
                    ans_correct = ans_correct + [arg1 * arg2]
                elif qn_type_r == 2:
                    if arg1 < arg2:
                        temp = arg1
                        arg1 = arg2
                        arg2 = temp
                    questions = questions + ["Q" + str(qn + 1) + "\t" + str(arg1) + " - " + str(arg2)]
                    ans_correct = ans_correct + [arg1 - arg2]
                elif qn_type_r == 3:
                    if arg1 < arg2:
                        temp = arg1
                        arg1 = arg2
                        arg2 = temp
                    arg1 = arg1 - arg1 % arg2
                    questions = questions + ["Q" + str(qn + 1) + "\t" + str(arg1) + " / " + str(arg2)]
                    ans_correct = ans_correct + [arg1 // arg2]
                qn = qn + 1

        ## ask questions, accept input and create results
        print('')
        start_time = datetime.datetime.now()
        while i < len(questions):
            good_answer = False
            while not good_answer:
                str_answer = input(questions[i] + " = ")
                str_answer = str_answer.strip()
                if str_answer.isdigit() == True: 
                    ans_input = ans_input + [int(str_answer)]
                    good_answer = True
                else:
                    print("Please try again...")
            results = results + [ans_input[i] == ans_correct[i]]
            i = i + 1

        ## output results - questions incorrect, results and time taken
        end_time = datetime.datetime.now()
        timetaken = end_time - start_time
        print("Incorrect answers as follows:")
        i = 0
        while i < len (questions):
            if not results[i]:
                print("\t" + questions[i] + " = " + str(ans_correct[i]) + "\tyou answered " + str(ans_input[i]))
            i = i + 1
        print("Summary: " + str(results.count(True)) + " out of " + str(len(results)) + ", " + str((results.count(True) * 100) / len(results)) + "%")
        print("Time taken: " + timetaken)
        if qn_type == "+": qn_word = "Addition"
        elif qn_type == "-": qn_word = "Subtraction"
        elif qn_type == "x" or qn_type == "*": qn_word = "Multiplication"
        elif qn_type == "/" or qn_type == "\\": qn_word = "Division"
        elif qn_type == "t": qn_word = "Times Tables"
        elif qn_type == "r": qn_word = "Random"
        else: qn_word = "Unknown"
        timetaken = timetaken.total_seconds()
        record = str(datetime.date.today()) + "," + str(num_questions) + "," + qn_word + "," + str(rangeup) + "," + str(p_input) + "," + str((results.count(True) * 100) / len(results)) + "%" + "," + str(timetaken) + "," + str(version) + "\n"
        recordtofile = input("Would you like to record these results in MathbuzzResults.csv? (Y/N)   ")
        recordtofile = recordtofile.strip()
        if recordtofile == "Y" or recordtofile == 'y':
            file = open("MathbuzzResults.csv", "a")
            file.close()
            file = open("Mathbuzzresults.csv", "r")
            if file.read(8) == '':
                file.close()
                file = open("MathbuzzResults.csv", "w")
                file.write('Date,Number of Questions,Type,Upper Limit,Times Table,Percentage Correct,Time Taken (seconds),Mathbuzz Version\n')
                file.close()
            else: file.close()
            file = open("MathbuzzResults.csv", "a")
            file.write(record)
            file.close()
            print("These results have been recorded. You can find MathbuzzResults.csv in the same folder as Mathbuzz itself.")
        else: print("The results have not been recorded")
        ## play again
        print('')
        play_again = ''
        while play_again == '':
            play_again = input("Would you like to play again? (Y/N)   ")
            play_again = play_again.strip()
            play_again = play_again.lower()
        print('')
        print('')
        player_done = play_again[0] == ('n' or 'q')

    ## finished playing
    print('')
    print('')
    print('        T H A N K S   for   playing!')
    print('')
    print('')
    print('_____________________________________________')
    print('')
    print('   _  _ ____ ___ _  _ ___  _  _ ___  ___  ')
    print('   |\\/| |__|  |  |__| |__] |  |   /    /  ')
    print('   |  | |  |  |  |  | |__] |__|  /__  /__ ')
    print('')
    print('              By VisibleReality              ')
    print('_____________________________________________')
    print('')
    print('')
    print('')
    print('        T H A N K S   for   playing!')
    print('')
    print('')
    input("Press enter to exit... (You can relaunch the game by calling mathbuzz())")
mathbuzz()
