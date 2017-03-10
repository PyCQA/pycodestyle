# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)


# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)


# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# Hanging indents should add a level.
foo = long_function_name(
    var_one,
    var_two,
    var_three,
    var_four
)


# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)


# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)


if (value1 == 0 and value2 == 0 and
    value3 == 'valueX' and value4 == 'valueY' or
    value5 > value6):
    raise ValueError("test")
