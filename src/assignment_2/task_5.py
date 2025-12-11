number_1 = 5


def function():
    number_1 = 10
    number_2 = 15
    print("Inside function, number_1 =", number_1)


print("Before function call, number_1 =", number_1)
function()
print("After function call, number_1 =", number_1)
try:
    print("Trying to access number_2 outside function:", number_2)
except Exception as e:
    print("Error because the local scope cannot be accessed outside scope:", e)
