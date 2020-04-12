# Matt Parkers Puzzle

# Scrabble letters. How many different sets of letters add up to specified target value
# Note assumes value is 44 or greater!

TARGET = 46

NOPTS = [' ']
ONEPTS = ['A','E','I','O','U','L','N','S','T','R']
TWOPTS = ['D','G']
THREEPTS = ['B','C','M','P']
FOURPTS = ['F','H','V','W','Y']
FIVEPTS = ['K']
EIGHTPTS = ['J','X']
TENPTS = ['Q','Z']

letters = {0: NOPTS, 1: ONEPTS, 2: TWOPTS, 3: THREEPTS, 4: FOURPTS, 5: FIVEPTS, 8: EIGHTPTS, 10: TENPTS}

final = []

def orderhand (i,j,k,l,m,n,o):
    hand = []
    hand.append(i)
    hand.append(j)
    hand.append(k)
    hand.append(l)
    hand.append(m)
    hand.append(n)
    hand.append(o)
    hand.sort()
    return hand

def create_hand(hand):
    global letters
    global final
    count = 0
    for a in letters.get(hand[0]):
        for b in letters.get(hand[1]):
            for c in letters.get(hand[2]):
                # Check no duplicates
                ohand = orderhand(a,b,c,"J","X","Q","Z")
                if ohand not in final:
                    final.append(ohand)
                    count = count +1
    print (hand, count)
        
print ("Distinct SCRABBLE hands that total",TARGET)
count = 0
valid = []
# Must be two 8 and two 10 letters - therefore reduces number of combinations.
# Only one 5 and ignoring blanks reduces the combinations further
for i in range (0,5):
    for j in range (0,5):
        for k in range (1,6):
            total = i+j+k+8+8+10+10
            if total == TARGET:
                # Order hand in ascending order and remove duplicates
                hand = orderhand(i,j,k,8,8,10,10)
                if hand not in valid:
                    valid.append(hand)
                    count = count +1 

print ("Total number",count)
for v in valid:
    create_hand(v)

# Show all of the letters in each possible hand
count = 0
for f in final:
    print (f)
    count = count + 1
print ("Total number",count)
print ("End")
