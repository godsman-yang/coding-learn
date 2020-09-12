# coding-learn

코딩하면 생각나는 문제들 정리
* 1부터 100까지 더하기
* 피보나치 수열
  - python - 쉬운 알고리즘(40번째)
  ```
    vscode@fc2e241b2660:/workspaces/vscode-remote-try-python$ python fibonacci.py
    Enter number for fibonacci> 40

    function call count(calc): 1
    elaspsed time(calc): 3.504753112792969e-05
    result: 102334155

    function call count(recursive): 331160281
    elaspsed time(recursive): 219.4066867828369
    result: 102334155

    function call count(memo): 77
    elaspsed time(memo): 9.512901306152344e-05
    result: 102334155

    function call count(python): 1
    elaspsed time(python): 1.430511474609375e-05
    result: 102334155
  ```
  - golang - 빠른 속도(40번째)
  - 같은 알고리즘, 가장 빠른 방법, 도커내부에서 실행한 경우, 70배 정도 빠르다.
  ```
    vscode@322a7b0c3325:/workspaces/coding-learn$ go run coding-fibonacci.go
    Enter number for fibonacci> 40

    Function call count(clac): 1
    Elaspsed time(calc): 1µs
    Result: 102334155

    Function call count(recursive): 331160281
    Elaspsed time(recursive): 851.6896ms
    Result: 102334155

    Function call count(memo): 79
    Elaspsed time(memo): 46.1µs
    Result: 102334155

    Function call count(golang): 1
    Elaspsed time(golang): 200ns
    Result: 102334155
  ```
* 소수 구하기
* 파이썬 100+ 문제 - https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt



