def check_overlap(array1, array2):
    # Check if there are any common elements
    common_elements = set(array1) & set(array2)
    return len(common_elements) > 0


# Get input from the user
def main():
    try:
        x1 = int(input("Enter x1: "))
        x2 = int(input("Enter x2: "))
        x3 = int(input("Enter x3: "))
        x4 = int(input("Enter x4: "))
    except ValueError:
        print("Please enter valid integer values.")
        exit(1)

    array1 = list(range(x1, x2 + 1))
    array2 = list(range(x3, x4 + 1))

    # Check for overlap
    if check_overlap(array1, array2):
        print("The lines overlap.")
    else:
        print("The lines do not overlap.")


if __name__ == "__main__":
    main()
