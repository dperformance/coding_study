"""
    버블정렬 (Bubble Sort)
    - 첫 번째와 두 번째 자료를 비교,
      두 번째와 세 번째 자료를 비교,
      ...
      마지막-1 번째와 마지막 자료를 비교하여 교환하는 정렬방식이다.
      첫 번째 사이클이 완료되면 가장 큰 숫자가 맨 뒤로 이동 되었기 때문에
      다음 사이클을 수행할 때는 마지막은 제외 하면 된다.

    * tip
        - 다른 언어인 경우에는 swap을 할 때 buffer 변수를 생성하여 이용해야 하지만
          파이썬은 buffer 변수를 사용하지 않아도 된다.
          ex) java
              - int a = 2;
                int b = 3;
                int buffer = 0;
                buffer = a;
                a = b;

          ex) python
              - a = 3
                b = 4
                a,b = b, a


    array length = 5
    현재 인덱스와 다음 인덱스를 비교하기 때문에
    마지막 전까지 돌 수 있도록 range 설정한다.
    index > index + 1

    0 1 2 3
    0 1 2
    0 1
"""

# input = [4, 6, 2, 9, 1]
input = [1, 4, 2, 5, 9]


def bubble_sort(array):
    # 시간 복잡도
    # 2차 반복문이 나왔고 고정되어 있지 않은 array의 길이만큼 반복 하기 때문에
    # O(N2)이다.
    n = len(array) - 1
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


bubble_sort(input)
print(input)

"""
 array length = 5
 현재 인덱스와 다음 인덱스를 비교하기 때문에
 마지막 전까지 돌 수 있도록 range 설정한다.
 index > index + 1
 
 0 1 2 3
 0 1 2
 0 1
 
"""

