import pandas as pd
import re
import random
import hang

def select():
    words = pd.read_csv(r'C:\Aswin\Projects\Hangman\words.csv')
    #print(words)
    length = len(words)
    #print(words.iloc[0])
    """for i in range(length):
        res = "".join(re.findall("[a-zA-Z]+",words["Words"][i]))
        words.iloc[i] = res
    """
    #words.to_csv(r'C:\Users\aswin\Downloads\words.csv',index=False)
    #words = pd.read_csv(r'C:\Users\aswin\Downloads\words.csv')
    #print(words)

    rand_ind = random.randint(0,length)
    selected_word = words["Words"][rand_ind]
    x = list(selected_word)
    length_str = len(selected_word)
    for j in range(0,length_str):
        if(j%2==0):
            x[j] = "_"
    print(selected_word)
    x = "".join(x)
    print(x,"\n")
    tries = 6
    print("Choose any of the below option:","1. Select the dash and enter the letter","2. Enter the entire word",sep="\n")
    print()
    while True:
        try:
            option = int(input("Please enter an integer: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")
    L=[]        
    while(tries!=0):
        if(option==1):
            print()
            while True:
                try:
                    dash = int(input("Enter dash number: "))
                    if((dash*2)>length_str+2 or dash<=0):
                        print("Entered value exceeds the specified limit.\n")
                    elif(dash in L):
                        print("You've already guessed that letter. Try a different one.\n")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.\n")

            pos = (dash*2)-2
            letter = str(input("Guess a letter: "))
            if(letter==selected_word[pos]):
                L.append(dash)
                x = list(x)
                x[pos] = letter
                x = "".join(x)
                print("Updated word: ",x)
                if(x==selected_word):
                    print("\nCongratulations! You guessed the word: ",selected_word)
                    
            else:
                tries-=1
                print("Incorrect guess. Attempts left: ",tries)
                hang.hang(tries)

        if(option==2):
            print()
            word = str(input("Enter the entire word: "))
            if(word==selected_word):
                print("\nCongratulations! You guessed the word: ",selected_word)
                tries = 0
            else:
                tries-=1
                print("Incorrect guess. Attempts left: ",tries)
                hang.hang(tries)
            




