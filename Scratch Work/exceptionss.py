# Multiple errors
try:
    # Open the file
    filename = "exceptionss.py"
    my_file = open(filename)

    # Read from the file and strip any trailing line feeds
    my_line = my_file.readline()
    my_line = my_line.strip()

    # Convert to a number
    my_int = 0

    # Do a calculation
    my_calculated_value = 101 / my_int

except FileNotFoundError:
    print(f"Could not find the file '{filename}'.")
except IOError:
    print(f"Input/Output error when accessing the file '{filename}'.")
except ValueError:
    print("Could not convert data to an integer.")
except ZeroDivisionError:
    print("Division by zero error.")
except:
    print("Unexpected error.")
