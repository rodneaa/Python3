import os
import csv

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
    total_votes = [int(row[1]) for row in data]
    print(f'Total Votes: ', total_votes)

### A complete list of candidates who received votes (Column 3)
    result = {}

    for row in csvreader:
        if row[1] in result:
            result[row[2]].append(row[1])
        else:
            result[row[2]] = [row[1]]
    print result

----------------------------------------------------
#https://stackoverflow.com/questions/50850093/group-corresponding-rows-value-in-a-columns-python?noredirect=1&lq=1
ans = dict()
for n, row in enumerate(reader):
    if n == 0:
        titles = row
    else:
        num = row[0]
        if num in ans:
            t = ans[num]
            for i in range(1, len(row)):
                t[i].append(row[i])
        else:
            tmp = []
            for other in row:
                tmp.append([other])
            ans[num] = tmp

writer = csv.writer(open("2.csv", 'w'))
writer.writerow(titles)
for row in ans.values():
    tmp = []
    for key in row:
        if isinstance(t, str):
            tmp.append(key)
        else:
            tmp.append(",".join(key))
    writer.writerow(tmp)

  
### The percentage of votes each candidate won

### The total number of votes each candidate won

### The winner of the election based on popular vote
