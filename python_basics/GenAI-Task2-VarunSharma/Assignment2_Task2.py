orders=[1200,2500,800,1750,3000]

print("----------------------------------------------")
print("|              ORDER SUMMARY                 |")
print("----------------------------------------------")

discount_percentage = 0
total_revenue = 0
tax = 5
for order in orders:
    try:
        if order >= 2000:
            discount_percentage = 15
        elif order >= 1500:
            discount_percentage = 10
        elif order >= 1000:
            discount_percentage = 7
        else:
            discount_percentage = 0

        sub_total_after_discount = order - (order * discount_percentage / 100)
        total_amount = sub_total_after_discount + (sub_total_after_discount * tax / 100)
        total_revenue=total_revenue+sub_total_after_discount
        print(f"{order} --> {discount_percentage}% -->{sub_total_after_discount} ")
       

        
    except:
        print("Invalid input. Please enter a valid number.")

print("----------------------------------------------")
print(f"| TOTAL REVENUE : {total_revenue} |")
print("----------------------------------------------")