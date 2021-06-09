from typing import List


"""
    Q. 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때,
        유저가 ["오뎅", "콜라", "만두"] 를 주문했다.

        [현재 주문 가능한 상태인지 여부]를 반환하시오.


    Tip. 이진탐색 (Binary Search)을 사용한다. 
        - 이진탐색의 조건 : 정렬이 되어 있어야 한다.
        - 시간복잡도 : 파이썬에서는 정렬하는 기능중 .sort() 함수를 제공한다.
                     .sort() 함수의 시간 복잡도 : 정렬할 배열의 길이 O(N * logN)
                     이분탐색 함수를 호출할 때 마다 O(logN)
                     orders 길이만큼 이분탐색 함수를 호출하는 for문 사용시 O(M * logN)
                     
                     O((M + N) * logN) 만큼 걸리는 비효율적인 시간복잡도가 계산된다.
    
    
    Tip. set을 이용한다. (집합은 중복을 허용하지 않는다)
        - 시간복잡도 : menus를 중복이 허용되지 않는 set(집합)으로 만들기 위해 O(n)만큼 시간이 필요하고,
                     menu집합에 주문메뉴가 존재하는지 확인하기 위해 O(1)만큼 시간이 필요하고,
                     주문메뉴 개수 만큼 for문 사용시 O(m)만큼 시간이 소요된다.
                     
                     O(N) + O(M) = O(N + M) 만큼 시간복잡도가 걸리기 된다.
                     
"""

shop_menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", "dyson"]


def is_available_to_order(menus: List[str], orders: List[str]) -> bool:
    set_menus = set(menus)          # O(n)
    for order in orders:            # O(m)
        if order not in set_menus:  # O(1)
            return False
    return True


def is_available_to_order(menus: List[str], orders: List[str]) -> bool:
    binary_search()


def binary_search(target, array):
    min = 0
    max = len(array) - 1
    middle = min // max
    return False



print(is_available_to_order(shop_menus, shop_orders))

