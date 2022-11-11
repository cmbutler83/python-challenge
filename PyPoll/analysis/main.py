#!/usr/bin/env python
# coding: utf-8

# In[83]:


import os

import csv

num_rows = 0

candidates = []

csvpath = os.path.join( 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
    csv_header = next(csvreader)

      

    for row in csvreader:

        num_rows +=1


# In[84]:


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')    
    
    for row in csvreader:
        if (row[2]) not in candidates:
            candidates.append(row[2])
            
    candidates.pop(0)
    
    


# In[85]:


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')    
    cand_1 = candidates[0]
    cand_2 = candidates[1]   
    cand_3 = candidates[2]
    cand_1_votes = 0
    cand_2_votes = 0
    cand_3_votes = 0
    for row in csvreader: 
        if cand_1 == row[2]:
            cand_1_votes = int(cand_1_votes) + 1
        elif cand_2 == row[2]:
            cand_2_votes = int(cand_2_votes) + 1
        elif cand_3 == row[2]:
            cand_3_votes = int(cand_3_votes) + 1
   


# In[86]:


percent_of_votes1 = ((cand_1_votes) / (num_rows))

percent_of_votes2 = ((cand_2_votes) / (num_rows))

percent_of_votes3 = ((cand_3_votes) / (num_rows))


# In[87]:


percentage1 = "{:.3%}".format(percent_of_votes1)

percentage2 = "{:.3%}".format(percent_of_votes2)

percentage3 = "{:.3%}".format(percent_of_votes3)


# In[88]:


vote_counts = [cand_1_votes,cand_2_votes,cand_3_votes,]
for votes in vote_counts:
    if (max(vote_counts)) == cand_1_votes:
        winner = cand_1
    elif (max(vote_counts)) == cand_2_votes:
        winner = cand_2
    else:
        winner = cand_3


# In[89]:


print("Election Results")
print("                                ")
print("----------------------------")
print("                               ")
print(f"Total Votes: {num_rows}")
print("                               ")
print("----------------------------")
print("                               ")
print(f"{cand_1}: {percentage1} ({cand_1_votes})" )
print("                                ")
print(f"{cand_2}: {percentage2} ({cand_2_votes})" )
print("                                ")
print(f"{cand_3}: {percentage3} ({cand_3_votes})" )
print("                                ")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

