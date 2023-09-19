subjects = ["computer science", "engineering", "maths", "applied maths", "biology", "physics"]

def main():
    print(f'{subjects = }')
    least_favourite = input("which is your least favourite subject? ").lower()

    if least_favourite not in subjects:
        print("Answer not in list of subjects")
        return

    subjects.remove(least_favourite)
    print(f'{subjects = }')

main()


