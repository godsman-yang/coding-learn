# ref: 
import time

def call_counter(func):
  def helper(x):
    helper.calls += 1
    return func(x)
  helper.calls = 0
  return helper

@call_counter
def factorial_calc(num):
  result = 1
  for i in range(1, num+1):
    result *= i
  return result

@call_counter
def factorial_recursive(num):
  if num == 1:
    return 1
  return num * factorial_recursive(num-1)


if __name__ == "__main__":
  num = int(input("Enter number for factorial> "))
  print()

  start_time = time.time()
  result = factorial_calc(num)
  end_time = time.time()
  print("function call count(calc):", factorial_calc.calls)
  print("elaspsed time(calc):", end_time - start_time)
  print("result:", result)
  print()

  start_time = time.time()
  result = factorial_recursive(num)
  end_time = time.time()
  print("function call count(recursive):", factorial_recursive.calls)
  print("elaspsed time(recursive):", end_time - start_time)
  print("result:", result)
  print()