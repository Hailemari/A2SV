class Solution:
    #Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        highest = i
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        
        if leftChild < n and arr[leftChild] > arr[highest]:
            highest = leftChild
        
        if rightChild < n and arr[rightChild] > arr[highest]:
            highest = rightChild
        
        if highest != i:
            arr[i], arr[highest] = arr[highest], arr[i]
            self.heapify(arr, n, highest)
            
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
            
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)