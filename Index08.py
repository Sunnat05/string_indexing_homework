def main(s):
    if s[0]=="*":
        return 0
    if s[1]=="*":
        return 1
    if s[2]=="*":
        return 2
    if s[3]=="*":
        return 3
    if s[4]=="*":
        return 4
    else:
        return False
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
print(main("r*86D"))
        