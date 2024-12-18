import random

def roll_dice(sides_of_dice):
    return random.randint(1, sides_of_dice)

def main():
    dice_sides = 6 
    continue_rolling = True  
    
    while continue_rolling:
        user_input = input("Ready to roll? Enter Q to Quit: ")
        
        if user_input.lower() != "q":
            dice_result = roll_dice(dice_sides)  
            print("You have rolled a", dice_result)
        else:
            continue_rolling = False  

if __name__ == "__main__":
    main()