# Implementation of some basic sorting algorithms

#Bubble Sort O(n^2)  - swapping the adjacent elements if they are in the wrong order.
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j+1]< arr[j]:
                arr[j+1],arr[j]=arr[j],arr[j+1]  #swap
    return arr

#Selection Sort O(n^2) - finding the minimum element from the unsorted part and putting it at the beginning. 
def selection_sort(arr):
    for i in range(len(arr)):
        small = i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[small]):
                small=j
        arr[i],arr[small]=arr[small],arr[i]
    return arr

#Insertion Sort O(n^2) - good if the data is really small or it is almost sorted.
def insertion_sort(arr):
    for i in range(1,len(arr)):
        value = arr[i]
        j=i-1
        while j>=0 and arr[j]>value:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=value
    return arr


#Merge sort O(nlogn)
def merge(left,right):
    arr = []
    l=0
    r=0
    if len(left)==0:
        return right.copy()
    if len(right)==0:
        return left.copy()
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            arr.append(left[l])
            l+=1
        else:
            arr.append(right[r])
            r+=1
    arr+=left[l:]+right[r:] #Concatenate the remaining values
    return arr


def merge_sort(arr):
    if len(arr)==1:
        return arr
    left = arr[0:len(arr)//2]
    right = arr[len(arr)//2:len(arr)]
    return merge(merge_sort(left),merge_sort(right))



def main():
    arr = [99,44,6,2,1,5,63,87,283,4,0]
    bubble_arr = arr.copy()
    print(bubble_sort(bubble_arr))
    selection_arr = arr.copy()
    print(selection_sort(selection_arr))
    insertion_arr = arr.copy()
    print(insertion_sort(insertion_arr))
    merge_sort_arr = arr.copy()
    print(merge_sort(merge_sort_arr))


if __name__ == "__main__":
    main()