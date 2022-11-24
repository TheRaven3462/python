# [ ] create, call and test the adding_report() function
# Adding report Function has a defalut argument of "T" (Total only), But also expects "A" (All entries and total)
items = []
total = 0
def adding_report(items, report_type):
    while True:
        Q = input("Please enter an integer or \"Q\" to exit: ")
        print("Enter an integer or \"Q\":",Q)
        if Q.isnumeric():
            if report_type == "a":
                items.append(int(Q))

        elif Q.lower() == "q":
            print("It should be quiting!", report_type)
            if report_type == "a":
                print(*report, sep = "\n")
                print("Total\n",sum(items))
                print("Breaking")
                break

            elif report_type == "t":
                print("Total\n",sum(items))
                print("Breaking")
                break

        else:
            print("Input is invalid:",Q)   
        
print("Input an integer to add to total or \"Q\" to quit:")
report_type = input("Please select to see full statement or just total: (A/T)").lower()
adding_report(items, report_type)