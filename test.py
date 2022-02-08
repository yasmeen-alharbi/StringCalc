import calculator as c

# Required tests:

# Testing an empty string:
if not c.Add("") == 0:
    print("Error with empty strings! Expected 0, but got: " + str(c.Add("")))

# Testing basic addition of integers:
if not c.Add("1,2,5") == 8:
    print("Error with calculation! Expected 8, but got: " + str(c.Add("1,2,5")))

# Testing with new lines in the input:
if not c.Add("1\n,2,3") == 6:
    print("Error with handling new lines in input! Expected 6, but got: " + str(c.Add("1\n,2,3")))

# Testing with only a new line as input:
if not c.Add("\n") == 0:
    print("Error with handling new lines in input! Expected 0, but got: " + str(c.Add("\n")))

# Testing custom delimiter ";":
if not c.Add("//;\n1;3;4") == 8:
    print("Error parsing delimiters! Expected 8, but got: " + str(c.Add("//;\n1;3;4")))

# Testing custom delimiter "$":
if not c.Add("//$\n1$2$3") == 6:
    print("Error parsing delimiters! Expected 6, but got: " + str(c.Add("//$\n1$2$3")))

# Testing custom delimiter "@":
if not c.Add("//@\n2@3@8") == 13:
    print("Error parsing delimiters! Expected 13, but got: " + str(c.Add("//@\n2@3@8")))

# Testing input with only delimiters:
if not c.Add("//@\n@@") == 0:
    print("Error with handling no numbers! Expected 0, but got: " + str(c.Add("//@\n@@")))

# Testing addition with only negative integers:
try:
    c.Add("-2,-3")
    print("Error with handling negative integers! Expected exception.")
except ValueError:  # Catch expected exception.
    print("Expected exception.")

# Testing addition with both negative and positive integers:
try:
    c.Add("-2,4")
    print("Error with handling negative integers! Expected exception.")
except ValueError:  # Catch expected exception.
    print("Expected exception.")

# Testing input with a new line and a custom delimiter:
if not c.Add("//@\n14@5@\n8") == 27:
    print("Error handling input! Expected 27, but got: " + str(c.Add("//@\n14@5@\n8")))

# Testing input with a new line, custom delimiter, and a negative number:
try:
    c.Add("//@\n14@5@\n-8")
    print("Error with handling negative integers! Expected exception.")
except ValueError:  # Catch expected exception.
    print("Expected exception.")


# Bonus tests:

# Testing input with a number larger than 1000:
if not c.Add("2,1001") == 2:
    print("Error handling numbers larger than 1000! Expected 2, but got: " + str(c.Add("2,1001")))

# Testing input with a delimiter of arbitrary length:
if not c.Add("//***\n1***2***3") == 6:
    print("Error handling input with an arbitrary length delimiter! Expected 6, but got: " + str(c.Add("//***\n1***2"
                                                                                                       "***3")))

# Testing an input with multiple delimiters:
if not c.Add("//$,@\n1$2@3") == 6:
    print("Error handling input with multiple delimiters! Expected 6 but got: " + str(c.Add("//$,@\n1$2@3")))

# Testing an input with multiple delimiters of arbitrary length:
if not c.Add("//**$,\n1**2$4,5") == 12:
    print("Error handling input with multiple arbitrary length delimiters! Expected 12, but got: " + str(c.Add("//**$,\n1**2$4,5")))

