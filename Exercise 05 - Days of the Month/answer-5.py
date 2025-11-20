january = 31     #
february = 28    #
march = 31       #
april = 30       #
may = 31         #      
june = 30        # intializing number of days in each month
july = 31        #
august = 31      #
september = 30   #
october = 31     #
november = 30    #
december = 31    #


days_in_month = [january, february, march, april, may, june, july, august, september, october, november, december]  #initializing list of days in each month via an array 
month = int(input("Enter month (1-12): "))     #asking user for month number
if 1 <= month <= 12:
    print(f"Number of days: {days_in_month[month - 1]}") #printing number of days in the month, 
else:
    print("Invalid month number. Please enter a number between 1 and 12.") #handling invalid month number