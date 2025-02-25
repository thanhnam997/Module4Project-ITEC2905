class DunnDelivery:
    # Constructor method - creates a new instance of a delivery
    def __init__(self):
        # Class attributes demonstrate encapsulation
        # by keeping related data together

        # Menu Attribute - menu of items you can order to be delivered
        self.menu = {
            "Energy Drinks": ["Monster", "Rockstar"],
            "Coffee Drinks": ["Latte", "Cappuccino", "Peppermint Mocha", "Pumpkin Spice Latte", "Iced Caramel Macchiato"],
            "Breakfast": ["Bagel", "Muffin", "Scone"],
            "Lunch": ["Falafel Wrap", "Hummus & Pita", "Chicken Wrap"]
        }

        # Price encapsulated within the class
        self.prices = {
            "Monster": 3.99, "Rockstar": 3.99,
            "Latte": 4.99, "Cappuccino": 4.99, "Peppermint Mocha": 5.49,
            "Pumpkin Spice Latte": 5.99, "Iced Caramel Macchiato": 5.29,
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
        else:
            print("\n=== Full Menu ===")
            for cat, items in self.menu.items():
                print(f"\n{cat}:")
                for item in items:
                    print(f"- {item}: ${self.prices[item]:.2f}")

    # Method to calculate the total cost of the order
    def calculate_total(self, items, has_student_id=False, priority_delivery=False):
        # Calculate the total
        total = sum(self.prices[item] for item in items)

        # Apply student discount if applicable
        if has_student_id and total > 10:
            total *= 0.9  # Apply 10% discount

        # Apply priority delivery charge
        if priority_delivery:
            total += 2  # Extra $2 for faster delivery

        # Return the total cost
        return total

    # Method to calculate the delivery time based on location, time of day, and priority delivery
    def estimate_delivery(self, location, current_hour, priority_delivery=False):
        # Calculate the base time
        base_time = self.delivery_locations[location]

        # Adjust delivery time during peak hours
        if (9 <= current_hour <= 10) or (11 <= current_hour <= 13):
            base_time += 5  # Increase by 5 minutes during peak hours

        # Reduce time for priority delivery
        if priority_delivery:
            base_time = max(0, base_time - 3)  # Ensure time doesn't go below 0

        # Return final estimated delivery time
        return base_time

    # Method that prints the order (receipt)
    def print_order(self, location, items, current_hour, has_student_id=False, priority_delivery=False):
        # Display the order information
        print("\n=== Order Summary ===")
        print(f"Delivery to: {location}")
        print("\nItems Ordered:")

        # Loop through the list of menu items ordered
        for item in items:
            print(f"- {item}: ${self.prices[item]:.2f}")

        # Call the method to get the total cost and the delivery time
        subtotal = sum(self.prices[item] for item in items)
        total = self.calculate_total(items, has_student_id, priority_delivery)
        delivery_time = self.estimate_delivery(location, current_hour, priority_delivery)

        # Display the subtotal
        print(f"\nSubtotal: ${subtotal:.2f}")

        # Apply student discount message if applicable
        if has_student_id and total < subtotal:
            print("Student Discount Applied!")

        # Apply priority delivery message if selected
        if priority_delivery:
            print("Priority Delivery Selected (+$2)")

        # Display total after discount & estimated delivery time
        print(f"Total after discounts: ${total:.2f}")
        print(f"Estimated delivery time: {delivery_time} minutes")

        self.rate_delivery()  # Ask for delivery rating

    # Allow users to rate the delivery service
    def rate_delivery(self):
        while True:
            try:
                rating = int(input("\nRate your delivery (1-5 stars): "))
                if 1 <= rating <= 5:
                    print(f"Thank you for your {rating}-star rating!")
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

    # Search for items under a certain price
    def search_by_price(self, max_price):
        print(f"\n=== Items Under ${max_price:.2f} ===")
        found = False
        for item, price in self.prices.items():
            if price <= max_price:
                print(f"- {item}: ${price:.2f}")
                found = True

        if not found:
            print("No items found in this price range.")

# Main method is executed as soon as the program runs
def main():
    delivery = DunnDelivery()

    print("\nWelcome to Dunn Brothers Delivery!")
    delivery.show_menu()  # Show full menu

    # User selects a delivery location
    print("\nDelivery Locations:", ", ".join(delivery.delivery_locations.keys()))
    location = input("Enter your delivery location: ")
    while location not in delivery.delivery_locations:
        location = input("Invalid location. Please enter a valid location: ")

    # User selects items to order
    order = []
    while True:
        item = input("\nEnter an item to add to your order (or type 'done' to finish): ")
        if item.lower() == "done":
            break
        elif item in delivery.prices:
            order.append(item)
        else:
            print("Item not found. Please choose an item from the menu.")

    if not order:
        print("No items ordered. Exiting.")
        return

    has_student_id = input("Do you have a student ID? (yes/no): ").strip().lower() == "yes"
    priority_delivery = input("Would you like priority delivery for an extra $2? (yes/no): ").strip().lower() == "yes"
    current_hour = int(input("Enter the current hour (0-23): "))

    delivery.print_order(location, order, current_hour, has_student_id, priority_delivery)

    max_price = float(input("\nEnter a maximum price to find budget-friendly items: "))
    delivery.search_by_price(max_price)


if __name__ == "__main__":
    main()
