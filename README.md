
## 시간복잡도

- 시간제한 1초당 약 2천만번 연산

  
- O(1)
  - 딕셔너리(해시 테이블)에서 `in` 연산
  - 리스트/Queue에서 `pop()`
- O(logn)
  - 이진 탐색(Binary Search)
- O(n)
  - 투 포인터
  - 리스트에서 `in` 연산
  - 리스트에서 `pop(1)`
- O(nlogn)
  - 내장함수 sort(), sorted()
  - 병합 정렬, 퀵 정렬
- O(n^2)
  - 버블 정렬
- O(2^n)
- O(n!)


<hr>

<details>
<summary><b>입력 받기</b></summary>

- 정수 1개<br>
  `num = int(input())` <br>
- 정수 2개 이상<br>
  `num1, num2 = map(int, input().split())` <br>
- 심화 버전<br>

  ```python
  lis = list(map(int, input().split()))  
  # 1 2 3 4 5 -> [1, 2, 3, 4, 5]
  ```
  
  ```python
  lis = list(map(int, input()))
  # 12345 -> [1, 2, 3, 4, 5]
  ```
  
  ```python
  lis = input().split()  
  # a b c d e -> ['a', 'b', 'c', 'd', 'e']
  ```
  
  ```python
  lis = []
  for _ in range(row):  # 행 수
    lis.append(list(map(int, input().split())))
  # 1 2 3
  # 4 5 6
  # ->
  # [[1, 2, 3], [4, 5, 6]]
  ```
  
- 효율적으로 입력 받기<br>
  ```python
  # 여러 줄을 반복해서 입력받아야할 때, input()을 사용하면 시간초과 에러가 발생하므로 sys.stdin.readline()를 사용
  import sys
  input_data = sys.stdin.readline().rstrip()  # rstrip()은 개행문자를 제거하기 위함
  ```
</details>
<hr>



<details>
<summary><b>Slicing</b></summary>

- 리스트 슬라이싱 결과 값은 리스트형
- 실제 범위를 벗어나도 에러가 발생하지 않음!
  ```python
  lis = [2,4,6,8]
  lis[3:10]  # [8]
  ```

</details>
<hr>


<details>
<summary><b>collections</b></summary>

- `defaultdict`
  - default 값을 설정하여 딕셔너리를 생성
  - 어떤 조건을 만족하면 특정 key의 value를 증가시키는 경우 유용하게 사용
    ```python
    dic = collections.defaultdict(int)  # default 값 : 0
    dic['A'] += 1 # 원래대로라면 존재하지 않는 key 값이므로 에러가 발생하지만, {'A': 1}이 됨
    ```

- `Counter`
  1. 원소의 빈도 세기<br>
     `lis = ['a', 'b', 'b', 'c', 'b']`일 때,<br>
      - 기본 : `collections.Counter(lis)   # Counter({'b': 3, 'a': 1, 'c': 1})`<br>
      - 빈도 높은 순 (모두) : `collections.Counter(lis).most_common()   # [('b', 3), ('a', 1), ('c', 1)]`<br>
      - 빈도 높은 순 (상위 2개)  : `collections.Counter(lis).most_common(2)  # [('b', 3), ('a', 1)]`<br>
  
  2. 두 리스트 빼기 (차집합)
      - 코드1) 중복 원소 고려 X
        ```python
        lis1 = ['a', 'b', 'b', 'c']
        lis2 = ['c', 'd']
        result = set(lis1) - set(lis2)  
        result = list(result) # ['a']
        ```
      - 코드2) 중복 원소 고려 O
        ```python
        lis1 = ['a', 'b', 'b', 'c']
        lis2 = ['c', 'd']
        result = Counter(lis1) - Counter(lis2)    # Counter({'a': 1, 'b': 2})
        ```

- `OrderedDict`
  - 딕셔너리의 입력 순서를 유지
  - Python 3.7 이상부터는 자동으로 입력 순서가 유지되지만, 혹시 모를 상황을 위해 사용하자.
  
    `collections.OrderedDict({'c': 1, 'a': 5, 'b': 4}) # 딕셔너리 형태 유지`
  

- `deque`
  - 리스트에서 pop()을 많이 사용하는 경우, 리스트 대신 deque를 이용하면 속도를 훨씬 높일 수 있다.
  - _리스트의 pop(0)은 O(n), deque의 popleft()는 O(1)_

    ```python
    queue = collections.deque([1,3,5])
    
    queue.pop() # 맨 뒤 원소 pop
    queue.popleft() # 맨 앞 원소 pop, 리스트의 pop(0)과 동일한 역할
    
    queue.append(10) # 맨 뒤에 원소를 삽입
    queue.appendleft(10) # 맨 앞에 원소를 삽입
    ```

