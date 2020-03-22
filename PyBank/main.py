import os
import csv
#Create empty lists 
months = []
pro_loss =[]
change_pl = []
total_periods = 0
previous_pl = []
total_pl = 0
g_increase = 0
g_decrease = 0

with open('budget_data.csv', 'r') as data_file:
    #read csv file
    csv_data = csv.reader(data_file)

    #skip headers found with the for loop above and declare line
    csv_data_header = next(csv_data)
    line = next(csv_data)
    
    previous_pl = int(line[1])
    total_periods += 1
    total_pl += 1
    #Loop for Total periods, pro_loss and changepl for the period
    #Convert strings into integers for sum of pro_loss
    for line in csv_data:
        
        total_periods +=1 
        total_pl = total_pl + int(line[1])

        change_pl = int(line[1]) - previous_pl
        pro_loss.append(change_pl)
        previous_pl = int(line[1])

        average_change = round((sum(pro_loss)/len(pro_loss)), 2)

        months.append(line[0])
        #compute for greatest increase and decrease profits and their 
        # corresponding periods using operators
        if int(line[1]) > g_increase:
            g_increase = int(line[1])
            g_increase_month = line[0]
        
        if int(line[1]) < g_decrease:
            g_decrease = int(line[1])
            g_decrease_month = line[0]
        #use max and min to establish the g increase and decrease
        g_increase_pro = max(pro_loss)
        g_decrease_pro = min(pro_loss)
             
#global variables I take them out of the loop...Use len for counting the number of months
#print to the terminal
count_months = total_periods  
print (f"Financial Analysis")
print (f"===============================")
print (f"Total months:  {count_months}")
print (f"Total: ${total_pl}")
print (f"Average change: ${average_change}")
print (f"Greatest Increase in Profits: {g_increase_month}, ${g_increase_pro}")
print (f"Greatest Decrease in Profits: {g_decrease_month}, ${g_decrease_pro}")


#Exporting results to a txt
#Open file with 'w' and declare the variables to put the contents in

with open("financial_analysis.txt", 'w',) as txtfile:

    txtfile.write(f"Financial Analysis \n")
    txtfile.write("============================== \n")
    txtfile.write(f"Total months:  {count_months} \n")
    txtfile.write(f"Total : $ {total_pl} \n")
    txtfile.write(f"Average change is $ {average_change} \n")
    txtfile.write(f"Greatest Increase in Profits: {g_increase_month}, ${g_increase_pro} \n")
    txtfile.write(f"Greatest Decrease in Profits: {g_decrease_month}, ${g_decrease_pro} \n")
    