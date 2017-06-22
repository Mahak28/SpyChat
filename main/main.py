from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored

#Strings to generate alerts
STATUS_MESSAGES = ['High on life,Low on sleep', 'At Work', 'Urgent Calls Only']
SPECIAL_KEYWORDS = ['HELP ME','SAVE ME','TROUBLE','URGENT']
print colored("Hello! Let's get started", 'green','on_grey')

question="do you want to continue as " + spy.salutation + " " + spy.name + "(Y/N)?"
existing=raw_input(question)

def count_words(word):
    word.split()
    length= len(word.split())
    return length

#method to remove a friend
def remove_friend(pos):
    del friends[pos]
    print 'spy has been removed'

#method defination to add or choose from the previous status
def add_status():
    current_status_message= None

    if current_status_message != None:
        print 'your current status is %s \n' % (current_status_message)
    else:
        print'You dont have any status currently \n'

    default = raw_input("do you want to select from older status(y/n)?")

    if default.upper() == "N":
        new_status_message= raw_input("what status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
           print '%d. %s' % (item_position,message)
           item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages"))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print'The option you chose is not valid! press either y or n.'

    if updated_status_message:
        print 'your updated status message is: %s' %  (updated_status_message)
    else:
        print'your current status dont have a status update'

    return updated_status_message

#method to add a friend
def add_friend():

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("please add your friend's name: ")
    new_friend.salutation = raw_input("are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print colored('Friend Added!', 'blue','on_grey')
    else:
        print "Sorry! Invalid Entry.We cant add spy with the details you provided"

    return len(friends)

def select_friends():
    item_number= 0

    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend.name, friend.age,friend.rating)

        item_number= item_number + 1

    friend_choice = raw_input("choose from your friends")
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position


def send_message():
    friend_choice = select_friends()
    print friend_choice

    input_image = raw_input("What is the name of the image?")
    output_path = 'secret.jpg'
    text = raw_input("What message do you want to give?")
    Steganography.encode(input_image, output_path, text)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print colored("Your secret message image is ready!", 'red', 'on_cyan')

#method to select friend from the list and decode the message
def read_message():

    sender = select_friends()
    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

#Generate a spy alert if special text is encountered
    if secret_text.upper() in SPECIAL_KEYWORDS:
        print colored("SPY ALERT! SPY ALERT! SPECIAL MESSAGE IS GENERATED " + secret_text, 'red', 'on_grey')

    number= count_words(secret_text)

    if number >10:
            remove_friend(sender)
    else:
            print secret_text
            new_chat = ChatMessage(secret_text,False)

            friends[sender].chats.append(new_chat)

            print "Your secret message has been saved!" + secret_text

#method to read the chat history
def read_chat_history():
        read_for = select_friends()
        print '\n'

        for chat in friends[read_for].chats:
            if chat.sent_by_me:
                print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'you said:', chat.message)
            else:
                print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name

    if spy.age > 15 and spy.age < 50:

        print"Authentication complete. Welcome " + spy.name  + "age:"  + str(spy.age) + "and rating of: " + str(spy.rating) + "proud to have you on board "

        show_menu= True

        while show_menu:
            menu_choices = "What operation do you want to perform? \n 1.Add a status update \n 2. Add a friend \n 3. Select a friend \n 4. Send a secret message \n 5.read a secret message \n 6. Read chats from user \n 7.Remove a friend \n 8.close application \n "
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice= int(menu_choice)


                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print'you have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    select_friends()
                elif menu_choice == 4:
                    send_message()
                elif menu_choice ==5:
                    read_message()
                elif menu_choice == 6:
                    read_chat_history()
                elif menu_choice == 7:
                    number= select_friends()
                    remove_friend(number)

                else:
                    show_menu = False
    else:
        print'Sorry you are not of the correct age to spy'

if existing == 'Y':
    start_chat(spy)
else:

    spy = Spy('','',0,0.0)
    spy.name = raw_input("welcome to spy chat,tell your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("should i call you Mr. or Ms,?: ")

        spy.age = raw_input("what is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("what is your spy rating? ")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print'you need to add a valid spy name'






