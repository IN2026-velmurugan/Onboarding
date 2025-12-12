number_1 = 5  # noqa: D100 - Missing docstring in public module (auto-generated noqa)


def function():  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    number_1 = 10
    number_2 = 15  # noqa: F841 - local variable 'number_2' is assigned to but never used (auto-generated noqa)
    print("Inside function, number_1 =", number_1)


print("Before function call, number_1 =", number_1)
function()
print("After function call, number_1 =", number_1)
try:
    print(
        "Trying to access number_2 outside function: ",
        number_2,  # noqa: F821 - undefined name 'number_2' (auto-generated noqa)
    )
except Exception as e:
    print("Error because the local scope cannot be accessed outside scope:", e)
