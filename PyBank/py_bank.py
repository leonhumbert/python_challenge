import os
import csv
#Create empty lists 
months = []
pro_loss =[]
profit_change = []
with open('budget_data.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)
    #skip headers found with the for loop above
    next(csv_data)
    #Convert strings into integers for sum of pro_loss
    #use zip for 'j-i'
    for line in csv_data:
        months.append(f'{line[0]}')
        pro_loss.append(f'{line[1]}')
        int_pro_loss = [int (item) for item in pro_loss]
        profit_change = [j - i for i, j in zip(int_pro_loss[: -1], int_pro_loss[1 :])]
         
#global variables I take them out of the loop...Use len for counting the number of months
print ("Financial Analysis")
count_months = len(months)
print ("Total months: ", count_months)
#Convert elements of pro_loss list str into int values
#int_pro_loss = [int (item) for item in pro_loss]
#print (int_pro_loss)
TotalSum = sum(int_pro_loss)
print ("Total: $", TotalSum)
Total_change = sum(profit_change)
#print(Total_change)
Average_change = (Total_change/(len(months)-1))
print ("Average change is $" , round(Average_change, 2))
greatest_date = profit_change.index(max(profit_change))
#print (greatest_date)
#print ("Greatest Increase in Profit is ", count_months.values(greatest_date), max(profit_change))
print ("Greatest Increase in Profit: ", "$", max(profit_change))
print ("Greatest Decrease in Profit: ", "$", min(profit_change))


#Exporting results to a txt
#Specify file to write it to
#output_file = os.path.join("PyBank", "financial_analysis.txt")

#Open file with 'w' and declare the variables to put the contents in

with open("financial_analysis.txt", 'w',) as txtfile:
    txtfile.write(f"Financial Analysis \n")
    txtfile.write("============================== \n")
    txtfile.write(f"Total months:  {count_months} \n")
    txtfile.write(f"Total : $ {TotalSum} \n")
    txtfile.write(f"Average change is $ {round(Average_change, 2)} \n")
    txtfile.write(f"Greatest Increase of Profit is $ {max(profit_change)} \n")
    txtfile.write(f"Greatest Deacrease of Profit is $ {min(profit_change)} \n")
    