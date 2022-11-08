def check_array(array):
    array = array.split()
    new_array = []

    for i in array:
        if len(i) <= 3:
            new_array.append(i)
    return new_array


def main():
    print(check_array(input("Please enter array: ")))


if __name__ == "__main__":
    main()
