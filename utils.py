def get_boolean_input(prompt):
    while True:
        response = input(prompt + " (y/n): ").lower()
        if response in ["y", "n"]:
            return response == "y"
        print("Invalid input, please enter 'y' or 'n'.")

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt + ": "))
        except ValueError:
            print("Invalid input, please enter a number.")
