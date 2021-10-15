import pandas as pd
import random

def main():
    df = pd.read_csv('./Languages/norsk.csv')
    
    active = True
    choice = 0
    while active:
        menu()
        choice = int(input("Selection: "))
        if choice == 1:
            randomWord(df)
        elif choice == 2:
            translate(df)
        elif choice == 0:
            active = False
        else:
            # do nothing
            choice == 0


def menu():
    print("*************************")
    print("* Norwegian Flash Cards *")
    print("*                       *")
    print("*    Select a mode:     *")
    print("*                       *")
    print("*    1) Random Word     *")
    print("*    2) Translate       *")
    print("*                       *")
    print("*                       *")
    print("*    0) Exit            *")
    print("*                       *")
    print("*************************\n")
    
def randomWord(df):
    # first index is amount of words, second index is for language (0 = norsk, 1 = english)
    active = True
    while active:
        num = random.randint(0, 1995)
        print(f"Card number: {num}.")
        print(f"Norsk: {df.iloc[num,0]}")
        print(f"English: {df.iloc[num,1]}\n")
        choice = input("Press enter to continue, or type \"0\" to quit.\n\n")
        if(choice == '0'):
            active = False

def translate(df):
    active = True
    while active:
        num = random.randint(0, 1995)
        print(f"Translate {df.iloc[num,0]} to English, or type \"0\" to quit.\n")
        userStr = input()
        if(userStr == df.iloc[num,1]):
            print("Correct!\n")
        elif(userStr != df.iloc[num,1]):
            print(f"Incorrect. The correct translation was {df.iloc[num,1]}\n")
        if(userStr == '0'):
            active = False


if __name__ == "__main__":
    main()