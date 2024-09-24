def calculate_discount(price, discount_percent):
    # Apply discount only if discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user to enter the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate and display the final price
    final_price = calculate_discount(price, discount_percent)
    
    if discount_percent >= 20:
        print(f"The final price after a {discount_percent}% discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount percentage.")