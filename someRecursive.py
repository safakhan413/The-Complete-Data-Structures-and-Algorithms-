def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
    if len(arr) == 1:
        return cb(arr[0])
    elif(   int(cb(arr[-1]) or someRecursive(arr[:-1],cb)) == 1):
        return True 
    else:
        return False
print(someRecursive([1,2,3,4], isOdd))