def main(s):
    if s[0]=="*":
        return "*"
    if s[1]=="*":
        return "*"
    if s[2]=="*":
        return "*"
    if s[3]=="*":
        return "*"
    if s[4]=="*":
        return "*"
    else:
        return False
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
print(main("re86D"))
        