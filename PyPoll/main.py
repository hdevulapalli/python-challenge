import os
import csv

election_csv_path = os.path.join("/Users/himadevulapalli/Documents/Tech/GTATL201908DATA3/02 - Homework/03-Python/Instructions/PyPoll/Resources", "election_data.csv")

#open and read the csv file
with open(election_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip the Header
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    
     #Read CSV into a List
    election_list = list(csvreader)
    
    #Reads the total Length of the List
    totalVotes = len(election_list)
    print("Election Results")
    print("-----------------------------")
    print("Total Votes: {}".format(totalVotes))
    print("-----------------------------")
    candidate_dict={}
    
    #read each row
    for row in election_list:
       
        candidate_key = row[2]
        if candidate_key in candidate_dict.keys():
            #increment the count
            candidate_dict[row[2]]+=1
        else:
             candidate_dict[row[2]] = 1
    
    #print("Candidates : {}".format(candidate_dict))
    
    percent_candidate_key = {}
    maxcandidate = None
    maxval = 0
    for key in candidate_dict.keys():
        if candidate_dict[key]> maxval:
            maxval = candidate_dict[key]
            maxcandidate = key
        #print(key, candidate_dict[key])
        
        #calculate the % Votes for each Candidate
        percent_candidate_key[key] = round(((candidate_dict[key]/totalVotes)*100),3,)
        #Percentage of Votes for Candidate {}: {}%".format(key, percent_candidate_key[key]))
        print("{} : {}% ({})".format(key, percent_candidate_key[key], candidate_dict[key]))
    print("-----------------------------")
    print("Winner : {}".format(maxcandidate))
    print("-----------------------------")
    #with votes {}".format( maxcandidate, maxval))
    
