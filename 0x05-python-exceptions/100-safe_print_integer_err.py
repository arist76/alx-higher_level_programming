def safe_print_integer_err(value):
    try:
        print("{:d}\n".format(value))
        return True
    except ValueError as e:
        print(e)
        return False
