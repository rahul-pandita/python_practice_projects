def main():
    # words = input("Enter list")
    print(comma([]))

def comma(lst):
    sentence = ""
    for word in lst:
        if len(lst) == 0:
            return "Empty"
        elif len(lst) != 0 and lst.index(word) != -1:
            sentence += f"{word}, "
            # return sentence
        else:
            sentence += f"and {word}"
            # return sentence
    
    return sentence

if __name__ == "__main__":
    main()
