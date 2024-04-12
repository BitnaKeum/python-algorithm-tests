
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
  - 리스트에서 `pop(n)`
- O(nlogn)
  - 내장함수 sort(), sorted()
  - 병합 정렬, 퀵 정렬
- O(n^2)
  - 버블 정렬
- O(2^n)
- O(n!)


<hr>

<details>
<summary><b> 입력 받기</b></summary>

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
  data = sys.stdin.readline().rstrip()  # rstrip()은 개행문자를 제거하기 위함
  ```

  ```python
  import sys
  input = sys.stdin.readline
  data = input()
  ```

- +_효율적으로 출력하기_
    - 주의) `print()` 안에 정수를 넣으면 TypeError가 발생하므로 `str()`로 형변환 해줘야함
    ```python
    import sys
    print = sys.stdout.write
    print('내용')
    ```
</details>
<hr>



<details>
<summary><b> Python 기본 문법</b></summary>

- <b>자주 쓰는 함수</b>
    - `리스트.insert(idx, value)`

    - 재귀함수의 최대 호출 횟수 제한 늘리기 (default: 3000)
        ```python
        import sys
        sys.setrecursionlimit(10000)
        ```
    
    <br>

- <b>Slicing</b>
    - 리스트 슬라이싱 결과 값은 리스트형
    - 실제 범위를 벗어나도 에러가 발생하지 않음!
      ```python
      lis = [2,4,6,8]
      lis[3:10]  # [8]
      ```
<br>

- <b> List Comprehension </b>

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
    
<br>

- <b>리스트 → 문자열 </b>

  : 문자열이 들어 있는 리스트를 하나의 문자열로 합치기

    `''.join(리스트)`
    
<br>

- <b> 정렬하기 </b>

  - 리스트 정렬
  
    `리스트.sort()` : 리스트에 정렬된 값을 저장<br>
    `sorted(리스트)` : 리스트 값은 변하지 않고, 정렬된 값만 반환
    
    <br>
    
  - 문자열 정렬
  
    `sorted(문자열)` : 문자열 값은 변하지 않고, 정렬된 값만 리스트로 반환<br>
      
    <br>
    
  - `sort()`의 조건 지정하는 방법

      `lis = ["5e", "3a", "1a"]`일 때,
      
      1. 표현식 1개: 해당 표현식을 기준으로 정렬<br>
         `lis.sort(key=lambda x: x[1])    # ['3a', '1a', '5e']`
      
      2) 표현식 2개: 첫 번째 표현식을 우선으로 하고, 첫 번째 표현식이 같을 경우 두 번째 표현식에 따라 정렬<br>
        `lis.sort(key=lambda x: (x[1], x[0]))    # ['1a', '3a', '5e']`
         
<br>

- <b> 문자열이 알파벳/숫자인지 확인 </b>

  - 숫자로만 이루어져 있는지 확인: `문자열.isdecimal()`
    
  - 알파벳으로만 이루어져 있는지 확인: `문자열.isalpha()`
    
  - 숫자+알파벳으로 이루어져 있는지 확인: `문자열.isalnum()`
    
<br>

- <b>XOR 연산</b>
  
  : 값이 0이면 1로, 1이면 0으로 만들기

  - `^` 연산은 int형 변수에만 가능, '0111'과 같은 문자열에는 불가
  
    ```python
    num = 0
    print(num ^ 1)   # 1
    ```
    ```python
    num1 = 7    # 0111 (2진법)
    num2 = 8    # 1000 (2진법)
    print(num1 ^ num2)  # 15 (10진법) == 1111 (2진법)
    ```
    
<br>

- <b>Shift 연산</b>

  : bit를 한칸씩 밀기

    ```python
    num = 8 # 1000 (2진법)
    print(num >> 1) # 4 (10진법) == 0100 (2진법)
    print(num >> 2) # 2 (10진법) == 0010 (2진법)
    ```


</details><hr>


<details>
<summary><b> collections 모듈</b></summary>

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
      - 코드1) 중복 원소 제거
        ```python
        lis1 = ['a', 'b', 'b', 'c']
        lis2 = ['b', 'd']
        result = set(lis1) - set(lis2)  
        result = list(result) # ['a', 'c']
        ```
      - 코드2) 중복 원소 유지
        ```python
        from collections import Counter
        
        lis1 = ['a', 'b', 'b', 'c']
        lis2 = ['b', 'd']
        result = Counter(lis1) - Counter(lis2)    # Counter({'a': 1, 'b': 1, 'c': 1})
        ```

