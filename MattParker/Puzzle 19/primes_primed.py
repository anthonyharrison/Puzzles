# MPMP #19

# Open file containing list of primes, each prime is on a single line
fh = open("primes.txt")
primes = fh.readlines()
fh.close()
print ("There are",len(primes),"primes. Last prime is",primes[-1])

# Try NUM=2 for original puzzle
NUM = 99
counts = [0] * NUM
found = [0] * NUM

# Remember Python counts from 0!
for n in range (len(primes)):
    for count in range (len(counts)):
        # First power to consider is 2
        power = count + 2
        counts[count] = counts[count] + int(primes[n]) ** power
        # Is the sum now divisble by the number of primes
        if (counts[count] % (n+1) == 0):
            # Ignore the special case of a single prime
            if n > 0:
                #print ("FOUND -",power, n+1, counts[count], counts[count] % (n+1), primes[n])
                print ("POWER",power, "COUNT", n+1, " LARGEST PRIME", primes[n])
                found[count] = found[count] + 1

# Now print out the number of instances found for each power
for i in range (len(found)):
    print ("POWER",i+2,"NUMBER",found[i])

# End
