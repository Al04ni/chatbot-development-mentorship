# 1football_points task

def football_points(wins, draws, losses):
    # Write your solution here
    #i used end to make it look more clearly
    print('wins: ',end='')
    wins=int(input())
    print('Draws: ',end='')
    draws=int(input())
    print('Losses: ',end='')
    losses=int(input())
    if wins>=0 and draws>=0 and losses>=0:
    #logic behind
      wins=wins*3
      draws=draws*1
      losses=losses*0
      return (wins+draws+losses)
    else:
     print('Input must be greater or equal to 0')
    
    pass

# Test cases
print(football_points(3, 4, 2))  # Output should be 13
print(football_points(5, 0, 2))  # Output should be 15
print(football_points(0, 0, 1))  # Output should be 0


# 2.chatroom_status task

def chatroom_status(users):
    # Write your solution here
      #seems that this logic is so tricky
    #users=[]- no need to make this list
    if len(users)==0:
        return('No one online')

    elif len(users)==1:
        return(users[0]+' online')

    elif len(users)==2:
        return(users[0]+' and '+users[1]+' online')

    elif len(users)>2:
        return(users[0]+' , '+users[1] +' and '+str(len(users)-2)+' more online')
    pass

# Test cases
print(chatroom_status([]))  # Output should be "no one online"
print(chatroom_status(["paRIE_to"]))  # Output should be "paRIE_to online"
print(chatroom_status(["s234f", "mailbox2"]))  # Output should be "s234f and mailbox2 online"
print(chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"]))
# Output should be "pap_ier44, townieBOY and 4 more online"

# 3. pin_validation

def is_valid_PIN(pin):
    # Write your solution here
    if len(pin)==4:
       return(pin.isdecimal())
    else:
      return(pin.isalpha())
    pass

# Test cases
print(is_valid_PIN("1234"))  # Output should be True
print(is_valid_PIN("12345"))  # Output should be False
print(is_valid_PIN("a234"))  # Output should be False
print(is_valid_PIN(""))  # Output should be False