- `OrderedDict`
  - 딕셔너리의 입력 순서를 유지
  - Python 3.7 이상부터는 자동으로 입력 순서가 유지되지만, 혹시 모를 상황을 위해 사용하자.
  
    `collections.OrderedDict({'c': 1, 'a': 5, 'b': 4}) # 딕셔너리 형태 유지`
  

- `deque`
  - pop()을 자주 사용해야 할 때, 리스트 대신 deque를 이용하면 속도를 훨씬 높일 수 있다.
  - _리스트의 pop(0)은 O(n), deque의 popleft()는 O(1)_

    ```python
    from collections import deque
    
    queue = deque([1,3,5])
    
    queue.pop() # 맨 뒤 원소 pop
    queue.popleft() # 맨 앞 원소 pop, 리스트의 pop(0)과 동일한 역할
    
    queue.append(10) # 맨 뒤에 원소를 삽입
    queue.appendleft(10) # 맨 앞에 원소를 삽입
    ```

</details>
<hr>


<details>
<summary><b> 진법 변환하기 </b></summary>

- n진법 → 10진법 변환: `int(수 문자열, n)`
  
    ```python
    print(int('1000', 2))   # 8
    ```
    
<br>
    
- 10진법 → 2진법 변환: `bin()`

  ```python
  num = 8
  print(bin(num))      # '0b1000'
  print(bin(num)[2:])  # '1000
  ```

</details><hr>


<details>
<summary><b> 소수 찾기 </b></summary>

- 2부터 **제곱근**까지 나누어떨어지는지 확인하기

    ```python
    # 기본 코드
    def isPrime(num):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    ```
    ```python
    # 더 효율적인 코드
    def isPrime(num):
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    ```

- 에라토스테네스의 체
  
    : 주어진 범위의 값들 중 소수를 모두 찾아야할 때, 2부터의 배수들을 모두 제외시키는 방법

    ```python
    # 1부터 100까지의 수 중 소수를 출력하시오.
    
    n = 100
    primes = [True] * (n+1) # [0]는 사용안함
    primes[1] = False   # 1은 False 처리
    
    for i in range(2, int(n**0.5)+1): # 2 ~ √n
        # i의 배수들을 False 처리하기 (i 자신은 X)
        for idx in range(i+i, n+1, i):
            primes[idx] = False
    
    # 소수들을 출력
    for idx in range(1, n+1):
        if primes[idx]:
            print(idx)
    ```


</details><hr>


<details>
<summary><b> 약수 구하기 </b></summary>


  방법1: 해당 값(n)까지의 모든 값을 확인하기 _=> 비효율적_

  방법2: &radic;n까지의 모든 값 i를 확인하는데, 이 때 대응되는 n//i 값도 넣어준다 (제곱수인지 확인하고 넣기)
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

  - +) 약수의 개수가 홀수인지 짝수인지 구하기
    - 해당 값이 제곱수이면 약수의 개수는 홀수, 제곱수가 아니면 약수의 개수는 짝수
      - 제곱수 판별 : `if int(n**0.5) == n**0.5:`
  
</details><hr>


<details>
<summary><b> 이차원 배열 회전시키기</b></summary>

```python
def rotate(arr):    # arr는 이차원 배열
    row, col = len(arr), len(arr[0])
    rotated_arr = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            rotated_arr[j][row-1-i] = arr[i][j] # 핵심!
    return rotated_arr
```

</details><hr>


<details>
<summary><b> BFS / DFS </b></summary>

  - <b>DFS</b>
    
    : 현재 노드의 인접 노드 중 방문하지 않은 것을 모두 방문, 이 과정을 반복
    - **재귀함수** or Stack을 이용해 구현
    - 시간복잡도: O(V+E)
        - V는 노드 수, E는 간선 수
    
    ```python
    # 재귀함수로 구현한 코드
    
    def dfs(graph, node, visited):
        visited[node] = True
        print(node, end=' ')
    
        for adj_node in graph[node]:
            if not visited[adj_node]:
                dfs(graph, adj_node, visited)
    
    n = 5
    graph = [
        [],     # [0]은 사용하지 않음
        [2,3],
        [1,4,5],
        [1],
        [2,5],
        [2,4],
    ]
    visited = [False] * (n+1)   # [0]은 사용하지 않음
    dfs(graph, 1, visited)      # 시작 노드는 1
    # 출력: 1 2 4 5 3
    ```

