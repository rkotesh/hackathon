num = input("Enter a number: ")
result = num + '5'
print("Result is:", result)

i = 0
while i < 5:
    print("Iteration:", i)
    i += 1
    
print("Done with iterations.")
# The above code concatenates '5' to the input string instead of adding numerically.

# To fix the code, we need to convert the input to an integer before adding 5.
num = int(input("Enter a number: "))
result = num + 5
print("Result is:", result)
