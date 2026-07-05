
print("USER OPTIONS:")
print("1. Add order amount to the running list")
print("2. Show all orders and totals after applying discounts")
print("q. Quit")

user_input=input("Please select an option (1, 2, or q): ")


while user_input!='q':

        if user_input=='1':
             print("you have selected option 1")
        elif user_input=='2':
             print("you have selected option 2")
        else:
            print("Invalid option. Please select 1, 2, or q.")
        user_input=input("Please select an option (1, 2, or q): ")
