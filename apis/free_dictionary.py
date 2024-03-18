import requests
import sys
import json

def main():
    print(get_user_word())
    ...

def get_user_word():
    while True:
        try:
            word = input("Which word's meaning would you like to know? ")
            if not word.isalpha():
                print("Please enter a valid word")
                continue
            return word
        except:
            ...

if __name__ == "__main__":
    main()