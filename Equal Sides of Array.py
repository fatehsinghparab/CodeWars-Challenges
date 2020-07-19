def find_even_index(arr):
    for i in range(len(arr)):
        try:
            lft_arr =sum(arr[0:i] )  
            rht_arr =sum(arr[i+1::])
            if ((lft_arr)==(rht_arr)):
                return i
                break
        except:
            continue
        if (i==(len(arr)-1)):
            return -1
