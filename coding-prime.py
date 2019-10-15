import math
import time

def is_prime_number1(num):
  if num == 1:
    return False
  elif num == 2:
    return True
  for i in range(2, num):
    if num%i == 0:
      return False
  return True

def is_prime_number2(num):
  if num == 1:
    return False
  elif num == 2:
    return True
  for i in range(2, int(math.sqrt(num))+1):
    if num%i == 0:
      return False
  return True

def is_prime_number3(num, prime_number_list):
  if num == 1:
    return False
  elif num == 2:
    return True
  for i in prime_number_list:
    if i > math.sqrt(num):
      return True
    if num%i == 0:
      return False
  return True

if __name__ == "__main__":
  max_num = int(input("Enter max num for prime number> "))

  prime_number_list = []
  start_time = time.time()
  for i in range(1, max_num+1):
    if is_prime_number1(i):
      prime_number_list.append(i)

  end_time = time.time()
  print("elaspsed time1:", end_time - start_time)
  print("prime_number count:", len(prime_number_list))

  prime_number_list = []
  start_time = time.time()
  for i in range(1, max_num+1):
    if is_prime_number2(i):
      prime_number_list.append(i)

  end_time = time.time()
  print("elaspsed time2:", end_time - start_time)
  print("prime_number count:", len(prime_number_list))

  prime_number_list = []
  start_time = time.time()
  for i in range(1, max_num+1):
    if is_prime_number3(i, prime_number_list):
      prime_number_list.append(i)

  end_time = time.time()
  print("elaspsed time3:", end_time - start_time)
  print("prime_number count:", len(prime_number_list))
  # print(prime_number_list)