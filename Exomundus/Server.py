from random import randint

star_sorted_numbers = []
for i in range(5):
    star_number = randint(1,18)
    if star_number not in star_sorted_numbers:
        star_sorted_numbers.append(star_number)
    else:
        while True:
            if star_number in star_sorted_numbers:
                star_number = randint(1,18)
            else:
                star_sorted_numbers.append(star_number)
                break

goal_sorted_numbers = []
for i in range(5):
    goal_number = randint(1,18)
    if goal_number not in goal_sorted_numbers:
        goal_sorted_numbers.append(goal_number)
    else:
        while True:
            if goal_number in goal_sorted_numbers:
                goal_number = randint(1,18)
            else:
                goal_sorted_numbers.append(goal_number)
                break
