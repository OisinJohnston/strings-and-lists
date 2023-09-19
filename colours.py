colours = ["blue", "green", "black", "purple", "orange", "magenta", "pink", "white", "indigo", "violet"]


while True:
    try:
        start_number = int(input("pick a start number between 0 and 4: "))
        assert start_number <= 4 and start_number >=0
        end_number = int(input("pick an end number between 5 and 9: "))
        assert end_number <=9 and end_number >= 5
        break
    except ValueError:
        print("Invalid input try again.")
    except AssertionError:
        print("Index out of range try again.")

splice = colours[start_number:end_number]

print(f'{splice = }')
