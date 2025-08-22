while True:
    day = input("Enter a day of the week (Monday-Sunday): ").lower()

    match day:
        case "monday":
            print("ugh, Mondays right!")
            break
        case "tuesday":
            print("another workday, what a hassle...")
            break
        case "wednesday":
            print("when is this week gonna end...")
            break
        case "thursday":
            print("almost there, come on")
            break
        case "friday":
            print("last day, then I can feel free for a day")
            break
        case "saturday" | "sunday":
            print("no one talk to me, I'm resting for once")
            break
        case _:
            print("Please enter a valid day. Try again.")
