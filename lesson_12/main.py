# x = lambda x,y: x+y
# result=x(1,2)
#
# m_list = ['1','2','3','4','5']
# numbers = map(int, m_list)
# m_numbers =list(numbers)
#
#
# def double(x):
#     return x**2
#
# duble_numbers=map(double,m_numbers)
# duble_number2=map(lambda x: x**2, m_numbers)
#
# print(list(duble_number2))
# print(list(duble_numbers))
import time


# numbers=[x for x in range(1,10)]
# print(numbers)
#
# even = filter(
#     lambda number: number%2==0,
#     numbers)
# print(list(even))


# def decor(func):
#     def inner(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end=time.time()
#         print(f"Время работы функции {end-start}")
#         return result
#     return inner
#
# @decor
# def summ_x_y(x,y):
#     print("ZAGRUZKA")
#     time.sleep(5)
#     return x+y
#
# summ_x_y(5,5)


def test(*args):
    print(*args)
x = [1,2,3,4]
test(x)
test(*x)

def test_kwargs(**kwargs):
    print(kwargs)
test_kwargs(name="Name",last_name="Last Name")

print("NEW BRANCH")
<<<<<<< HEAD
# ЧТО ТОПИШУ

