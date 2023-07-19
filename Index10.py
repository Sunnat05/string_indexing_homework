def main(s):
    a=0
    if s[0] in "0123456789":
        a+=int(s(0))
    if s[1] in "0123456789":
        a+=int(s[1])
    if s[2] in "0987654321":
        a+=int(s[2])
    if s[3] in "1234567890":
        a+=int(s[3])
    if s[4] in "1234567890":
        a+=int(s[4])
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    return a
print(main("dfw45"))