first_line = input("Enter the first line of a nursery rhyme: ")
len_first_line = len(first_line)
print(f'{len_first_line = }')
while True:
    try:
        start_num = int(input("Start index: "))
        end_num = int(input("End index: "))
        break
    except ValueError:
        print("Invalid entry, please try again.")

segment = first_line[start_num-1:end_num]
print(f'{segment = }')

