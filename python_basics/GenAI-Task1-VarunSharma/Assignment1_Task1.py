
#Task 1 : Product Collections 

#list of 6 products : all string
products=["Airpods","Laptop","Mobile","Apple Watch","Smart TV","iPad"]

#tuple of sample products
sample_products=("Airpods",25399,"Headphones")

#printing second product from the products list
print("First item in the list is:", products[1])

#printing last product from the products list
print("Last item in the list is:", products[-1])

#add two products and print the products list
products.append("Speakerrs")
products.append("Home Theatre")
print("Printing the list of products:", products)


#convert sample_products tuple to list and change the second product to 40000 and convert it back to tuple and print the new tuple
sample_productList=list(sample_products)
sample_productList[1]=40000
sample_products=tuple(sample_productList)
print("Printing the revised tuple of products:", sample_products)

