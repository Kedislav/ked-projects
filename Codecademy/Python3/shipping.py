print("What is the weight of your package?\n")
weight = float(input("> "))
cost = 0
print("Please note that Ground Shipping has a $20.00 flat charge, Ground Shipping premium has a $125.00 flat charge and Drone Shipping has no flat charges.\n")

# Ground Shipping Premium
premiumcost = weight + 125.00

# Ground Shipping
if weight <= 2:
  cost = 1.50 * weight + 20.00
  print("Your total will be $" + str(cost) + "\n")
elif weight > 2 and weight <= 6:
  cost = 3.00 * weight + 20.00
  print("Your total will be $" + str(cost) + "\n")
elif weight > 6 and weight <= 10:
  cost = 4.00 * weight + 20.00
  print("Your total will be $" + str(cost) + "\n")
else:
  cost = 4.75 * weight + 20.00
  print("Your total for Ground Shipping service will be $" + str(cost) + "\n")
  if cost > premiumcost:
    print("You might want to consider using our Ground Shipping Premium service for this package.\n")
    print("Price with Ground Service Premium: $" + str(premiumcost))
