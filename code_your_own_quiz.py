intro = '''This quiz is a project from: 
|* * * * * * * * * * * * * * * * * * * *|
|* * * * * * *  UDACITY  * * * * * * * *|
|*   Nanodegree Intro to Programming   *|
|* * * *   Create your own quiz  * * * *|
|* * * * * * * * * * * * * * * * * * * *|
'''

# All the main variables are here.
questions = ['__1__', '__2__', '__3__', '__4__', '__5__', '__6__', '__7__', '__8__', '__9__', '__10__']
# All string variables are in one line so the rest of code is easier to read.
easy = 'A common first thing to do in a language is display: \n\'Hello __1__!\' In __2__ this is particularly easy; all you have to do is type in: __3__ "Hello __1__!" Of course, that isn\'t a very useful thing to do. However, it is an example of how to output to the user using the __3__ command, and produces a program which does something, so it is useful in that capacity. It may seem a bit odd to do something in a Turing complete language that can be done even more easily with an __4__ file in a browser,but it\'s a step in learning __2__ syntax, and that\'s really its purpose.'
easy_answers = ['world', 'Python', 'print', 'HTML']
medium = 'A __1__ is created with the def keyword.  You specify the inputs a __1__ takes by adding\n__2__ separated by commas between the parentheses. __1__s by default returns __3__ if you don\'t specify the value to return.\n__2__ can be standard data types such as string, integer, dictionary, tuple, and __4__ or can be more complicated\nsuch as objects and lambda functions.'
medium_answers = ['function', 'arguments', 'None', 'list']
hard = 'When you create a __1__, certain __2__s are automatically generated for you if you don\'t make them manually.\nThese contain multiple underscores before and after the word defining them. When you write a __1__,\nyou almost always include at least the __3__ __2__, defining variables for when __4__s of the __1__ get made.\nAdditionally, you generally want to create a __5__ __2__, which will allow a string representation of the method\nto be viewed by other developers.\n\nYou can also create binary operators, like __6__ and __7__, which allow + and - to be used by __4__s of the __1__.\nSimilarly, __8__, __9__, and __10__ allow __4__s of the __1__ to be compared (with <, >, and ==).'
# I admit...... I had to google most of them, they were way to hard for what I know about Python so far. Spend quite a lot of time finding them
hard_answers = ['class', 'method', '__init__', 'instance', '__repr__', '__add__', '__sub__', '__lt__', '__gt__', '__eq__']

#This function checks for questions in the string and it is implemented in the main function
def questions_in_string(word, questions):
    for q in questions:
        if q in word:
            return q
    return None

#This function is the core of the quiz, telling how many attemts user have per question, 
#starting a loop to check the questions, having inline function(check bellow)
#posting a wining message and prompting a user to try again with different difficulty
def quiz(string, questions, answer):
    print 'You have 3 tries per question!\n\n'
    print string
    string = string.split()
    tries = 3
    for word in string:
        replacement = questions_in_string(word, questions)
        
    # An inline function that checks the answer and how many attempts the user has done
    # and prompting user to try again if they lost the game.
        def engine(tries):
            if replacement != None:
                user_input = raw_input('\nWhat should be substituted in for ' + replacement +'? ')
                if user_input == answer[questions.index(replacement)]:
                    for word in string:
                        string[string.index(word)] = word.replace(replacement, user_input)
                    new_string = ' '.join(string)
                    print new_string
                else:
                    tries -= 1
                    if tries > 0:
                        print 'Wrong answer. You have ' + str(tries) + ' tries remaining!\nWatch out for uppercase and lowercase letters!'
                        return engine(tries)
                    else:
                        restart_question = raw_input('You are out of the attemts. Restart?')
                        if restart_question == 'yes' or restart_question == 'y':
                            return intro_selection()
                        else:
                            quit()
        engine(tries)
    # Winn
    print '* * * * * * * * * * * * * * * * * *\n* * * * * *  You won!!  * * * * * *\n* * * * * * * * * * * * * * * * * *'
    restart_question = raw_input('Want to try again with another difficulty?')
    if restart_question == 'yes' or restart_question == 'y':
        return intro_selection()
    else:
        quit()

# THe quiz crust that allows users to see the content.
def intro_selection():
    print '\nThis quiz text is a copy from a sample Udacity quiz.\n To play, just type the answer. If the answer is correct, \n You\'ll see the brackets will be replaced with answers.\n'
    print 'Please select a game difficulty by typing it in!\n'
    select_difficulty = raw_input("Possible choices include easy, medium, and hard: ")
    if select_difficulty == 'easy' or  select_difficulty == 'e':
        print 'You selected EASY difficulty.\n'
        return quiz(easy, questions, easy_answers)
    elif select_difficulty == 'medium' or select_difficulty == 'm':
        print 'You selected MEDIUM difficulty!\n'
        return quiz(medium, questions, medium_answers)
    elif select_difficulty == 'hard' or  select_difficulty == 'h':
        print 'This is a HARD difficulty!\n\n'
        hard_yes_no = raw_input('Are you sure you want to continue?')
        if hard_yes_no == 'yes' or hard_yes_no == 'y':
            print '\nRight on!\n'
            return quiz(hard, questions, hard_answers)
        else:
            return intro_selection()
    elif select_difficulty == 'exit' or select_difficulty == 'quit':
        quit()
    else:
        print 'Not an option. You can use \'e\',\'m\',\'h\' as an alternative choice.\n'
        intro_selection()    

print intro
intro_selection()