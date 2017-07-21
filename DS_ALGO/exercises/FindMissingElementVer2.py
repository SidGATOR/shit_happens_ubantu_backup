def finder(arr1,arr2):
    result = 0

    for num in arr1+arr2:
        result ^= num
        print result

    return result

arr1 = [x for x in range(11)]
arr2 = [1,2,3,4,5,6,8,9,10]
print(finder(arr1,arr2))
