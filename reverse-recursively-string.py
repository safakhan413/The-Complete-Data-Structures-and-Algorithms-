
def reverse(strng):
    if len(strng) == 1:
        return strng
    else:
        return strng[-1] + reverse(strng[:-1])

print(reverse('python')) # 'nohtyp')
