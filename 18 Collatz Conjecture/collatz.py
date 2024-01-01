def collatz(*num):
    count = 0
    for x in num:
        while x != 1:
            if x%2== 0:
                x= x / 2
            elif x % 2 != 0:
                x = (x * 3)+1
            else:
                print("Invalid")
            count += 1
    return count

natural = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(list(map(collatz,natural)))