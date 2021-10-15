def linearSearch(array, key):
    count = 0
    for num in array:
        if num==key:
            return (f"The {key} number is found at {count} position")
        count = count+1
    return (f"The {key} is not in the array")

print(linearSearch([1,2,3,4,5,6], 3))
print(linearSearch([1,2,3,4,5,6], 9))
print(linearSearch([1,2,3,4,5,6], 2))