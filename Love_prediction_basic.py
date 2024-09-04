def prediction_love(male, female):
    male = male.lower()
    female = female.lower()
    count = 0
    for words in range(ord('a'), ord('z')+1):
        if (chr(words) in male) and (chr(words) in female):
            count = count + 1

    if count == 0:
        result = "Nope dude, there is no chance at all, you will live with dogs and cats and die alone"
    elif count < 4:
        result = "Just friend, bruh, you will be in the infinity friendzone"
    else:
        result = "Congratulation you son of bitch, but don't feel so lucky because she will cheat on you"
    return result
print("Give the male's name and female's name")        
male = input()
female = input()
print('Your prediction is: ' + prediction_love(male, female))