</details>
<hr>


<details>
<summary><b> 리스트 -> 문자열 </b></summary>

  - 문자열이 들어 있는 리스트를 하나의 문자열로 합칠 때 사용

  `''.join(리스트)`

</details>
<hr>

<details>
<summary><b> List Comprehension </b></summary>

  - 기본 사용법
    ```python
    arr = [1,2,3,4,5]
    result = [x for x in arr]  # [1,2,3,4,5]
    ```
  - if문 사용
    ```python
    arr = [1,2,3,4,5]
    result = [x for x in arr if x < 3]  # [1,2]
    ```
  - if ~ else문 사용
    ```python
    arr = [5,3,2,7,1]
    result = ['small' if x < 3 else 'big' for x in arr]  # ['big', 'big', 'small', 'big', 'small']
    ```
    
</details>
<hr>

<details>
<summary><b> 정렬하기 </b></summary>

  - 리스트 정렬
  
    `리스트.sort()` : 리스트에 정렬된 값을 저장<br>
    `sorted(리스트)` : 리스트 값은 변하지 않고, 정렬된 값만 반환<br>
  
  
  - 문자열 정렬
  
    `sorted(문자열)` : 문자열 값은 변하지 않고, 정렬된 값만 리스트로 반환<br>
    _+ 정렬된 리스트를 문자열로 바꾸려면? `''.join(리스트)`<br>_

</details><hr>


<details>
<summary><b> n진법 수를 10진법으로 변환하기 </b></summary>

  `int(수 문자열, n)`

  ex) `int('1010', 2)   # 10`

</details><hr>


<details>
<summary><b> 소수 찾기 </b></summary>

  - 제일 먼저 2로 나누어 떨어지는지 확인한 후,  3부터 2씩 건너뛰면서 확인한다 (for 효율성)

</details><hr>


<details>
<summary><b> 문자열이 알파벳/숫자인지 확인 </b></summary>

  - 숫자로만 이루어져 있는지 확인
  
    `문자열.isdecimal()`

    
  - 알파벳으로만 이루어져 있는지 확인
  
    `문자열.isalpha()`

    
  - 숫자+알파벳으로 이루어져 있는지 확인
  
    `문자열.isalnum()`

</details><hr>


<details>
<summary><b> sort()의 조건 지정하기 </b></summary>

  `lis = ["5e", "3a", "1a"]`일 때,
  
  1) 표현식 한 개
    
  -  해당 표현식을 기준으로 정렬한다.<br>
     `lis.sort(key=lambda x: x[1])    # ['3a', '1a', '5e']`
  
  2) 표현식 두 개
  - 첫 번째 표현식을 우선으로 하고, 첫 번째 표현식이 같을 경우 두 번째 표현식에 따라 정렬한다.<br>
    `lis.sort(key=lambda x: (x[1], x[0]))    # ['1a', '3a', '5e']`

</details><hr>


<details>
<summary><b> 약수 구하기 </b></summary>

  방법1. 해당 값(n)까지의 모든 값을 확인하기 _=> 비효율적_

  방법2. &radic;n까지의 모든 값 i를 확인하는데, 이 때 대응되는 n//i 값도 넣어준다 (제곱수인지 확인하고 넣기)
  ```python
  div_list = []
  for i in range(1, int(n**0.5)+1):
          if n % i == 0:    # i는 n의 약수
              div_list.append(i)
              if n // i != i:   # n//i는 n의 약수
                  div_list.append(n//i)
  div_list = sorted(div_list)   # 오름차순 정렬
  ```
  <br>

  - <b>약수의 개수가 홀수 or 짝수 ?</b>
    - 해당 값이 제곱수이면 약수의 개수는 홀수, 제곱수가 아니면 약수의 개수는 짝수
      - 제곱수 판별 : `if int(n**0.5) == n**0.5:`
  
</details><hr>


<details>
<summary><b> BFS/DFS </b></summary>

  - BFS
    - Queue 구조로 구현 (`deque` 주로 사용, `append()`/`popleft()`)
  - DFS
    - Stack 구조로 구현 (리스트 사용, `append()`/`pop()`) or 재귀함수로 구현
 
</details><hr>


<details>
<summary><b>Queue</b></summary>

- FIFO (First In First Out)
- 일반적으로 `deque`를 사용해 구현
  - 삽입: `append()` (`appendleft()`도 있음)
  - 제거: `popleft()` (`pop()`도 있음)
  

