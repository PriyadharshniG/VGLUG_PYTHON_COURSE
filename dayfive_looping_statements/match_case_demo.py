# match_case_demo.py
# Demonstrating the match-case statement (Python 3.10+)

day = input("Enter a day of the week: ").lower()

match day:
    case "monday":
        print("Start of the work week!")
    case "tuesday":
        print("Second day of the week")
    case "wednesday":
        print("Midweek day")
    case "thursday":
        print("Almost Friday")
    case "friday":
        print("Last workday of the week!")
    case "saturday" | "sunday":
        print("It's the weekend")
    case _:
        print("Not a valid day")
