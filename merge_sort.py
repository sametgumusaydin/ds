def merge_sort(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2] #left array
        right=arr[len(arr)//2:]  #right array

        #recursion
        merge_sort(left)
        merge_sort(right)

        i=0  #left array index
        j=0  #right array index
        k=0  #merged array index

        while i<len(left)and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
arr=[20,60,90,50,10,30,40,5]
merge_sort(arr)
print(arr)