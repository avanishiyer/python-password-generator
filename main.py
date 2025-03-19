import random
import string
import time
import os
from random import sample


# function to generate a secure password
def generate_password():
    password = None

    fairness_words = ["equality", "equity", "access", "justice", "opportunity"]

    development_words = ["growth", "progress", "sustainability", "empowerment", "inclusion"]

    symbols = string.punctuation

    numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    meanings = {"equality": "the state of being equal, especially in status, rights, or opportunities",
                "equity": "the quality of being fair and impartial",
                "access": "the opportunity or right to use something",
                "justice": "the quality of being fair and reasonable",
                "opportunity": "a set of circumstances that makes it possible to do something"}

    # Keep generating passwords until a valid password is found
    while not password:
        word1 = random.choice(fairness_words)
        word2 = random.choice(development_words)
        symbol = random.choice(symbols)
        number = random.choice(list(numbers))
        word, meaning = random.choice(list(meanings.items()))

        password = word1 + word2 + symbol + str(number) + word.capitalize()[:3]

        if not (len(password) >= 10 and any(i.isdigit() for i in password) and any(i.isupper() for i in password)):
            password = None
    
    return password

# jumbling the password then outputting based on strenght
def jumble(password, strength):
    test_list = [password, ]
    res = [''.join(sample(ele, len(ele))) for ele in test_list]

    final = res[0]

    return final[:strength+5]

# main
while __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')


    # strenght
    while True:
        try:
            strenght = int(input("Enter strength of password between 1 - 10: "))

        except ValueError:
            input("Invalid input\n\n")

        else:
            if strenght <= 0 or strenght > 10:
                input("Invalid strenght\n\n")

            else: 
                break

    # number of password to generate
    while True:
        try:
            quantity = int(input("Enter amount of passwords to be generated: "))

        except ValueError:
            input("Invalid Input\n\n")

        else:
            if quantity <= 0:
                input("Invalid amountr\n\n")

            elif quantity > 20:
                input("Too many passwords requested\n\n")

            else:
                break
    
    os.system('cls' if os.name == 'nt' else 'clear')

    # just as a middle thing
    print(f"Generating {quantity} passwords with the strength of {strenght}...\n")
    time.sleep(1)

    # generating and printing the passwords
    n = 1
    while n <= quantity:
        password = generate_password()
        password = jumble(password, strenght)

        print(f"Password {n}: {password}")

        n += 1
    
    print("\n")

    # quotes
    message = ["This password reflects the importance of fairness and development in protecting your personal information and ensuring a secure online environment for all.",
                "Remember, it's important to use unique and strong passwords for each of your accounts to keep your personal information safe.",
                "You can also use password managers to generate and store strong passwords for you.",
                "Additionally, be cautious of phishing scams and never share your passwords with anyone.",
                "Stay safe online!"
                "Don't reuse passwords across multiple accounts, as this can make it easier for hackers to gain access to all of your online accounts."
                "Be cautious of unsolicited emails and messages that ask for your personal information or login credentials."
                "Consider using a password manager to help you generate and securely store unique, strong passwords for each of your accounts."]

    print(random.choice(message))
    
    input()

