def calc(*args):
    for el in args:
        print(el)



calc(1, 2 ,34, 5, 6, 7, 8)


def calc2(**kwargs):
    print(kwargs["a"])
    print(kwargs["b"])
    print(kwargs["c"])


calc2(a=1, b=2, c=3)