- <b>우선순위 큐 (Priority Queue)</b>
  - 저장된 값들을 **정렬**하고, 가장 작은 값을 반환하는 특징
  - 삽입: `put()`
  - 제거: `get()`
  - 오름차순 말고 다른 기준으로 반환하고 싶으면, `(우선순위, 값)` 튜플로 저장
    - ex: `(1, 'lemon')`
    - 우선순위가 동일한 튜플들은 값에 따라 정렬됨
    
  ```python
  from queue import PriorityQueue
  
  queue = PriorityQueue()
  
  queue.put(3)
  queue.put(1)
  queue.put(5)
  print(queue.get())  # 1
  print(queue.get())  # 3
  print(queue.get())  # 5
  ```
  
  ```python
  from queue import PriorityQueue
  
  queue = PriorityQueue()
  
  queue.put((2, 'apple'))
  queue.put((1, 'lemon'))
  queue.put((1, 'blueberry'))
  print(queue.get())  # (1, 'blueberry')
  print(queue.get())  # (1, 'lemon')
  print(queue.get())  # (2, 'apple')
  ```

</details><hr>


<details>
<summary><b> Heap </b></summary>

  - 최소값/최대값을 반복적으로 찾아야할 때 유용함
  - Heap은 완전이진트리이므로 높이가 logn => 모든 노드에 대해 연산을 해야하므로 시간복잡도는 O(nlogn)
  - pop 연산을 하면 루트 노드의 값이 반환됨 (min heap이면 최소값, max heap이면 최대값)
  - heapq 모듈은 min heap만을 지원함. max heap을 사용해야한다면 원소를 모두 음수로 만들어서 사용하면 됨.
  ```python
  import heapq
  
  # heap을 만들면서 원소를 하나씩 집어넣기
  heap = []
  heapq.heappush(heap, 1)
  heapq.heappush(heap, 2)
  heapq.heappop(heap)  # 1
  ```
  ```python
  import heapq
  
  # 리스트를 한번에 heap으로 만들기
  heap = [1, 2]
  heapq.heapify(heap)
  heapq.heappop(heap)  # 1
  ```

</details><hr>


<details>
<summary><b> Binary Search (이진 탐색)</b></summary>

  : start, mid, end를 사용하면서, mid의 값이 찾는 값과 일치하는지 확인을 반복하는 방법
  - 이진 탐색을 사용하려면 리스트가 **정렬**되어 있어야함!
  - 값의 갯수 or 범위가 엄청 클 때 많이 사용
  - 시간복잡도: O(logn)


  - 코드1. 재귀로 구현
    ```python
    arr = [0,2,4,6,8]
    target = 4
    
    def binary_search(arr, target, start, end):
        if start > end: # 해당 값이 없는 경우
            return -1
        
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            # end = mid - 1
            return binary_search(arr, target, start, mid-1)
        else:
            # start = mid +1
            return binary_search(arr, target, mid+1, end)
        
    binary_search(arr, target, 0, len(arr)-1)  # 2
    ```
  - 코드2. 반복문으로 구현
    ```python
    arr = [0,2,4,6,8]
    target = 4
    
    def binary_search(arr, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1 # 해당 값이 없는 경우
        
    binary_search(arr, target, 0, len(arr)-1)  # 2
    ```

</details><hr>


<details>
<summary><b> 투 포인터 </b></summary>

  : start 포인터와 end 포인터를 설정하고 값의 범위를 따져 포인터를 한칸씩 이동시킴
  
  - 시간복잡도: O(n)
  - 시간복잡도가 낮기 때문에, 주로 값의 범위가 크거나 갯수가 많을 때 사용함
  
  
  - 예제1. k를 연속된 수들의 합으로 나타낼 수 있는 경우의 수
    ```python
    start, end = 1, 1 # 자연수여야하므로 1로 할당
    sum = 1
    answer = 1    # k 하나로만 구성된 경우를 포함
    while end < k:
        if sum < k:
            end += 1
            sum += end
        elif sum == k:
            end += 1
            sum += end
            answer += 1
        else:
            sum -= start
            start += 1
    print(answer)
    ```
  - 예제2. k를 두 수의 합으로 나타낼 수 있는 경우의 수
    ```python
    numbers = [2, 6, 4, 1, 5, 3]
    numbers.sort()    # [1, 2, 3, 4, 5, 6]
    
    start, end = 0, len(numbers)-1
    answer = 0
    while start < end:
        if numbers[start] + numbers[end] > k:
            end -= 1
        elif numbers[start] + numbers[end] == k:
            answer += 1
            end -= 1
        else:
            start += 1
    print(answer)
    ```

</details><hr>