# match-case statements (switch)

def is_weekend(day):
    match day:
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
            return False
        case "Saturday"|"Sunday":
            return True
        case _:
            return False
        
print(is_weekend("Pizza"))