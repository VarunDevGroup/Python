
try:
    order_amount=int(input("Please enter the order amount:"))
    discount_percentage=0
    tax =5

    if(order_amount>=2000):
        discount_percentage=15
    elif(order_amount>=1500):
        discount_percentage=10
    elif(order_amount>=1000):
        discount_percentage=7
    else:
        discount_percentage=0
    
    
    sub_total_after_discount=order_amount-(order_amount*discount_percentage/100)
    total_amount=sub_total_after_discount+(sub_total_after_discount*tax/100)
    
    print("Order Value is:",order_amount)
    print("Discount percentage is:",discount_percentage,"%")
    print("Sub Total after discount is :",sub_total_after_discount)
    print("Tax is:",tax,"%")
   
    print("Total amount to be paid is:",total_amount)


except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()  




