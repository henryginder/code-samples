# Henry Ginder - Coding Question 2

# import necessary packages

import sys, json
from random import randint

# open and read json file using the system argv module, set to reading mode

with open(sys.argv[1], 'r') as f:
    
    # load json object and save it as a variable, using json module
    
    j = json.load(f)
    

def updater():
    """Open json file again, now in writing mode. Create as many random
    new ids as requested in the command line. Update the json file by
    appending to the object. After all the new ids have been created,
    dump the new ids in with the old ones. Print the new ids as well.
    """
    with open(sys.argv[1], 'w') as f:

        # initiate list for printing new identifier(s)

        l = []

        # loop through number of desired new identifier(s)

        for i in range(int(sys.argv[2])):

            # initialize string for new identifier

            numbers = ''

            # generate a 7 digit interger where each digit is random
            # using random.randint, adding each digit onto the 'numbers' string, sequentially

            for i in range(7):
                numbers += str(randint(0,9))

            # 'g' character is desired at the end of each identifier

            numbers += 'g'

            # append the newly created identifier to the json object

            j.append({'barcode': numbers})

            # append the newly created identifier to the list for printing

            l.append(numbers)

        # update the json file with the new identifier(s)

        json.dump(j, f)

    # print new identifiers

    print(*l)
    
# define main function

def main():
    updater()


if __name__ == "__main__":
    main()
