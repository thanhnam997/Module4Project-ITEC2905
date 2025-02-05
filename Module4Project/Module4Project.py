class DunnDelivery:
    # Constructor method - creates a new instance of a delivery
    def __init__(self):
        # Class attributes demonstrate encapsulation
        # by keeping related data together

        # Menu Attribute - menu of items you can order to be delivered
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuccino"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }

        # Price encapsulated within the class
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuccino": 4.99,
            "Bagel": 2.99, "Muffin": 2.99, "Scone": 2.99,
            "Falafel Wrap": 8.99, "Hummus & Pita": 7.99, "Chicken Wrap": 8.99
        }

        # Delivery locations and number of minutes to deliver to that location
        self.delivery_locations = {
            "Library": 10,
            "Academic Success Center": 8,
            "ITEC Computer Lab": 5
        }

    # Show the menu of items available for delivery
    def show_menu(self, category=None):
        if category:
            print(f"\n==={category}===")
            # Loop through the items in that specific category on the menu
            # and display them to the user
            if category in self.menu:
                for item in self.menu[category]:
                    print(f"{item}: ${self.prices[item]:.2f}")

    # Method to calculate the total cost of the order
    def calculate_total(self, items, has_student_id=False):
        # Calculate the total
        total = sum(self.prices[item] for item in items)

        # Apply student discount if applicable
        if has_student_id and total > 10:
            total *= 0.9  # Apply 10% discount

        # Return the total cost
        return total

    # Method to calculate the delivery time based on location and time of day
    def estimate_delivery(self, location, current_hour):
        # Calculate the base time
        base_time = self.delivery_locations[location]
        # Adjust delivery time during peak hours
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            return base_time + 5  # Increase by 5 minutes during peak hours

        # Return base time if it's not a peak hour
        return base_time

    # Method that prints the order (receipt)
    def print_order(self, location, items, current_hour, has_student_id=False):
        # Display the order information
        print("\n=== Order Summary ===")
        print(f"Delivery to: {location}")
        print("\nItems Ordered:")

        # Loop through the list of menu items ordered
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")

        # Call the method to get the total cost and the delivery time
        total = self.calculate_total(items, has_student_id)
        delivery_time = self.estimate_delivery(location, current_hour)
        # Display the subtotal
        subtotal = sum(self.prices[item] for item in items)
        print(f"\nSubtotal: ${subtotal:.2f}")

        # Apply student discount message if applicable
        if has_student_id and total < subtotal:
            print("Student Discount Applied!")

        # Display total after discount & estimated delivery time
        print(f"Total after discount: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")

# Main method is executed as soon as the program runs
def main():
    delivery = DunnDelivery()
    delivery.show_menu("Coffee Drinks")
    
    # Sample order at 9:30 AM (peak morning hour)
    order = ["Latte", "Bagel"]
    delivery.print_order("ITEC Computer Lab", order, 9, has_student_id=True)

if __name__ == "__main__":
    main()