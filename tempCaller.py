import rollerSkeleton

uIn = input()
while int(uIn) != 0:
    outPut = rollerSkeleton.rollCall(int(uIn))
    print(f"{outPut[0]} \nSuccesses: {outPut[1]}")
    if outPut[2]: print(f"Botched! (count: {outPut[2]})")
    uIn = input()

print("quitting")
quit
