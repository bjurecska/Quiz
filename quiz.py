import os

clear = lambda: os.system('cls')

#main data values

level1string =  """
The __1__ Wide Web ( abbreviated WWW or the Web ) is an information space where
documents and other web resources are identified by Uniform Resource Locators ( URLs ),
interlinked by __2__ links, and can be accessed via the Internet.
English scientist Tim Berners-Lee invented the World Wide Web in __3__ . He wrote
the first web browser computer program in 1990 while employed at __4__ in Switzerland.
The Web browser was released outside of CERN in 1991, first to other __5__
institutions starting in January 1991 and to the general public on the Internet in August 1991.
                """
level2string =  """
The World Wide Web has been central to the development of the Information Age
and is the primary tool __1__ of people use to interact on the Internet.
Web pages are primarily text documents formatted and annotated with
Hypertext Markup Language ( __2__ ). In addition to formatted text, web pages may
contain images, video, audio, and software components that are rendered in the
user's web browser as coherent pages of multimedia content. Embedded __3__
permit users to navigate between web pages. Multiple web pages with a common theme,
a common __4__ name, or both, make up a website. Website content can largely be
provided by the publisher, or interactive where users contribute content or the
content depends upon the user or their actions. Websites may be mostly informative,
primarily for entertainment, or largely for __5__ , governmental,
or non-governmental organisational purposes.
                """
level3string =  """
Hypertext Markup Language ( HTML ) is the standard markup language for creating
web pages and web applications. With __1__ __2__ Sheets ( CSS ) and __3__
it forms a triad of cornerstone __4__ for the World Wide Web. Web browsers
receive HTML documents from a webserver or from local storage and render them
into multimedia web pages. __5__ describes the structure of a web page semantically
and originally included cues for the appearance of the document.
                """

mystery_list = ["__1__", "__2__", "__3__", "__4__", "__5__"]
level1_key =    [["World", "world"], ["hypertext", "Hypertext"],
                ["1989"], ["CERN", "cern"], ["research", "Research"]]
level2_key =    [["billions", "Billions"], ["HTML", "html"],
                ["hyperlinks", "Hyperlinks"], ["domain", "Domain"],
                ["commercial", "Commercial"]]
level3_key =    [["Cascading", "cascading"], ["Style", "style"],
                ["Javascript", "javascript"], ["technologies", "Technologies"],
                ["HTML", "html"]]

def choose_difficulty():
    #choose what difficulty user wants
    difficulty = 0
    while difficulty == 0:
        user_choice = raw_input("Please select a difficulty:\nEasy, Normal or Nightmare \n")
        if user_choice in ["Easy", "easy"]:
            difficulty = 1
            print "\nYou have selected Easy.\n"
            lives = choose_lives(difficulty)
        elif user_choice in ["Normal", "normal"]:
            difficulty = 2
            print "\nYou have selected Normal.\n"
            lives = choose_lives(difficulty)
        elif user_choice in ["Nightmare", "nightmare"]:
            difficulty = 3
            print "\nYou have selected Nightmare.\n"
            lives = choose_lives(difficulty)
        else:
            print "Invalid choice."
    return difficulty, lives

def valid_entry(input_text):
    #checks if is a valid entry for lives
    correct_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if input_text in correct_input:
        return True
    else:
        return False

def choose_lives(difficulty):
    #choose how many lives a user wants. in nightmare it is auto 1.
    user_lives = 0
    while user_lives == 0:
        if difficulty == 1 or difficulty == 2:
            user_lives = raw_input("""Between 1 and 10 please select the number of lives you wish to have:\n""")
            if valid_entry(user_lives) == True:
                user_lives = int(user_lives)
                if user_lives == 1:
                    print "You have chosen " + str(user_lives) + " life.\n"
                else:
                    print "You have chosen " + str(user_lives) + " lives.\n"
                return user_lives
            else:
                print "Invalid choice"
                user_lives = 0
        else:
            print "As you are playing on Nightmare difficulty. You have only 1 life."
            user_lives = 1
            return user_lives

def user_answer(string_key, solution_number, lives):
    #ingame user input function
    result = False
    while result == False:
        answer = raw_input("\nPlease enter the solution to missing word number " + str(solution_number + 1) + ":")
        if answer in string_key[solution_number]:
            print "Correct\n"
            result = True
        else:
            print "Incorrect\n"
            lives -= 1
            if lives > 1:
                print "You have " + str(lives) + " lives left!\n"
            else:
                print "You have " + str(lives) + " life left!\n"
            if check_lives(lives) == False:
                return (False, lives)
    return (True, lives)

def process_new_lines(string):
    #to format the amended paragraph by adding in new lines
    length = 2 #to avoid adding a space after an 'a' or other 1 letter character (cosmetic)
    index = 0
    end_of_line = 90
    while (index + length) < len(string):
        if index == end_of_line:
            if string[index + length] != " " and string[index] == " ":
                string = string[:(index + 1)] + "\n" + string[(index + 1):]
                end_of_line += 90
            else:
                end_of_line += 1
        index += 1
    return string

def process_answer(split_list, word_replace, string_key, solution_number):
    #progresses the game by adding guessed words to their right place.
    result_list = []
    key_list = string_key[(solution_number - 1)]
    for word in split_list:
        if word == word_replace:
            word = word.replace(word, key_list[0])
            result_list.append(word)
        else:
            result_list.append(word)

    result_list = " ".join(result_list)
    result_list = process_new_lines(result_list)
    print result_list + "\n"
    result_list = result_list.split()
    return result_list

def check_lives(lives):
    #checks if a user is out of lives
    if lives == 0:
        return False
    return True

def another_game():
    #to play another game or not
    list_another_game = ["Yes", "yes", "Y", "y"]
    another_game = raw_input("Enter 'y' or 'yes' to play another game.\nOtherwise enter anything to quit:\n")
    if another_game in list_another_game:
        return True
    else:
        return False

def play_quiz(string_original, string_key, mystery_list, lives):
    #return win or lose
    string_replaced = []
    all_solutions_correct = 5
    solution_number = 0
    print string_original
    split_list = string_original.split()

    for word in split_list:
        if word in mystery_list:
            user_choice, lives = user_answer(string_key, solution_number, lives)
            if user_choice == True:
                solution_number += 1
                split_list = process_answer(split_list, word, string_key, solution_number)
                if solution_number == all_solutions_correct:
                    return True
            else:
                return False
        else:
                string_replaced.append(word)

def end_game(win_or_not):
    if win_or_not == True:
        print "You have won!\n"
    else:
        print "You lost!\n"
    return None


#main code is here
play_again = True
while play_again == True:
    clear()

    print   """
Hello, \n
Welcome to Quiz World. The point of the game is to guess the missing
word in the paragraphs. The missing words will be numbered and you will
have the chance to answer them in order. You will chose how many lives
you get on each difficulty, except on nightmare, where you will be limited
to 1 life only. \n
            """

    difficulty, lives = choose_difficulty()

    if difficulty == 1:
        win_or_not = play_quiz(level1string, level1_key, mystery_list, lives)
        end_game(win_or_not)
        play_again = another_game()
    elif difficulty == 2:
        win_or_not = play_quiz(level2string, level2_key, mystery_list, lives)
        end_game(win_or_not)
        play_again = another_game()
    else:
        win_or_not = play_quiz(level3string, level3_key, mystery_list, lives)
        end_game(win_or_not)
        play_again = another_game()
