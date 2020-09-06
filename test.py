import random
import time
import os
import sys

# Array of 10 000 integers to compare speed
nums = [i for i in range(1, 10001)]

# INSERTION SORT O(n^2)
def insertion_sort(a):
    for i in range(len(a)-1):
        if a[i+1]<a[i]:
            j=i
            while j>=0 and a[j+1]<a[j]:
                a[j], a[j+1] = a[j+1], a[j]
                j-=1

# SELECTION SORT O(n^2)
def selection_sort(a):
    sorted_index = 0
    for i in range(len(a)):
        mni = i
        for j in range(i+1, len(a)):
            if a[j]<a[mni]:
                mni = j
        a[mni], a[i] = a[i], a[mni]

# BUBBLE SORT O(n^2)
def bubble_sort(a):
    swap = True
    while swap:
        swap = False
        for i in range(len(a)-1):
            if a[i+1]<a[i]:
                swap = True
                a[i+1], a[i] = a[i], a[i+1]

# PANCAKE SORT O(n^2)
def pancake_sort(a):
    cur = len(a)
    while cur:
        mni = 0
        for i in range(cur):
            if a[i]>a[mni]:
                mni = i   

        pancake_flip(a, mni)
        pancake_flip(a, cur-1)
        cur-=1

def pancake_flip(a, ind):
    for i in range(ind):
        a[i], a[ind-i] = a[ind-i], a[i]

# COCKTAIL SORT O(n^2)
def cocktail_sort(a):
    swap = True
    while swap:
        swap = False
        for i in range(len(a)-1):
            if a[i+1]<a[i]:
                swap = True
                a[i+1], a[i] = a[i], a[i+1]
        if not swap:
            break
        for i in range(len(a)-1, 1, -1):
            if a[i]<a[i-1]:
                swap = True
                a[i], a[i-1] = a[i-1], a[i]

# QUICKSORT O(n*log(n))
def quicksort(a, l=0, r=None):
    if r is None:
        r = len(a)-1
    
    if l < r:
        p = partition(a,l,r)
        quicksort(a, l, p-1)
        quicksort(a, p+1, r)

# Helper function for quicksort
def partition(a, l, r):
    i = l-1
    pivot = a[r]
    for j in range(l,r):
        if a[j] < pivot:
            i += 1
            a[j], a[i] = a[i], a[j]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

# MERGE SORT O(n*log(n))
def merge_sort(a):
    if len(a) <= 1:
        return
    m = len(a)//2
    L = a[:m]
    R = a[m:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        a[k] = L[i]
        k += 1
        i += 1
    while j < len(R):
        a[k] = R[j]
        k += 1
        j += 1

# To print results in a text file
output_file = open("./tests.txt", "w")
sys.stdout = output_file

sorting_functions = {
    "insertion sort": insertion_sort,
    "selection sort": selection_sort,
    "bubble sort": bubble_sort,
    "pancake sort": pancake_sort,
    "cocktail sort": cocktail_sort,
    "quicksort": quicksort,
    "mergesort": merge_sort
}

for f in sorting_functions.keys():
    random.shuffle(nums)
    t0 = time.clock()
    sorting_functions[f](nums)
    t1 = time.clock()
    print(f+":",t1-t0)

output_file.close()