
msg = "Python is an interpreted, high-level, general-purpose programming language.\n"
msg += "It was created by Guido van Rossum and first released in 1991.  "
msg += "Python's design philosophy emphasizes code readability with its notable use of significant whitespace.\n"
msg += "Its language constructs and object-oriented approach aims to help programmers write clear, logical code.\n"
msg += "Python can be used for small and large-scale projects.\n\n"
print(msg)

print("The variable msg was created by assigning the string value to it.")
print("Text stored in a variable is called a string.")
print("msg += combines the a new string with the existing string in msg.\n")

print("In python, you can add numbers: 2+3={}".format(2+3))
a = 2
b = 3
print("In python, you can add variables: {}+{}={}".format(a,b,a+b))

print("Variables are useful for math and loops")
print("the for loop lets you repeat a process many times")
for i in range(6): 
    print("for loop i={}".format(i))

print('If the if condition is true, the indented code is evaluated')
print("The modulo operator % returns the remainder 3%2={}".format(3%2))
for i in range(6): 
    if i%2==0:
        print("{} is even".format(i))
    else:
        print("{} is odd".format(i))