<br>
      
  - <b>BFS</b>
    - Queue를 이용해 구현
 
</details><hr>


<details>
<summary><b> Queue</b></summary>

- FIFO (First In First Out)
- 일반적으로 `deque`를 사용해 구현
  - 삽입: `append()` (`appendleft()`도 있음)
  - 제거: `popleft()` (`pop()`도 있음)
    ```python
    from collections import deque
    
    queue = deque()
    queue.append(3)
    queue.append(1)
    queue.popleft() # 3
    ```
  

- <b>우선순위 큐 (Priority Queue)</b>
  
  : 단순히 먼저 들어온 값을 반환하지 않고, 저장된 값들을 **정렬**해서 가장 작은 값을 반환함

  - 일반적으로 `PriorityQueue`를 사용해 구현
    - 삽입: `put()`
    - 제거: `get()`
    - 오름차순 말고 다른 기준으로 반환하고 싶으면, `(우선순위, 값)` 튜플로 저장
      - ex: `(1, 'lemon')`
      - 우선순위가 동일한 튜플들은 값에 따라 정렬됨
    - 주의) `while queue:` 하면 항상 True이므로 `while queue.qsize() > 0:`으로 사용
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
  
  - `heapq`로도 구현 가능
      ```python
      import heapq
      
      heap = []
      heapq.heappush(heap, 3)
      heapq.heappush(heap, 1)
      heapq.heappop(heap)   # 1
      ```
      ```python
      import heapq
      
      heap = [3,5,1,4,2]
      heapq.heapify(heap)
      heapq.heappop(heap)   # 1
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
    
    - heap을 비우려면
      - `heap = []`로 리스트를 재생성해주면 됨 


</details><hr>


<details>
<summary><b> Tree</b></summary>

- **이진 트리**
    - 자식 노드의 수가 1개 또는 2개로 구성된 트리
    - 일반적으로 리스트로 구현
        - 루트 노드의 index는 1
        - index로 노드를 이동할 때
            - 루트 노드로 이동 => `index = 1`
            - 부모 노드로 이동 => `index = index / 2`
            - 왼쪽 자식 노드로 이동 => `index = index * 2`
            - 오른쪽 자식 노드로 이동 => `index = index * 2 + 1`

</details><hr>


<details>
<summary><b> 이진 탐색 (Binary Search)</b></summary>

  : start, mid, end를 사용하면서, mid의 값이 찾는 값과 일치하는지 확인을 반복하는 방법
  - 이진 탐색을 사용하려면 리스트가 **정렬**되어 있어야함!
  - 값의 갯수 or 범위가 엄청 클 때 많이 사용
  - 시간복잡도: O(logn)
  - **코딩테스트 자주 출제** 
    
  <br>

  - 코드1. 재귀로 구현
    ```python
    arr = [0,2,4,6,8]
    target = 4
    
    def binary_search(start, end):
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
        
    binary_search(0, len(arr)-1)  # 2
    ```
  - 코드2. 반복문으로 구현
    ```python
    arr = [0,2,4,6,8]
    target = 4
    
    def binary_search(start, end):
        while start <= end:
            mid = (start + end) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1 # 해당 값이 없는 경우
        
    binary_search(0, len(arr)-1)  # 2
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
            start += 1
            sum -= start
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


<details>
<summary><b> 정렬 알고리즘</b></summary>

1. <b>병합(merge) 정렬</b>

    : 리스트를 두 개의 부분집합으로 반복해 나누고, 이미 정렬된 부분집합들을 병합하며 정렬하는 방식

    - 재귀함수를 통해 리스트를 쪼갠 후, 투 포인터를 이용해 두 부분집합에서 작은 값부터 집어넣음
    - 시간복잡도: O(nlogn)
    - **코딩테스트에서 자주 등장**
    
    ```python
    arr = [3,5,4,1,2]
    
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
    
        # 리스트 쪼개기
        mid = len(arr) // 2
        left_arr = merge_sort(arr[:mid])
        right_arr = merge_sort(arr[mid:])
        
        # 투 포인터를 활용해 작은 값부터 집어넣음
        merged_arr = []
        l, r = 0, 0
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                merged_arr.append(left_arr[l])
                l += 1
            else:
                merged_arr.append(right_arr[r])
                r += 1
        # 남은 원소들 삽입
        if l < len(left_arr):
            merged_arr += left_arr[l:]
        else:
            merged_arr += right_arr[r:]
            
        return merged_arr
    ```

