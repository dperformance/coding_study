from typing import List
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

c = ['ccc', 'aah', 'd', 'bb', 'ddddd', 'abcdefghijk']


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def sort(s: List[str]):
    def fn(s):
        print(s[0], s[-1])
        return s[0], s[-1]

    print("input                :", s)
    print("sorted(s)            :", sorted(s))
    print("sorted(s, key=len)   :", sorted(s, key=len))
    print("sorted(s, key=fn)    :", sorted(s, key=fn))
    print("lambda               :", sorted(s, key=lambda c: (c[0], c[-1])))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    sort(c)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
