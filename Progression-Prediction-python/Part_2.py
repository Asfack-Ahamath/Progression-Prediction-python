# Import necessary modules
from module.graphics import *

# Variables with initial values set to 0
pass_credits = 0
defer_credits = 0
fail_credits = 0
max_count = 0
x_start = 0
x_pos = 0
total_outcomes = 0

# List to store tuples of student data (outcome, pass_credits, defer_credits, fail_credits)
student_data = []

# Constants for the dimensions of the graphics window
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 450

# Constants for the width and spacing of bars in the histogram
BAR_WIDTH = 80
BAR_SPACING = 15

# List of colors for each bar in the histogram
BAR_COLORS = ["light green", "light blue", "gray", "pink"]

# List of possible outcomes for students
OUTCOMES = ["Progress", "Trailer", "Retriever", "Excluded"]

# Dictionary to store counts of each outcome category
outcome_counts = {category: 0 for category in OUTCOMES}

# Function for the Student Progression Outcome Prediction Tool
def prediction_tool_header():
    """
    Display the header for the Student Progression Outcome Prediction Tool.

    This function prints a formatted header with information about the tool.

    Usage:
    Call this function to print the header when using the Student Progression Outcome Prediction Tool.
    """
    print("\n============================================================================================")
    print("                         Student Progression Outcome Prediction Tool")
    print("============================================================================================\n") 
    print("┌────────────────────────────────┐ ┌─────────────────────┐ ┌───────────────────────────────┐")
    print("│ Volume of Credit at Each Level │ │ Progression Outcome │ │ To enter another set of data? │")
    print("└────────────────────────────────┘ └─────────────────────┘ └───────────────────────────────┘")
    print("┌──────┐     ┌───────┐    ┌──────┐                         ┌───────────────────────────────┐")
    print("│ Pass │     │ Defer │    │ Fail │                         │       Yes - Y / Quit - Q      │")
    print("└──────┘     └───────┘    └──────┘                         └───────────────────────────────┘")
    print("────────────────────────────────────────────────────────────────────────────────────────────")

# Dictionary to map outcomes to corresponding display texts
outcome_mapping = {
    "Progress": "\t\t\t\t\t   Progress",
    "Trailer": "\t\t\t\t\t   Progress \n\t\t\t\t       (module trailer)",
    "Retriever": "\t\t\t\t       Module retriever",
    "Excluded": "\t\t\t\t\t   Excluded"
}

# Dictionary for display labels in list
outcome_display = {
    "Progress": "Progress",
    "Trailer": "Progress (module trailer)",
    "Excluded": "Exclude",
    "Retriever": "Do not progress – module retriever"
}

# Function to get integer input within a specified range
def integer_input(prompt):
    """
    Takes an integer input from the user and validates it within a specific range.

    Args:
    - prompt (str): The prompt message to display.

    Returns:
    - int: The valid integer input.
    """
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 20, 40, 60, 80, 100, 120]:
                return value
            print("---------- Out of range ----------")
        except ValueError:
            print("-------- Integer Required --------")

# Function to get pass, defer, and fail credits and ensure the total is 120
def get_credits():
    """
    Gets credits for pass, defer, and fail from the user and validates the total.

    Returns:
    - tuple or None: A tuple of pass, defer, and fail credits if the total is 120, otherwise None.
    """
    pass_credits = integer_input("   ")
    defer_credits = integer_input("                 ")
    fail_credits = integer_input("                             ")

    total = pass_credits + defer_credits + fail_credits
    if total != 120:
        print("\t\t\t\t\tTotal Incorrect")
        return None
    return pass_credits, defer_credits, fail_credits

# Function to predict the outcome based on pass, defer, and fail credits
def predict_outcome(pass_credits, defer_credits, fail_credits):
    """
    Predicts the outcome based on pass, defer, and fail credits.

    Args:
    - pass_credits (int): The number of pass credits.
    - defer_credits (int): The number of defer credits.
    - fail_credits (int): The number of fail credits.

    Returns:
    - str: The predicted outcome.
    """
    if pass_credits == 120:
        return "Progress"
    elif pass_credits == 100:
        return "Trailer"
    elif fail_credits >= 80:
        return "Excluded"
    else:
        return "Retriever"

