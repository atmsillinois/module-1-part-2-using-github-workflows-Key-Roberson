"""Rectangle Area Calculator.

This script asks the user for the length and width of a rectangle,
calculates the area, and prints the result.
"""

def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area.
    """
    return length * width


def main():
    """Main function to run the area calculator."""
    print("Welcome to the Rectangle Area Calculator!")

    # Ask the user to enter the length and width
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
    except ValueError:
        # Handle cases where the input is not a number
        print("Oops! Please enter valid numbers for length and width.")
        return

    # Call the function to calculate the area
    area = calculate_area(length, width)

    # Display the results
    print("\n--- Results ---")
    print(f"Length: {length:.2f}")
    print(f"Width: {width:.2f}")
    print(f"Area of the rectangle: {area:.2f} square units")


# This ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
