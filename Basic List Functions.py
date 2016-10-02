cars = ["Cadillac","Ford", "Toyota", "Chevrolet", "BMW", "Nissan", "Honda" ]

for type in cars:
    print (type)
print ("\n")

cars.sort()
for car in cars:
    print car
print ("\n")

brand = []
newbrand = ""


print ("\nPlease enter a car brand that hasn't already been used. Type done when finished.")

while newbrand != "done":
    newbrand = raw_input("What brand will it be?: ")
    if newbrand != "done":
         brand.append(newbrand)

for car in brand:
    print car
print ("\n")

mergedlist = cars + brand # I used this to combine the raw inputs and the original list
mergedlist.sort() # Organizes both cars and the raw inputs
print mergedlist 
