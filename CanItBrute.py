# Copyright (c) 2021 Azhaan Salam
# Licensed under the MIT License

from time import time, sleep
from sys import argv
from string import ascii_letters, digits, punctuation
from itertools import product
def main():
    print("Welcome to CanItBrute! Run with a command-line argument to see the different combinations being tried!")
    password = input("Password: ")
    while password == "":
        print("Please enter a password!")
        password = input("Password: ")
    length = 0
    results = False
    printable = False
    if len(argv) == 2:
        printable = True
    timestart = time()
    while results == False:
        length += 1
        print(f"Trying passwords with the length of {length}")
        results = crackpass(password, length, printable)
    timeend = time()
    elapsed = timeend - timestart
    print(f"Your password was cracked! It took {elapsed} seconds to crack your password. But, that doesn't mean it's not secure!")
    print(f"Most brute-force algorithms, like this one, can crack any password with enough time.")
    print("Though, keep in mind, keep your passwords more than 6 characters, and have at least one character that is not an alphabetical character.")
    print(f"Run with any command-line argument to see what permutations of passcodes are being guessed!")


def crackpass(password, length, printable):
    # Credits to https://github.com/dmalan/cybersecurity/blob/master/crack4.py
    for passcode in product(ascii_letters + digits + punctuation, repeat=length):
        if printable:
            print("".join(passcode))    
        if "".join(passcode) == password:
            return True
    return False        


if __name__ == "__main__":
    main()