# Function to draw a bar in the histogram
def draw_bar(win, x_pos, category, count, max_count):
    """
    Draw a bar in a window representing a category in a histogram.

    Parameters:
    - win: The graphics window.
    - x_pos (float): The x-coordinate of the bar.
    - category (str): The category label.
    - count (int): The count of occurrences for the category.
    - max_count (int): The maximum count among all categories.
    """
    # Calculate the height of the bar based on count and max_count
    bar_height = (count / max_count) * (WINDOW_HEIGHT - 160) if max_count else 0  

    # Define the bottom left and top right points of the rectangle representing the bar
    bottom_left = Point(x_pos, WINDOW_HEIGHT - 80)
    top_right = Point(x_pos + BAR_WIDTH, WINDOW_HEIGHT - 80 - bar_height)

    # Create a rectangle (bar) and set its color
    bar = Rectangle(bottom_left, top_right)
    bar.setFill(BAR_COLORS[OUTCOMES.index(category)])
    bar.draw(win)

    # Add label for the category above the bar
    label = Text(Point(x_pos + BAR_WIDTH/2, WINDOW_HEIGHT - 63), category)
    label.draw(win)

    # Add text displaying the count at the top of the bar
    count_text = Text(Point(x_pos + BAR_WIDTH/2, WINDOW_HEIGHT - 95 - bar_height), str(count))
    count_text.draw(win)

# Function to create and display the histogram
def histogram_window(outcome_counts):
    """
    Displays a histogram based on outcome counts in a graphics window.

    Args:
    - outcome_counts (dict): A dictionary containing outcome counts.
    """
    # Create a graphics window
    win = GraphWin("Histogram", WINDOW_WIDTH, WINDOW_HEIGHT)

    # Find the maximum count among all categories
    max_count = max(outcome_counts.values())

    # Calculate the starting x-coordinate for the first bar
    x_start = (WINDOW_WIDTH - ((BAR_WIDTH + BAR_SPACING) * 4 - BAR_SPACING)) / 2

    # Iterate over categories and draw bars
    for index, category in enumerate(OUTCOMES):
        x_pos = x_start + index * (BAR_WIDTH + BAR_SPACING)
        draw_bar(win, x_pos, category, outcome_counts.get(category, 0), max_count)

    # Draw the x-axis
    x_axis_start_x = 15
    x_axis_end_x = WINDOW_WIDTH - 15 
    x_axis_y_position = WINDOW_HEIGHT - 79  
    x_axis = Line(Point(x_axis_start_x, x_axis_y_position), Point(x_axis_end_x, x_axis_y_position))
    x_axis.setWidth(2)
    x_axis.draw(win)

    # Add title to the histogram
    title = Text(Point(WINDOW_WIDTH / 2, 25), "Histogram Results")
    title.setSize(16)
    title.setStyle("bold")
    title.draw(win)

    # Display total outcomes at the bottom
    total_outcomes = sum(outcome_counts.values())
    text_to_display = f"{total_outcomes} outcome{'s' if total_outcomes > 1 else ''} in total."
    total_text = Text(Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 25), text_to_display)
    total_text.setSize(16)
    total_text.setStyle("bold")
    total_text.draw(win)

    # Wait for user click, then close the window
    try:
        win.getMouse()
    except GraphicsError:
        pass  
    finally:
        win.close()

# Function to display student data in List
def stored_data(student_data):
    """
    Display student progression data from a nested list.
    """
    print("Progression Data from List:\n")
    if not student_data:
        print("Student Data is Empty")
    else:
        for index, (outcome, pass_credits, defer_credits, fail_credits) in enumerate(student_data, start=1):
            print(f"{index:02d}. {outcome:<36} - {pass_credits:>5} {defer_credits:>5} {fail_credits:>5}")

# Main function where the program execution starts
def main():
    """
    The main function orchestrating the prediction tool.
    """
    prediction_tool_header()
    outcome_counts = {category: 0 for category in OUTCOMES}
    student_data = []

    while True:
        credits = get_credits()
        if credits:
            pass_credits, defer_credits, fail_credits = credits
            outcome = predict_outcome(pass_credits, defer_credits, fail_credits)
            print(f"{outcome_mapping[outcome]}")
            outcome_counts[outcome] += 1 

            specific_outcome = outcome_display.get(outcome, "Unknown Outcome")
            student_data.append((specific_outcome, pass_credits, defer_credits, fail_credits))

        while True:
            continue_input = input("\t\t\t\t\t\t\t\t\t   ").lower()
            if continue_input == 'q':
                histogram_window(outcome_counts)
                print("============================================================================================\n")
                print("Part 2\n")
                stored_data(student_data)
                print("\n============================================================================================")
                return
            elif continue_input == 'y':
                print("────────────────────────────────────────────────────────────────────────────────────────────")
                break
            else:
                print("\n\t\t\t\t\t\t\t    Invalid Input. Enter 'Y' or 'Q'\n")

# Call the main function to run the program
main()
