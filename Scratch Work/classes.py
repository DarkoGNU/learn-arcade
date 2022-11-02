# Class with a static variable
class ClassB():
    x = 7


def main():
    # Create a class instance
    b = ClassB()

    # This prints 7
    print(b.x)

    # This also prints 7
    print(ClassB.x)

    # Set x to a new value using the class name
    ClassB.x = 8

    # This also prints 8
    print(b.x)

    # This prints 8
    print(ClassB.x)

    # Set x to a new value using the instance.
    # Wait! Actually, it doesn't set x to a new value!
    # It creates a brand new variable, x. This x
    # is an instance variable. The static variable is
    # also called x. But they are two different
    # variables. This is super-confusing and is bad
    # practice.
    b.x = 9

    # This prints 9
    print(b.x)

    # This prints 8. NOT 9!!!
    print(ClassB.x)


main()
