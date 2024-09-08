def outer_function():
    z = 30

    def inner_function():
        print(z)

    inner_function()

outer_function()
