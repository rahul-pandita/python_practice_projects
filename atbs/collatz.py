def main():
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Please enter an integer.")
    
    

def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3*num + 1

if __name__ == "__main__":
    main()