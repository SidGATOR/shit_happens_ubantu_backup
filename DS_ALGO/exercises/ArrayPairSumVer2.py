def pair_sum(arr,k):

    ## Check if the array has more than one element
    if (len(arr)) < 2:
        return False

    else:

        ## Making two sets to keep track of output and numbers seen
        seen = set()
        output = set()

        ## Other number required for the pair

        for i in arr:
            target = k- i

            if target not in seen:
                seen.add(target)
            else:
                output.add((min(target,i),max(target,i)))

        #return len(output)
        print ('\n'.join(map(str,list(output))))


arr = [1,2,3,2,2,3]
print(pair_sum(arr,4))