2. <b>버블(bubble) 정렬</b>

    : 인접 값끼리 비교해서 swap하며 정렬하는 방식
   
    - 시간복잡도: O(n^2)
    ```python
    arr = [3,5,4,1,2]
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:   # swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    ```

3. <b>삽입(insertion) 정렬</b>

    : 특정 값을 이미 정렬된 영역의 값들과 하나씩 비교해서 swap하면서 적절한 위치에 삽입하는 방식

    - i는 index 1부터 오른쪽으로, j는 index i부터 왼쪽으로 이동.
    - 시간복잡도: O(n^2)
    ```python
    arr = [3,5,4,1,2]
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:   # swap
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
    ```

4. <b>퀵(quick) 정렬</b>

    : pivot을 선정해 해당 값을 기준으로 대소비교하면서 정렬하는 방식

    - 재귀함수 이용
    - 시간복잡도: O(nlogn) _(로 알고 있으면 되고 최악의 경우 O(n^2)임)_
    
    ```python
    arr = [3,5,4,1,2]
    
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[0]  # 첫번째 원소를 pivot으로 설정
        small_arr = [x for x in arr[1:] if x <= pivot]
        large_arr = [x for x in arr[1:] if x > pivot]
        
        return quick_sort(small_arr) + [pivot] + quick_sort(large_arr)
    
    print(quick_sort(arr))  # [1,2,3,4,5]
    ```

5. <b>선택(selection) 정렬</b>

    : 남은 부분에서 최소값을 찾고 남은 부분의 맨 앞에 있는 데이터와 swap하며 정렬하는 방식 (최대값도 가능)

    - 시간복잡도: O(n^2)
    - 구현이 복잡하고 시간복잡도도 높아 코테에서 잘 사용하지 않음!

</details><hr>


<details>
<summary><b> 그리디(Greedy) 알고리즘</b></summary>

: 현재 상태에서 최선의 선택지가 전체에서 최선의 선택지라고 가정하는 알고리즘

- 수행 과정
    1. 현재 상태에서 최선의 해를 선택한다.
    2. 선택한 해가 전체 문제의 제약 조건에 벗어나지 않는지 확인한다.
    3. 현재까지 선택한 해의 집합이 전체 문제를 해결할 수 있는지 확인한다. <br>
       해결하지 못한다면 1번으로 돌아가 반복한다.
       
- 대표 문제: 최소 갯수의 동전을 사용해 주어진 금액 만들기

</details><hr>


<details>
<summary><b> 유니온 파인드 (union-find)</b></summary>

- union(a, b)
  - a 노드의 대표 노드와 b 노드의 대표 노드 중, 더 큰 대표 노드를 더 작은 대표 노드에 연결시킴
- find(a)
  - a 노드의 대표 노드를 반환
  - 재귀를 통해서 대표 노드를 찾음
  - 대표 노드를 찾은 후, 재귀를 빠져나오면서 거치는 모든 노드의 대표 노드를 업데이트함
    => 그래프를 정돈하고 시간 복잡도를 줄이는 역할을 함
    
- 구현 코드
    ```python
    parents = list(range(n + 1))    # 각 노드의 대표 노드를 의미
  
    def find(a):
        if a == parents[a]:  # 대표노드
            return a
        else:
            parent_a = find(parents[a])
            parents[a] = parent_a  # 대표노드 업데이트
            return parent_a
      
    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)
        
        if parent_a <= parent_b:
            parents[parent_b] = parent_a
        else:
            parents[parent_a] = parent_b
        # 아래처럼 작성하지 않게 주의!! 대표노드끼리 연결을 해야함
        # if a <= b:
        #     parents[b] = parent_a
        # else:
        #     parents[a] = parent_b
    ```

- 자주 실수하는 부분
    - find 연산에서, 재귀를 빠져나오면서 모든 노드의 대표 노드를 꼭 업데이트해야 함
    - union 연산에서, a와 b 노드끼리 연결하는 게 아니라 a와 b의 대표노드끼리 연결해야 함
    
