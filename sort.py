niz = [5,6,2,1,12,41,52,61,70,18]

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

# po vrijednosti i po referenci
print(niz)


niz.sort()
print(niz)
