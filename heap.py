def heapify(arr, n, i):
   largest = i 
   l = 2 * i + 1 
   r = 2 * i + 2 
   # if left child exists
   if l < n and arr[i] < arr[l]:
      largest = l
   # if right child exits
   if r < n and arr[largest] < arr[r]:
      largest = r
   if largest != i:
      arr[i],arr[largest] = arr[largest],arr[i] 
      heapify(arr, n, largest)
def heapSort(arr):
   n = len(arr)
   # maxheap
   for i in range(n, -1, -1):
      heapify(arr, n, i)
   for i in range(n-1, 0, -1):
      arr[i], arr[0] = arr[0], arr[i] 
      heapify(arr, i, 0)
arr = list(map(int,input().split()))
heapSort(arr)
n = len(arr)
print ("Sorted array is")
for i in range(n):
   print (arr[i],end=" ")