</details><hr>


<details>
<summary><b> 위상 정렬</b></summary>

: 사이클이 없는 방향 그래프에서 **노드의 순서**를 찾는 알고리즘

- 정렬 결과가 유일하지는 않음
- 시간복잡도: O(V+E)


- 구현 방법
    1. 그래프와 별개로, 자기 자신을 가리키는 간선의 수를 의미하는 진입차수(in-degree) 리스트를 만듦
    2. 진입차수가 0인 노드들을 queue에 삽입
    3. queue에서 노드를 뽑고 (결과값에 저장)<br>
      해당 노드가 가리키는 노드들의 진입차수를 1 감소시킴<br>
      감소 후 진입차수가 0이 된 노드들을 queue에 삽입
    4. queue가 빌 때까지 3번 작업을 반복

    ```python
    from collections import deque
    
    n = 5
    graph = [
        [],     
        [2,3],  # node 1
        [4,5],  # node 2
        [4],    # node 3
        [5],    # node 4
        [],     # node 5
    ]
    
    # 1번 작업
    indegree = [0, 0, 1, 1, 2, 2]
    
    # 2번 작업
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
            
    while queue:
        # 3번 작업
        node = queue.popleft()
        print(node, end=' ')    # 결과 값 출력
        for next_node in graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)
    ```

</details><hr>


<details>
<summary><b> 다익스트라 (Dijkstra) 알고리즘</b></summary>

: 특정 노드에서 다른 모든 노드들까지의 **최단 거리**를 구할 때 사용

- 특징
  - 노드 간 거리가 주어지는 방향 그래프여야 함 
  - 거리는 모두 **양수**여야 함
- 시간복잡도: O(ElogV)


- 구현 방법
    1. (노드, 거리)를 인접 리스트에 저장해 그래프를 만든다.
    2. `distance` 리스트를 만들고, 출발 노드의 거리는 0, 다른 노드들의 거리는 INF로 초기화한다.
    3. 거리가 가장 작은 노드를 선택한다.
       - 이를 위해 **우선순위 큐**를 사용해야 함 (`PriorityQueue` / `heapq`)
       - 큐에 (거리, 노드) 순으로 저장해야 함
    4. 선택한 노드에 연결된 노드들에 대해 거리를 업데이트한다.
        - `distance[adj_node]`과 `dist + adj_dist` 중 더 작은 것
    5. 모든 노드가 선택될 때까지 3~4번을 반복한다.
    

- 코드1: `heapq`로 구현
    ```python
    import heapq
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        src_node, tgt_node, dist = map(int, input().split())
        graph[src_node].append((tgt_node, dist))
    
    INF = 10 ** 5
    distance = [INF] * (n + 1)
    
    # priority queue 만들기
    queue = []
    heapq.heappush(queue, (0, start))   # (거리, 노드) 순으로 저장
    distance[start] = 0
    
    # 다익스트라 알고리즘
    while queue:
        dist, node = heapq.heappop(queue)  # 가장 거리가 작은 노드 반환
        if dist > distance[node]:   # invalid
            continue
        for adj_node, adj_dist in graph[node]:
            if dist + adj_dist < distance[adj_node]:  # 최단 거리 업데이트
            # if distance[node] + adj_dist < distance[adj_node]:  # 이렇게 작성하지 않도록 주의!
                distance[adj_node] = dist + adj_dist
                heapq.heappush(queue, (distance[adj_node], adj_node))   # (거리, 노드) 순으로 저장
    ```
  
- 코드2: `PriorityQueue`로 구현
    ```python
    from queue import PriorityQueue
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        src_node, tgt_node, dist = map(int, input().split())
        graph[src_node].append((tgt_node, dist))
    
    INF = 10 ** 5
    distance = [INF] * (n + 1)
    
    # priority queue 만들기
    queue = PriorityQueue()
    queue.put((0, start))   # (거리, 노드) 순으로 저장
    distance[start] = 0
    
    # 다익스트라 알고리즘
    while queue.qsize() > 0:
        dist, node = queue.get()  # 가장 거리가 작은 노드 반환
        if dist > distance[node]:   # invalid
            continue
        for adj_node, adj_dist in graph[node]:
            if dist + adj_dist < distance[adj_node]:  # 최단 거리 업데이트
                distance[adj_node] = dist + adj_dist
                queue.put((distance[adj_node], adj_node))   # (거리, 노드) 순으로 저장
    ```
