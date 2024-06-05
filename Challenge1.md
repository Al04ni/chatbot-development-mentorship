## 1.Football Points Task

Create a function that takes the number of wins, draws, and losses and calculates the number of points a football team has obtained so far.

- Wins get 3 points
- Draws get 1 point
- Losses get 0 points

**Examples:**
- `football_points(3, 4, 2)` ➞ 13
- `football_points(5, 0, 2)` ➞ 15
- `football_points(0, 0, 1)` ➞ 0

**Notes:**
- Inputs will be numbers greater than or equal to 0.

 ## 2. Chat Room Status Task

Write a function that returns the number of users in a chatroom based on the following rules:

- If there is no one, return "no one online".
- If there is 1 person, return "user1 online".
- If there are 2 people, return "user1 and user2 online".
- If there are n > 2 people, return the first two names and add "and n-2 more online".

**Examples:**
- `chatroom_status([])` ➞ "no one online"
- `chatroom_status(["paRIE_to"])` ➞ "paRIE_to online"
- `chatroom_status(["s234f", "mailbox2"])` ➞ "s234f and mailbox2 online"
- `chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])`
   ➞ "pap_ier44, townieBOY and 4 more online"

## 3. ATM PIN Code Validation Task

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. Your task is to create a function that takes a string and returns True if the PIN is valid and False if it's not.

**Examples:**
- `is_valid_PIN("1234")` ➞ True
- `is_valid_PIN("12345")` ➞ False
- `is_valid_PIN("a234")` ➞ False
- `is_valid_PIN("")` ➞ False

**Notes:**
- Some test cases contain special characters.
- Empty strings must return False.
