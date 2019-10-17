# ref: https://devdoggo.netlify.com/post/alg_ds/challenges/fibonacci_solutions/
import time

def call_counter(func):
  def helper(x):
    helper.calls += 1
    return func(x)
  helper.calls = 0
  return helper

@call_counter
def fibonacci_calc(num):
  if num < 2:
    return num

  n1 = 1
  n2 = 1
  result = 0
  for i in range(3, num+1):
    result = n1 + n2
    n1, n2 = n2, result
  return result

@call_counter
def fibonacci_recursive(num):
  if num < 2:
    return num
  return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)

memo = {1:1, 2:1}
@call_counter
def fibonacci_recursive_memo(num):
  if num == 0:
    return 0
  if num not in memo:
    # print("not in", num)
    memo[num] = fibonacci_recursive_memo(num-1) + fibonacci_recursive_memo(num-2)
  # else:
  #   print("in", num)
  return memo[num]

@call_counter
def fibonacci_python(num):
  a, b = 1, 0
  for i in range(num):
    a, b = b, a + b
  return b

if __name__ == "__main__":
  num = int(input("Enter number for fibonacci> "))
  print()

  start_time = time.time()
  fibonacci_number = fibonacci_calc(num)
  end_time = time.time()
  print("function call count(calc):", fibonacci_calc.calls)
  print("elaspsed time(calc):", end_time - start_time)
  print("result:", fibonacci_number)
  print()

  start_time = time.time()
  fibonacci_number = fibonacci_recursive(num)
  end_time = time.time()
  print("function call count(recursive):", fibonacci_recursive.calls)
  print("elaspsed time(recursive):", end_time - start_time)
  print("result:", fibonacci_number)
  print()

  start_time = time.time()
  fibonacci_number = fibonacci_recursive_memo(num)
  end_time = time.time()
  print("function call count(memo):", fibonacci_recursive_memo.calls)
  print("elaspsed time(memo):", end_time - start_time)
  print("result:", fibonacci_number)
  # print(memo)
  print()

  start_time = time.time()
  fibonacci_number = fibonacci_python(num)
  end_time = time.time()
  print("function call count(python):", fibonacci_python.calls)
  print("elaspsed time(python):", end_time - start_time)
  print("result:", fibonacci_number)
