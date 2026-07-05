daily=[200,150,0,400,50,-1,300]

total_sales=0

for d in daily:
    if d < 0:
        break
    elif d == 0:
        continue
    else:
        total_sales=total_sales+d
        print("Running total sales:", total_sales)

print("Total sales:", total_sales)