</details><hr>


<details>
<summary><b> 벨만-포드 (Bellman-ford) 알고리즘</b></summary>

: 특정 노드에서 다른 모든 노드들까지의 **최단 거리**를 구할 때 사용 (음수 거리가 있을 때!) 

- 특징
  - 노드 간 거리가 주어지는 방향 그래프여야 함 
  - 거리가 **음수**여도 됨
  - 노드가 n개일 때 엣지의 최대 갯수는 (n-1)이므로 거리 업데이트를 (n-1)번 반복
- 시간복잡도: O(VE)
- 코딩테스트에서는 최단 거리 구하는 문제보다 음수 사이클을 판별하는 문제가 더 많이 출제됨


- 구현 방법
    1. 그래프를 **엣지 리스트**로 구현한다.
       - 엣지 리스트의 각 인덱스마다 (노드1, 노드2, 가중치)가 저장됨
    2. `distance` 리스트를 만들고, 출발 노드의 거리는 0, 다른 노드들의 거리는 INF로 초기화한다.
    3. 거리 업데이트를 (n-1)번 반복한다.
        - `distance[src_node] == INF`일 때, 값을 업데이트하지 X
        - `distance[src_node] + weight < distance[tgt_node]`일 때, `distance[tgt_node]`를 업데이트 
    4. **음수 사이클**이 존재하는지 확인한다.
        - 모든 엣지를 한번씩 다시 사용해 업데이트된 노드가 있는지 확인
        - 업데이트가 일어났으면 음수 사이클이 존재하는 것 => 최단 거리 찾을 수 없음

    ```python
    # 그래프를 엣지 리스트로 구현
    graph = []
    for _ in range(m):
        src_node, tgt_node, dist = map(int, input().split())
        graph.append((src_node, tgt_node, dist))
        
    # distance 리스트 만들기
    INF = 10 ** 6
    distance = [INF] * (n+1)
    
    # start 노드
    start = 1
    distance[start] = 0
    
    # 벨만-포드 알고리즘
    for _ in range(n-1):    # (n-1)번 반복
        for (src_node, tgt_node, dist) in graph:
            if distance[src_node] != INF and distance[src_node] + dist < distance[tgt_node]:
                distance[tgt_node] = distance[src_node] + dist
    # 음수 사이클 판별
    neg_cycle = False
    for (src_node, tgt_node, dist) in graph:    # 1번 반복
        if distance[src_node] != INF and distance[src_node] + dist < distance[tgt_node]:
            # 업데이트가 일어나는 경우 (음수 사이클 존재)
            neg_cycle = True
            break
    ```

</details><hr>


<details>
<summary><b> 플로이드-워셜 (Floyd-warshall) 알고리즘</b></summary>

: 모든 노드 간에 **최단 거리**를 구할 때 사용

- 특징
    - 노드 간 거리가 주어지는 방향 그래프여야 함
    - 거리가 **음수**여도 됨
    - Dynamic Programming의 원리를 이용
        - A → B 로 가는 최단 경로를 구했을 때, 그 경로 위에 존재하는 C 노드에 대해 A → C, C → B 경로 역시 최단 경로임
- 시간복잡도: O(V^3)
    - 시간복잡도가 높기 때문에 노드 수는 적게 주어짐


- 구현 방법
    1. `distance` 리스트를 이차원으로 만들고, 자기 자신을 뜻하는 대각선 칸의 거리는 0, 다른 칸의 거리는 INF로 초기화한다.
    2. 그래프의 데이터를 `distance` 리스트에 저장한다.
    3. 3중 for문으로 **점화식**에 따라 거리를 업데이트한다. 
       - for문 순서: 경유 노드 K에 대해 → 출발 노드 S에 대해 → 도착 노드 E에 대해
       - 점화식: `distance[S][E] = min(distance[S][E], distance[S][K] + distance[K][E])`
        
    ```python
    # distance 리스트 만들기
    INF = 10 ** 6
    distance = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        distance[i][i] = 0
    
    # 그래프의 데이터를 distance 리스트에 저장하기
    for _ in range(m):
        s, e, dist = map(int, input().split())
        if distance[s][e] > dist:
            distance[s][e] = dist
    
    # 플로이드-워셜 알고리즘
    # 3중 for문으로 거리 업데이트
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if distance[i][j] > distance[i][k] + distance[k][j]:    # 점화식
                    distance[i][j] = distance[i][k] + distance[k][j]
    ```


