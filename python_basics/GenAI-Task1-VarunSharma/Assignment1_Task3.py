

#Task 3: Product Pricing

products=["TV 1","TV 2","Mobile","Phone 1","Phone 2","Laptop 1","Laptop 2"]

#creation of th price dict
price_dict={"Airpods": 15000, "Laptop": 100000, "Mobile": 80000, "Apple Watch": 40000, "Smart TV": 12000, "iPad": 30000, "Speakers": 2000, "Home Theatre": 5000}

print("Original Price List:", price_dict)
#update the value of existing item
price_dict["Laptop"]=120000

if "Speakers" in price_dict:
    del(price_dict["Speakers"])

print("Revised Price List:", price_dict)

#printing Average Price
avg_product = sum(price_dict.values()) / len(price_dict)    
print("Average Price of Products:", avg_product)
      
#printing product with maximum price
max_product = max(price_dict, key=price_dict.get)
print("Product with Maximum Price:", max_product)

#printing minimum price
min_product = min(price_dict, key=price_dict.get)
print("Product with Minimum Price:", min_product)


