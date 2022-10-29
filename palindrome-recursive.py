

def reverse(strng):
    if len(strng) == 1:
        return strng
    else:
        return strng[-1] + reverse(strng[:-1])
def isPalindrome(strng):
    if strng == reverse(strng):
        return True 
    else:
        return False