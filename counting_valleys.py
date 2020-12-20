# I just copied this answer because i couldn't do it myself > <
# it counts the number of valleys

def countingValleys(path):
    # Write your code here
    level = valleys = 0
    for step in path:
        level += 1 if step == 'U' else -1

        if level == 0 and step == 'U':
            valleys += 1

    return valleys


print(countingValleys("UDDDUDUU"))