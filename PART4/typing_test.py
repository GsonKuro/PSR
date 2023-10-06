#!/usr/bin/env python3

import random
import argparse
from readchar import readkey  

list_words = ["Abduzir", "Belicoso", "Cominar", "Dissentir", "Engodar", "Fugaz", "Homizio", "Ígneo", "Jaez", "Lauto"]

def arguments():
    """

    """

    # Define variable to process commands
    parser = argparse.ArgumentParser(description='Menu of typing game')
    # Add argument to choose max time to evaluate 
    parser.add_argument('-mt', '--max_time', type=int, help='Max time.', required=True)
    # Add argument to choose max number of inputs 
    parser.add_argument('-mni', '--max_number_inputs', type=int, help='Max number of inputs', required=True)
    # Add argument to choose the type of typing game
    parser.add_argument('-md', '--mode', type=str, choices=['characters', 'words'], help='Type of typing test', required=True)

    # Create a dictionary
    args = vars(parser.parse_args())

    # Print the time that the game will take to end, the number of inputs to finish the task and the mode of the typing test
    print("Starting game of typing test\nMode: " + args['mode'] + 
          "\nDuration: " + str(args['max_time']) + " s" +
          "\nNumber of inputs: " + str(args["max_number_inputs"]))
    
    print("Press any key to start the typing test...")
    wait_key = readkey()
    
    if(args['mode'] == 'characters'):
        mod_char(args['max_number_inputs'])
    else:
        mod_word(args['max_number_inputs']) 

    
def mod_char(num_inputs):
    """

    """
    for i in range(0, num_inputs):
        temp_char = random.randint(97, 122)
        print(chr(temp_char))
        compare_key = readkey()
        print(compare_key)

def mod_word(num_inputs):
    """

    """
    compare_word = ""
    count = 0

    while(True):
        temp_word = random.choice(list_words)
        print(temp_word)

        while (True):
            compare_word += readkey()

            if(len(compare_word) == len(temp_word)):
                print(compare_word)
                compare_word = ""
                count += 1
                break

        if count == num_inputs:
            break

def main():
    arguments()

if __name__ == "__main__":
    main()