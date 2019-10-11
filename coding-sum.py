# 1st
# C for style 
NUM_MAX = 100

sum = 0
i = 0
while(i < 100):
    i += 1
    sum += i

print("sum 1st: {}".format(sum))

# 2nd
# python style
sum = 0
for value in range(1, NUM_MAX+1):
    sum += value

print("sum 2nd: {}".format(sum))

# 3nd
# python list sum
sum = sum(range(1, NUM_MAX))
print("sum 3rd: {}".format(sum))