</details><hr>


<details>
<summary><b> 최소 신장 트리 (minimum spanning tree)</b></summary>

: 그래프에서 **모든 노드를 연결**할 때 사용된 **에지들의 가중치 합을 최소**로 하는 트리

- 특징
    - 사이클이 생기지 않도록 연결함
    - 노드가 n개이면 최소 신장 트리를 구성하는 <b>에지는 항상 (n-1)개</b>
    - <b>유니온 파인드</b>를 활용해 구현


- 구현 방법
    1. 그래프를 **엣지 리스트**로 구현한다. 유니온 파인드 리스트도 초기화한다.
        - 엣지 리스트의 각 인덱스마다 (노드1, 노드2, 가중치)가 저장됨
    2. 엣지 리스트를 가중치 기준으로 정렬한다.
        - 이를 위해 엣지 리스트를 우선순위 큐로 구현
    3. 가중치가 낮은 엣지부터 순서대로 선택해, 사이클이 형성되지 않는지 확인 후 두 노드를 연결한다.
        - 사이클 형성 확인: find 연산
        - 두 노드를 연결: union 연산
    4. 연결된 엣지가 (n-1)개가 될 때까지 3번 작업을 반복한다.
    
    ```python
    from queue import PriorityQueue
    import sys
    input = sys.stdin.readline
    
    V, E = map(int, input().split())
    queue = PriorityQueue()
    for _ in range(E):
        node1, node2, weight = map(int, input().split())
        queue.put((weight, node1, node2))  # weight 기준으로 정렬
    parents = list(range(V + 1))
    
    
    def find(node):
        if node == parents[node]:
            return node
        else:
            parent_node = find(parents[node])
            parents[node] = parent_node
            return parent_node
    
    def union(node1, node2):
        node1_parent = find(node1)
        node2_parent = find(node2)
        if node1_parent <= node2_parent:
            parents[node2_parent] = node1_parent
        else:
            parents[node1_parent] = node2_parent
    
    
    weight_sum, edge_cnt = 0, 0
    while queue.qsize() > 0 and edge_cnt < V-1:
        weight, node1, node2 = queue.get()
    
        # 사이클 형성 여부 확인
        node1_parent, node2_parent = find(node1), find(node2)
        if node1_parent == node2_parent:  # 연결 X
            continue
    
        # 두 노드 연결
        union(node1, node2)
        weight_sum += weight
        edge_cnt += 1
    
    print(weight_sum)
    ```
</details><hr>


<details>
<summary><b> 세그먼트 트리 (Segment Tree)</b></summary>

: 데이터의 특정 **구간 합**과 **업데이트**를 빠르게 수행하기 위해 사용

- 세그먼트 트리의 종류: 구간 합, 최대값, 최소값



- 세그먼트 트리 만들기
    - 데이터가 $N$개일 때, $2^k >= N$ 을 만족하는 최소의 $k$를 구한 후, $2^{k+1}$ 크기의 트리 리스트를 만듦
    - 트리 리스트의 $2^k$ index부터 주어진 데이터 $N$개를 채움 (Leaf 노드)
    - 채워진 값을 이용해 부모 노드로 올라가면서 세그먼트 트리의 종류에 따라 값을 채움
        - 구간 합: tree[i] = tree[2i] + tree[2i+1]
        - 최대값: tree[i] = max(tree[2i], tree[2i+1])
        - 최소값: tree[i] = min(tree[2i], tree[2i+1])
    

- 구간 합/최대값/최소값 구하기
    - 주어진 질의 index를 세그먼트 트리의 Leaf 노드에 해당하는 index로 변경
        - 세그먼트 트리 index = 질의 index + ($2^k - 1$)
    - 다음의 과정을 거침
        1. `start_index % 2 == 1`이면 해당 노드를 선택해 연산 수행
            - `start_index += 1`
        2. `end_index % 2 == 0`이면 해당 노드를 선택해 연산 수행
            - `end_index -= 1`
        3. start_index의 depth 변경: `start_index = start_index // 2`
        4. end_index의 depth 변경: `end_index = end_index // 2`
        - a~d 작업을 반복하다가 `start_index > end_index`가 되면 종료
    

