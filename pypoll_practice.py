import os
import csv


# ? from collections import counter


#open csv
  csvpath = os.path.join("..", "python-challenge", "Pypoll", "Resources", "election_data.csv")

#read csv
  with open(csvpath, 'r') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=",")

#store the csv headers
    election_csv_header = next(csvreader) 
    next(csvfile, none)

#### The total number of votes cast (either column)
total_votes = 0
    for row in csvfile
    total_votes = [int(row[1]) for row in data]
    print(f'Total Votes: ', total_votes)

### A complete list of candidates who received votes, # and % of votes recd (Column 3)
    candidate_votes=[total_votes.count(candidate),  for candidate in candidates in set (candidates)]   #youtube caleb curry, Pyhton tutorial 10
    print(candidate, vote_counts)


      
    row =[ballotID, County, candidate]
    result = {}
    candidate = [row[2]   #column3
    candidates = []   #number of different variables (candidates) in column 3
    candidate_votes = 0  #number of times each variable appears
    
    for candidate_votes in total_votes:
        if candidate in candidates = candidate:
         candidate_votes = candidate_votes + 1
          else 
          candidate_votes = 1


        totalPurchases = totalPurchases + 1;
        totalSum = totalSum + price;
        if(price > 1800):
            sumAbove1800 = sumAbove1800 + price;
            countAbove1800 = countAbove1800 + 1;






### The total number of votes each candidate won ** candidate_votes

### The percentage of votes each candidate won is **each candidate divided by the total number of votes recd**


### The winner of the election based on popular vote ****max(candidate_votes)


----------------------------------------------------
#https://stackoverflow.com/questions/50850093/group-corresponding-rows-value-in-a-columns-python?noredirect=1&lq=1 ca
