number = 459


def get_sum(some_number: int):
    
    a = 0
    for i in str(some_number):
        a += int(i)
    print(a)

get_sum(number)
