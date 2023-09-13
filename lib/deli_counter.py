# lib/deli_counter.py

# Initialize an empty list to represent the deli queue
katz_deli = []

# Function to display the current line
def line(katz_deli):
    if not katz_deli:
        return "The line is currently empty."
    else:
        line_message = "The line is currently:"
        for i, person in enumerate(katz_deli, start=1):
            line_message += f" {i}. {person}"
        return line_message

# Function for a new customer to take a number
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    return f"Welcome, {name}. You are number {position} in line."

# Function to serve the next person in line
def now_serving(katz_deli):
    if not katz_deli:
        return "There is nobody waiting to be served!"
    else:
        serving = katz_deli.pop(0)
        return f"Currently serving {serving}."

# Example usage
if __name__ == "__main__":
    take_a_number(katz_deli, "Ada")
    take_a_number(katz_deli, "Grace")
    take_a_number(katz_deli, "Kent")

    print(line(katz_deli))

    now_serving(katz_deli)

    print(line(katz_deli))

    take_a_number(katz_deli, "Matz")

    print(line(katz_deli))

    now_serving(katz_deli)

    print(line(katz_deli))
