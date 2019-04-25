
forward = 0
backward = 0 
left = 0
right = 0

while True:
    
    direction = input("Which direction will you move") 
    string = ("l","r","f","b")
    
    print ("left " + str(left))
    print ("right " + str(right))
    print ("forward " + str(forward))
    print ("backward " + str(backward))     
    print ("center " + str(center))   
    
    
    
    if direction == "f" and forward <= 5:
        forward += 1
        backward -= 1
        print (forward)
        print ("You've taken a step forward")
        if direction in string and left == 0 and right == 0 and forward == 0 and backward == 0:
            print ("You are back where you started")
            continue
    if direction == "f" and forward >= 5:
        print ("You've run into a wall")
        if direction in string and left == 0 and right == 0 and forward == 0 and backward == 0:
            print ("You are back where you started")
            continue
    if direction == "l" and left < 6:
        left += 1
        right -= 1
        print (left)
        print ("You've taken a step to the left")
        if direction in string and left == 0 and right == 0 and forward == 0 and backward == 0:
            print ("You are back where you started")
            continue
    if direction == "r" and right < 6:
        right += 1
        left-=1
        print (right)
        print ("You've taken a step to the right")
        if direction in string and left == 0 and right == 0 and forward == 0 and backward == 0:
            print ("You are back where you started")
            continue

    if direction == "l" and left >= 5:
        print ("You've run into a wall")
        print(left)
        if direction in string and left == 0 and right == 0 and forward == 0 and backward == 0:
            print ("You are back where you started")
            continue
    if direction == "r" and right >= 5:
        print ("You've run into a wall")
        print(right)
        if direction in string and left == 0 and right == 0 and forward == 0 and backward == 0:
            print ("You are back where you started")
            continue
    if direction == "b" and backward < 5:
        backward += 1
        forward -= 1
        print (forward)
        print ("You've taken a step backward")
        if direction in string and left == 0 and right == 0 and forward == 0 and backward == 0:
            print ("You are back where you started")
            continue
    if direction == "b" and backward >= 5:
        print ("You've run into a wall")
        print(backward)
        if direction in string and left == 0 and right == 0 and forward == 0 and backward == 0:
            print ("You are back where you started")
            continue
        
    
   
    
    