- 값 업데이트하기
    - 업데이트된 노드의 값과 부모가 같은 다른 자식 노드의 값에 대해 연산하고 계속해서 부모 노드로 올라감
    - 업데이트가 일어나지 않으면 종료
    - ex) 최대값 트리에서, 6번 노드의 값이 업데이트됨 → 6번과 7번 노드의 값 중 더 큰 값을 부모인 3번 노드에 업데이트 → 3번 노드와 2번 노드 값 비교해서 더 큰 값을 부모인 1번 노드에 업데이트


- 코드
    ```python
    # 2^k>=N 만족하는 k 구하기
    length = N
    k = 0
    while length != 0:
        length = length // 2
        k += 1
    # N: 5, k = 0
    # N: 2, k = 1
    # N: 1, k = 2
    # N: 0, k = 3
    
    # 2^(k+1) 크기의 리스트 만들기
    # 최소값 트리에서는 INF로 초기화, 구간합/최대값 트리에서는 0으로 초기화
    INF = 10 ** 6
    tree_size = 2 ** (k+1)
    tree = [INF] * (tree_size + 1)  # [0]은 사용 X
    
    # 2^k index부터 주어진 데이터 저장
    for i in range(2**k, 2**k + N):
        tree[i] = int(input())  # 데이터 입력
    
    # 부모 노드로 올라가면서 값 채우기
    i = tree_size
    while i != 1:   # 1이면 Root 노드이므로 종료
        if tree[i//2] > tree[i]:
            tree[i//2] = tree[i]
        i -= 1
        
  
    # a번째부터 b번째 값 중에서 최소값 구하기
    start, end = a + (2**k - 1), b + (2**k - 1) # 질의 index를 세그먼트 트리의 index로 변경
    selected_nums = []
    while start <= end:
        if start % 2 == 1:
            selected_nums.append(tree[start])
            start += 1
        if end % 2 == 0:
            selected_nums.append(tree[end])
            end -= 1
        start = start // 2
        end = end // 2
    
    answer = sum(selected_nums)
    answer = max(selected_nums)
    answer = min(selected_nums)
    ```

</details><hr>


<details>
<summary><b> 순열</b></summary>

- 라이브러리 활용 코드
    ```python
    from itertools import permutations
    
    li1 = [1,2,3,4]
    
    permutations(li1)       # 4!
    permutations(li1, r=2)  # 4P2
    ```
    - 결과로 객체를 반환하므로 list()를 씌워주자. 내부 값들은 튜플 형태이다.


- n개의 수로 순열을 만드는 상황에서, 다음을 이용하자. 
    - 1번째 자릿수가 정해졌다고 가정했을 때, 그 다음에 올 수 있는 경우의 수는 (n-1)!이다.
    - 2번째 자릿수가 정해졌다고 가정했을 때, 그 다음에 올 수 있는 경우의 수는 (n-2)!이다.
    - ...
    - [참고 블로그](https://kosaf04pyh.tistory.com/211)

</details><hr>


<details>
<summary><b> 동적 계획법 (Dynamic Programming)</b></summary>

: 복잡한 문제를 여러 개의 간단한 문제로 분리하고, 부분 문제들을 해결함으로써 최종적인 문제의 답을 구하는 방법

- 큰 문제를 작은 문제로 나눌 수 있어야함
- 작은 문제들이 반복적으로 나타나고 사용되며, 이 결과값은 항상 같아야함
- 모든 작은 문제의 결과값은 한번만 계산하여 DP 테이블에 저장 (Memoization)
- Top-down 방식 또는 Bottom-up 방식으로 구현할 수 있음
    - Top-down 방식: 주로 재귀함수 사용
    - Bottom-up 방식: 주로 반복문 사용
- 동적 계획법으로 풀 수 있다고 판단했으면 점화식 세우기


- 대표적인 문제
    - 피보나치 수열
    - LCS (Longest Common Subsequence)
        - [백준 9252번 문제](https://www.acmicpc.net/problem/9252)
    - 타일 채우기
        - [백준 11726번 문제](https://www.acmicpc.net/problem/11726)

</details>