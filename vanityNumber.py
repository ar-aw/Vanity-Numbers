"""
name: arika awan
date: nov 16
desc: convert text into a vanity number
"""

#create a dictionary for all the letters and their corresponding numbers
def transNum(string):
    num = 1
    numDict={
        "a":2,"b":2,"c":2,
        "d":3,"e":3,"f":3,
        "g":4,"h":4,"i":4,
        "j":5,"k":5,"l":5,
        "m":6,"n":6,"o":6,
        "p":7,"q":7,"r":7,"s":7,
        "t":8,"u":8,"v":8,
        "w":9,"x":9,"y":9,"z":9,
    }
    #read through given string and assign each letter a number
    for ch in string:
        num = numDict[ch.lower()]
    return num

def translate(phrase1, phrase2):
    
    #declare variable vanNum1, or the first part of the phrase
    vanNum1 = ""
    for ch in phrase1:
        if ch.lower() in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
            vanNum1 = vanNum1 + str(transNum(ch))
        else:
            vanNum1 = vanNum1 + ch
            
    #declare variable vanNum2, or the second part of the phrase
    vanNum2= ""
    for ch in phrase2:
        if ch.lower() in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
            vanNum2 = vanNum2 + str(transNum(ch))
        else:
            vanNum2 = vanNum2 + ch
    return (f"{vanNum1}-{vanNum2}")

#main function
def main():
    phrase1 = input("enter the first 3 characters of the vanity number: ")[:3]
    
    while (len(phrase1)< 3):
        phrase1 = input("that's too short, enter 3 characters please: ")[:3]
        
    phrase2 = input("enter the last 4 characters of the vanity number: ")[:4]
    
    while (len(phrase2)< 4):
        phrase2 = input("that's too short, enter 4 characters please: ")[:4]
        
    vanNum = translate(phrase1, phrase2)
    print(f"Dial {vanNum} to call {phrase1} {phrase2}.")

#call main function
main()