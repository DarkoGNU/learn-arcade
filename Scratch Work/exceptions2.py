# Generating exceptions
def get_input():
    try:
        user_input = input("Enter something: ")
        if len(user_input) == 0:
            raise IOError("User entered nothing")
    except:
        print("Test test, exception here")


get_input()
