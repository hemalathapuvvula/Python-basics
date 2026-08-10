
def print_star():
    #Top Peak
    for i in range(1, 4):
        print(" " * (10 - i) + "*" * (2 * i - 1))

    #Middle Wings
    print("*" * 19)
    print(" " * 2 + "*" * 15)
    print(" " * 4 + "*" * 11)

    #Bottom Legs
    print(" " * 3 + "***" + " " * 7 + "***")
    print(" " * 2 + "**" + " " * 11 + "**")

print_star()
