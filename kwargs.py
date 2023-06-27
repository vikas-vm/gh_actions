def func1(*args, **kwargs):
    kwargs["five"] = 6
    print(kwargs["five"])
    # kwargs["dict1"]["a"] = 3
    # print("func1", kwargs["dict1"]["a"])


def func(a, *args, **kwargs):
    func1(*args, **kwargs)
    print(kwargs["five"])
    # print("func", kwargs["dict1"]["a"])



func(7, 1, 2, 3, five=5, name="John", age=22, dict1={"a": 1, "b": 2})