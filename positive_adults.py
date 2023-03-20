# Henry Ginder - Coding Question 3

# import necessary packages

import sys, json
from datetime import datetime

# get today's datetime

todays_date = datetime.now()

# open and read the files named on the command line using sys.argv
# load the json files into lists

with open(sys.argv[1], 'r') as f:
    participants_json = json.load(f)
    
with open(sys.argv[2], 'r') as f:
    results_json = json.load(f)


def dic_getter(results):
    """Convert the results list into a dictionary containing all participants
    who tested positive in the last 30 days as the key, where the values are
    lists containing: [days since last tested (int), 
    most recent test result (str), most recent test date (datetime.datetime)]
    
    Arguments:
        results = list of dictionaries
    """
    
    # initialize dictionary object
    
    d = {}
    
    # loop through the length of the results
    
    for i in range(len(results)):
        
        # for each loop, grab the participant's id number, test date, and result
        
        user = results[i]['participant']
        date = (results[i]['date'].split('-'))
        result = results[i]['result']
        
        # turn date string into list of intergers for datetime()
        # adding zeros for hrs,min,sec
        
        add_zeros = [int(i) for i in date] + [0, 0, 0]
        test_date = datetime(*add_zeros)
        
        # subtract the datetime objects and get the days difference in return
        
        days_diff = (todays_date - test_date).days

        # if test is within last 30 days, check if they are already
        # in the dictionary. If they are then check if this test is more recent.
        # If it is then reassign the values in the dictionary. If they are not
        # already in the dictionary then assign their list of values
        
        if (days_diff <= 30):
            if user in d:
                if (days_diff < d[user][0]):
                    d[user][0] = days_diff
                    d[user][1] = result
                    d[user][2] = test_date
            else:
                d[user] = [days_diff, result, test_date]

    return d


def participant_checker(d, participants):
    """Given d, and 'participants' list of dictionaries, check if each person
    in d is elgible to be printed by calculating their age. Those who are at
    least 18 years old will be printed.
    """
    
    # initialize dictionary for birthdates
    
    users = {}
    
    # assign each participant as the key, and their birthdate the value
    
    for i in range(len(participants)):
        users[participants[i]['participant']] = participants[i]['birthdate']
        
    # loop through participants, calculate the time difference using techniques from earlier
    # convert time difference to years
    
    for i in (users.keys()):
        date = users[i].split('-')
        add_zeros = [int(i) for i in date] + [0, 0, 0]
        birth_date = datetime(*add_zeros)
        time_diff = (todays_date - birth_date)
        age_years = (time_diff.days / 365)
        
        # if the participant isn't in d then they don't apply, so skip them
        
        if i not in d.keys():
            continue
            
        # if the participant is at least 18 then we can print out their most recent test info
        
        if age_years >= 18:
            
            # combine the strings seperately so we can get it to 
            # print out right, with the commas as desired
            one = 'participant ' + i
            two = 'age ' + str(int(age_years))
            three = 'result ' + d[i][1]
            four = 'date ' + str(datetime.date(d[i][2]))
            print(one+', '+two+', '+three+', '+four)


# define main function

def main():
    dictionary = dic_getter(results_json)
    participant_checker(dictionary, participants_json)


if __name__ == "__main__":
    main()
    
