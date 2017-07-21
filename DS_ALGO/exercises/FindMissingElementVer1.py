def finder(arr1,arr2):
    arr2 = sorted(arr2)

    ##Check if anything is missing
    if (len(arr1) == len(arr2)):
        return "Same"
    else:
        sum_arr1 = sum_arr2 = 0
        for num in arr1:
            sum_arr1 += num
        for num in arr2:
            sum_arr2 += num
        return sum_arr1-sum_arr2
arr1 = [x for x in range(1,8)]
arr2 = [3,4,2,1,6,7]
print(finder(arr1,arr2))
