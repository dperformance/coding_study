"""
    Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.

    [6] -> [7] -> [8] # 이런 링크드 리스트가 입력되었을 때,
                      # 끝에서 2번째 값은 7을 반환해야 합니다!
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # case 1
        # 1. node의 총 개수를 구한다.
        # 2. 총 개수에서 사용자가 입력한 k 만큼 뺀 node의 data를 return한다.

        length = 1
        cur = self.head

        # O(n)
        while cur.next is not None:
            cur = cur.next
            length += 1

        end_length = length - k
        cur = self.head
        if end_length < 0 or end_length == length:
            print('입력하신 인덱스보다 생성된 LinkedList의 길이가 짧습니다.')
            return False

        # O(n - k)
        for i in range(end_length):
            cur = cur.next
        return cur.data


    def get_kth_node_from_last_2(self, k):
        # case 2
        # 1. 투 포인터를 이용하여 첫 번째 포인터는 0부터 상승
        # 2. 두 번째 포인터는 사용자가 입력한 k 만큼 먼저 next 시키고 검색
        # 3. 마지막 Node에 두 번째 포인터가 도착하면 첫 번째 포인터 값을 return 해준다.

        if k == 0:
            return False

        start_cur = self.head
        end_cur = self.head

        # O(n)
        for i in range(k):
            end_cur = end_cur.next

        # O(n - k)
        while end_cur is not None:
            end_cur = end_cur.next
            start_cur = start_cur.next

        return start_cur.data


linked_list = LinkedList(1)
linked_list.append(5)
linked_list.append(8)
linked_list.append(5)
linked_list.append(4)
linked_list.append(2)
linked_list.append(9)
print(linked_list.get_kth_node_from_last(1))
print(linked_list.get_kth_node_from_last_2(0))
