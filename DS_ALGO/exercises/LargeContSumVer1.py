def large_cont_sum(arr):
    min_max = {}
    max_list = []
    for i in range(len(arr)):
        result = 0
        tmp_sum = arr[i]
        if i+1 == len(arr):
            max_list.append(arr[i])
        else:
            for j in range(i+1,len(arr)):
                tmp_sum += arr[j]
                if (result < tmp_sum):
                    result = tmp_sum
                    min_max[result] = {"min" : i,"max" : j}
                    max_list += [result]
    return sorted(max_list)[-1]

print (large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
