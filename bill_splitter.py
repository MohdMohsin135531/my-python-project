# write your code here
def get_number(prompt: str) -> float:
    """        
    Ask the user for a positive number with validation.            
    Keeps asking until the user enters a valid positive number.        
    Rejects negative numbers and non-numeric input.            
    Args:            
    prompt: The message to show the user            
    Returns:            
    A positive float number            
    """
    while True:
        try: 
            value = float(input(prompt))
            if value < 0:
                print("Please type positive number")
            else:
                return value
        except ValueError:
            print("Please type number")


def main():
    no_of_friends_joining = int(get_number("Enter the number of friends joining (including you):\n"))
    friend_names = []
    
    if no_of_friends_joining < 1:
        print("No one is joining for the party")

    else:
        print("Enter the name of every friend (including you), each on a new line:")
        for _ in range(no_of_friends_joining):
            name = input()
            while name.strip() == "":
                print("Please enter a valid name")
                name = input()
            friend_names.append(name.strip())

        total_bill = get_number("Enter total bill amount:")
        tip_percent = get_number("Enter tip percentage:")
        tip_amount = tip_percent / 100 * total_bill
        split_bill = (total_bill + tip_amount) / no_of_friends_joining

        friends_dict = {}
        for name in friend_names :
            friends_dict[name] = round(split_bill, 2)

        for name, amount in friends_dict.items():
            print(f"{name} should pay ${amount}")


if __name__ == "__main__":
    main()
