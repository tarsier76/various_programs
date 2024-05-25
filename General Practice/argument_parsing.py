def args_logger(*args, **kwargs):
    for arg in args:
        print(f"* {arg}")

    for kwarg in kwargs:
        print(f"* {kwargs[kwarg]}")

def test(*args, **kwargs):
    args_logger(*args, **kwargs)
    print("========================================")


def main():
    test(1, 2, date_str="01/01/2023")
    test(message="Hello World", to_delete="l")
    test(1, 2, 3, 4, 5)
    test("hi", True, name="Lane", age=28)


main()
