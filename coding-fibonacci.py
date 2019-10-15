# ref: https://devdoggo.netlify.com/post/alg_ds/challenges/fibonacci_solutions/
import time

def get_fibonacci1(num):
  if num < 2:
    return num
  return get_fibonacci1(num-1) + get_fibonacci1(num-2)

memo = {1:1, 2:1}
def get_fibonacci2(num):
  if num == 0:
    return 0
  if num not in memo:
    # print("not in", num)
    memo[num] = get_fibonacci2(num-1) + get_fibonacci2(num-2)
  # else:
  #   print("in", num)
  return memo[num]

def get_fibonacci3(num):
  a, b = 1, 0
  for i in range(num):
    a, b = b, a + b
  return b

if __name__ == "__main__":
  num = int(input("Enter number for fibonacci> "))

  start_time = time.time()
  fibonacci_number = get_fibonacci1(num)
  end_time = time.time()
  print("elaspsed time1:", end_time - start_time)
  print("fibonacci number:", fibonacci_number)

  start_time = time.time()
  fibonacci_number = get_fibonacci2(num)
  end_time = time.time()
  print("elaspsed time2:", end_time - start_time)
  print("fibonacci number:", fibonacci_number)
  # print(memo)

  start_time = time.time()
  fibonacci_number = get_fibonacci3(num)
  end_time = time.time()
  print("elaspsed time3:", end_time - start_time)
  print("fibonacci number:", fibonacci_number)
