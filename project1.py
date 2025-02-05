name = input("Enter your name: ")
print("Hello " + name + " Welcome to my game!")

should_we_play = input("Do you want to play? y/n: ").lower()

if should_we_play == "y":
    print("Great! Let's play!")
    direction = input("Enter the direction you want to go (left/right): ").lower()
    if direction == "left":
        print("You went left and fell down a cliff! , Game Over!")
    elif direction == "right":
        print("You went right!")
        choice = input(
            "Now you see a bridge. Do you want to swim under it or cross it? s/c: "
        ).lower()
        if choice == "s":
            print("You swam under the bridge and escaped! , Game Over!")
        elif choice == "c":
            print("You crossed the bridge and fell down a cliff! , Game Over!")
    else:
        print("Invalid direction!")
        print("Game Over!")
else:
    print("Okay, let's not play then.")
