import os
import csv
csv_path = os.path.join("/Users/himadevulapalli/Documents/Tech/GTATL201908DATA3/02 - Homework/03-Python/Instructions/PyBank/Resources", "budget_data.csv")
# Open and read csv
with open(budget_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader) #<_csv.reader object at 0x1069e39e8>
    
    #skip the Header
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    #Read CSV into a List
    budget_list = list(csvreader)
    
    #Reads the total Length of the List
    totalMonths = len(budget_list)
    print("Total Months in the Data Sheet = {}".format(totalMonths))
    
    #Total Net Amount of Profit/Losses
    totalNetProfitLosses = 0
    prev = 0
    totalchange = 0
    avgchange = 0
    isFirstRow = True
    
    for row in budget_list:
        
        totalNetProfitLosses += int(row[1])
        
        if isFirstRow:
            prev = int(row[1])
            #print(prev)             
            isFirstRow =False
        else:
            change = (int(row[1]) - prev)
            totalchange += change
            prev = int(row[1])
    print("Total Net Profit/Losses = {}".format(totalNetProfitLosses))
    print("Total Change = {}".format(totalchange))
    print("Average of Change in ProfitLosses is {}".format(totalchange/(totalMonths-1)))
