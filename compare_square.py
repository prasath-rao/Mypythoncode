def compare(arr1 ,arr2):
    if arr1 is None or arr2 is None:
        return False
    #list comprehension saves time ,sorted dosent alter the variables permanently
    if sorted(arr1) == sorted([i**2 for i in arr2]) or sorted(arr2) == sorted([i**2 for i in arr1]):
        return True
    else:
        return False

