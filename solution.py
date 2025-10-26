# Shopping Mall Discount Program

# Take input for the bill amount
amount = float(input("Enter your total bill amount: "))

# Check discount conditions
if amount >= 5000:
    discount = 0.20 * amount
    total = amount - discount
    print("You got a 20% discount!")
elif amount >= 2000 and amount < 5000:
    discount = 0.10 * amount
    total = amount - discount
    print("You got a 10% discount!")
else:
    discount = 0
    total = amount
    print("No discount applied.")

# Display results
print(f"Discount amount: ₹{discount:.2f}")
print(f"Total bill after discount: ₹{total:.2f}")
