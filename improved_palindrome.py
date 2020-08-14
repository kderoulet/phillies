def is_palindrome(s):
    for x in range(0, len(s) // 2):
        if s[x] != s[-1 - x]:
            return False
    return True