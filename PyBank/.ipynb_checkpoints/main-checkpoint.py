import os
import csv
budget_csv_path = os.path.join("/Users/himadevulapalli/Documents/Tech/GTATL201908DATA3/02 - Homework/03-Python/Instructions/PyBank/Resources", "budget_data.csv")
# Open and read csv
with open(budget_csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader) #<_csv.reader object at 0x1069e39e8>
    
    #Output file
    f=open("Budget_results.txt", "w")
    
    #skip the Header
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    #Read CSV into a List
    budget_list = list(csvreader)
    
    print("Financial Analysis")
    print("-----------------------------")
    
    print("Financial Analysis", file=f)
    print("-----------------------------", file=f)
    
    #Reads the total Length of the List
    totalMonths = len(budget_list)
    print("Total Months : {}".format(totalMonths))
    
    #write to the output file also
    print("Total Months : {}".format(totalMonths), file=f)
    
    #Total Net Amount of Profit/Losses
    totalNetProfitLosses = 0
    prev = 0
    totalchange = 0
    avgchange = 0
    min =0
    max = 0
    minDate = None
    maxDate = None

    isFirstRow = True
    
    for row in budget_list:
        
        totalNetProfitLosses += int(row[1])
        
        if isFirstRow:
            prev = int(row[1])
            isFirstRow =False
        else:
            change = (int(row[1]) - prev)
            #min = change
            #max = change
            totalchange += change
            prev = int(row[1])
            if min > change:
                minDate = row[0]
                min=change
            if max < change:
                maxDate = row[0]
                max=change                  
    print("Total ${}".format(totalNetProfitLosses))
    #print("Total Change = {}".format(totalchange))
    print("Average Change : ${}".format(round(totalchange/(totalMonths-1),2)))
    print('Greatest Increase in Profits:', maxDate, "(",max, ")")
    print ('Greatest Decrease in Profits:', minDate, '(', min, ")")
    #print('maxdate:', maxDate,'max:', max)
    
    
    print("Total ${}".format(totalNetProfitLosses), file=f)
    #print("Total Change = {}".format(totalchange))
    print("Average Change : ${}".format(round(totalchange/(totalMonths-1),2)), file=f)
    print('Greatest Increase in Profits:', maxDate, "(",max, ")", file=f)
    print ('Greatest Decrease in Profits:', minDate, '(', min, ")", file=f)
    
f.close()