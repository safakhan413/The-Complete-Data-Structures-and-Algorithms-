def capitalizeFirst(arr):
    if len(arr) == 1:
        return [arr[0].capitalize()]
    return [arr[0].capitalize()] + capitalizeFirst(arr[1:])

def capitalizeWords(arr):
    # TODO
    if len(arr) == 1:
        return [arr[0].upper()]
    return [arr[0].upper()] + capitalizeWords(arr[1:])