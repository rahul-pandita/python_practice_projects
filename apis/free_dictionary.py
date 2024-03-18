import requests
import sys
import json

def main():
    get_definitions(get_user_word())
    ...

def get_user_word():
    while True:
        word = input("Which word's meaning would you like to know? ")
        if not word.isalpha():
            print("Please enter a valid word")
            continue
        return word

def get_definitions(word):
    response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word).json()
    
    print("Our database has the following definitions for your word:")
    for count, defintion in enumerate(response[0]["meanings"][0]["definitions"]):
        print(f"Definition {count + 1}:", defintion["definition"])


if __name__ == "__main__":
    main()