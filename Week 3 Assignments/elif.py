# Assignment: Quistion 1
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if it's 20% or higher.
    
    Args:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage.

    Returns:
    float: The final price after applying the discount, or the original price if discount is less than 20%.
    """
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price
    

    original_price = 1000  # Example original price
discount = 25          # Example discount percentage

final_price = calculate_discount(original_price, discount)
print(f"The final price is: {final_price}")