def pair_sum(arr,ele):
    pair_sum = 0
    index_i = []
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if (arr[i]+arr[j] == ele and i not in index_i and j not in index_i):
                pair_sum += 1
                #print (arr[i],arr[j])
                index_i += [i] + [j]
    return pair_sum
arr = [1,3,2,2,2,3]
print(pair_sum(arr,4))
