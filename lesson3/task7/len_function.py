phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
first_half = phrase[:int(len(phrase)/2)]
# We need to do type conversion as divide gives us a float and the slice/index expects
# an integer
print(first_half)
