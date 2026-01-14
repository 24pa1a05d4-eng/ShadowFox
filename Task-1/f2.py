total = 0

for i in range(10):
    total += 10
    print(f"You finished {total} jumping jacks")

    tired = input("Are you tired? (yes/no): ")

    if tired.lower() == "yes" or tired.lower() == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no): ")
        if skip.lower() == "yes" or skip.lower() == "y":
            break

if total == 100:
    print("Congratulations! You completed the workout")
else:
    print("You completed a total of", total, "jumping jacks")
