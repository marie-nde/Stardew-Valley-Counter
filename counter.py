crops_spring = [
    ["Parsnip", 20, 6],
    ["Green Bean", 60, 1],
    ["Caulilflower", 80, 2],
    ["Potato", 50, 4],
    ["Tulip", 20, 4],
    ["Kale", 70, 4],
    ["Blue Jazz", 30, 3],
    ["Garlic", 40, 6],
    ["Rice", 40, 3],
    ["Rhubarb", 100, 2],
    ["Coffee", 2500, 1],
    ["Strawberry", 100, 1]
]

crops_summer = [
    ["Melon", 80, 2],
    ["Tomato", 50, 1],
    ["Blueberry", 80, 1],
    ["Hot Pepper", 40, 1],
    ["Wheat", 10, 6],
    ["Radish", 40, 4],
    ["Poppy", 100, 3],
    ["Summer Spangle", 50, 3],
    ["Hops", 60, 1],
    ["Corn", 150, 1],
    ["Sunflower", 200, 3],
    ["Red Cabbage", 100, 3],
    ["Starfruit", 400, 2],
    ["Coffee", 2500, 1],
]

crops_fall = [
    ["Pumpkin", 100, 2],
    ["Corn", 150, 1],
    ["Eggplant", 20, 1],
    ["Bok Choy", 50, 6],
    ["Yam", 60, 2],
    ["Cranberries", 240, 1],
    ["Wheat", 10, 6],
    ["Sunflower", 200, 3],
    ["Fairy Rose", 200, 2],
    ["Amaranth", 70, 3],
    ["Grape", 60, 1],
    ["Artichoke", 30, 3],
    ["Beet", 20, 4],
    ["Sweet Gem Berry", 1000, 1]
]


def counter(my_list):
    i = 0
    length = len(my_list)
    new_list = []
    while i < length:
        new_list.append(0)
        i = i + 1
    i = 0
    print("\nEnter the number you want to modify\n\n")
    while (i < length):
        print(str(i) + "- " + my_list[i][0] + ": " + str(new_list[i]) + "\n")
        i = i + 1
    i = 0
    user_answer = input("Type a number or c to confirm\n")
    while (user_answer != "c"):
        i = 0
        if (int(user_answer) >= 0 and int(user_answer) < length):
            new_result = input(my_list[int(user_answer)][0] + ": ")
            new_list[int(user_answer)] = int(new_result)
            print("\nEnter the number you want to modify\n\n")
            while (i < length):
                print(str(i) + "- " + my_list[i][0] + ": " + str(new_list[i]) + "\n")
                i = i + 1
            user_answer = input("Type a number or c to confirm\n")
        elif (user_answer != "c"):
            print("Invalid input")
            user_answer = input("Type a number or c to confirm\n")
    i = 0
    total = []
    while (i < length):
        total.append(my_list[i][2] * new_list[i])
        i = i + 1
    i = 0
    print ("\nTotal to buy\n")
    total_gold = 0
    while (i < length):
        print(str(i) + "- " + my_list[i][0] + ": x" + str(total[i]) + " for " + str(my_list[i][1] * total[i]) + "g\n")
        total_gold = total_gold + (my_list[i][1] * total[i])
        i = i + 1
    print("\nTotal to pay: " + str(total_gold) + "g")


season = input("Choose a season: \"spring\", \"summer\" or \"fall\"\n\n")
if (season == "spring"):
    counter(crops_spring)
elif (season == "summer"):
    counter(crops_summer)
elif (season == "fall"):
    counter(crops_fall)
else:
    print("Wrong season")