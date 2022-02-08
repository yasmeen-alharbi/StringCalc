

def Add(numbers: str) -> int:
    """
    Adds integers given as a string of comma-separated numbers
    :param numbers: a string are separated by a comma
    :return: Empty strings should return 0
    """
    # Stores all negative values.
    negatives = []
    # Stores all numbers as strings.
    nums = []
    # Standard delimiter.
    delim = ","
    # Calculation result.
    result = 0

    numbers = numbers.strip()  # Handle newline characters.

    if not numbers == "":  # Check for empty strings.

        if numbers[0:2] == '//':  # Handle multiple, custom, arbitrary length delimiters.

            # Ending index of delimiter, as specified by the format.
            delim_ind = numbers.find('\n')

            # List of all given delimiters.
            delim_chars = get_delimiters(numbers[2:delim_ind])

            # Get the list of string values after splitting by the given delimiters.
            nums = [x for x in split_by_delims(delim_chars, numbers[delim_ind + 1:])]

        else:  # If there are no customs delimiters.
            nums = [x for x in numbers.split(delim)]

        for x in nums:
            if not x == '':  # Handles input with only custom delimiters.
                if int(x) < 0:  # Handle negative numbers.
                    negatives.append(x)
                if int(x) <= 1000:  # Handle numbers larger than 1000.
                    result = result + int(x)

    if len(negatives) > 0:  # Throw exception for negative numbers.
        e = "Negatives not allowed. Negative number listed:"

        for x in negatives:  # List negative numbers.
            e = e + " " + x
        raise ValueError(e)

    return result


def get_delimiters(chars):
    """
    A helper for handling delimiters of arbitrary length.
    :param chars: A string representing all delimiter characters.
    :return: a list of the given delimiters, including ones of arbitrary length.
    """
    res = {}
    for c in chars:
        if c in res:  # If the delimiter is found again, then it is of arbitrary length.
            res[c] = res[c] + c  # Append it to the already existing delimiter.
        else:
            res[c] = c  # Otherwise, add it to the dictionary.

    return list(res.values())


def split_by_delims(chars, vals):
    """
    A helper for handling multiple delimiters.
    :param chars: a list of delimiters.
    :param vals: a string of numbers to be split by the given delimiters.
    :return: a list of numbers as strings.
    """
    res = ""
    for i in chars:
        # Split the values by the current delimiter
        res = vals.split(i)
        # Rejoin the values using a single space as a delimiter.
        vals = " ".join(res)

    return vals.split()
