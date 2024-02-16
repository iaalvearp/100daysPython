# Link to the reeborgs world stage 10
"https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Fsk_menu.json&name=Step%2010&url=worlds%2Fsk%2Fstep10.json"

# Angelas's solution with for loop
hurdles = 6
while hurdles > 0:
    jump()
    hurdles -= 1
    print(hurdles)

# My solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
jump()
jump()
jump()
jump()
jump()
jump()