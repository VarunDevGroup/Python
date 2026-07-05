

#Task 2 : Categories

#list of 6 products : all string
products=["Airpods","Laptop","Mobile","Apple Watch","Smart TV","iPad","Speakers","Home Theatre"]

categories_set=set(products)
print("Printing the set of categories:", categories_set)

#additions of items in category
categories_set.add("Washing Machine")
categories_set.add("Iron Machine")
categories_set.add("Microwave Oven")
categories_set.add("iPad")
print("Printing the revised set of categories:", categories_set)

#how to check whether a cateroy exist in set and print the boolean
category_check="iPad" in categories_set
print("Does the category iPad exist in the set?", category_check)

category_check="Gaming console" in categories_set
print("Does the category Gaming console exist in the set?", category_check)

#total number of items in the category
print("The number of categories in the set is:", len(categories_set))
