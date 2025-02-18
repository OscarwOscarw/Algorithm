
# File:    smartsort.py
# Author:  John Longley
# Date:    October 2024

# Template file for Inf2-IADS (2024-25) Coursework 1, Part A:
# Implementation of hybrid Merge Sort / Insert Sort,
# with optimization for already sorted segments.


import peekqueue
from peekqueue import PeekQueue

# Global variables

comp = lambda x,y: x<=y   # comparison function used for sorting

insertSortThreshold = 10

sortedRunThreshold = 10


# TODO: Task 1. Hybrid Merge/Insert Sort

# In-place Insert Sort on A[m],...,A[n-1]:

#   insertSort(A,m,n)

def insertSort(A,m,n):
    
    if n <= m:
        return
    
    for i in range(m+1,n):
        num = A[i]
        j = i-1

        while j >= m and comp(num,A[j]):
            A[j+1] = A[j]           # if num2 < num1, sort
            j = j - 1               # move forward

        A[j+1] = num                # insert

# Merge C[m],...,C[p-1] and C[p],...,C[n-1] into D[m],...,D[n-1]

#   merge(C,D,m,p,n)

def merge(C, D, m, p, n):
    i, j, k = m, p, m

    while i < p and j < n:  # compare numbers
        if comp(C[i], C[j]):
            D[k] = C[i]
            i += 1
        else:
            D[k] = C[j]
            j += 1
        k += 1

    while i < p:  # fill rest num
        D[k] = C[i]
        i += 1
        k += 1

    while j < n:  # fill rest num
        D[k] = C[j]
        j += 1
        k += 1



# Merge Sort A[m],...,A[n-1] using just B[m],...,B[n-1] as workspace,
# deferring to Insert Sort if length <= insertSortThreshold

#   greenMergeSort(A,B,m,n)

def greenMergeSort(A,B,m,n):

    if n - m <= insertSortThreshold:    # if length is small use insertSort
        insertSort(A, m, n) 
        return

    B = [0] * (n - m)*2
    
    qua1 = m + (n-m)//4
    mid  = m + (n-m)//2
    qua2 = m + 3*(n-m)//4

    # four-way recursive splitting
    greenMergeSort(A,B,m,qua1)
    greenMergeSort(A,B,qua1,mid)
    greenMergeSort(A,B,mid,qua2)
    greenMergeSort(A,B,qua2,n)

    # merge after sorting
    merge(A, B, m, qua1, mid)
    merge(A, B, mid, qua2, n)
    merge(B, A, m, mid, n)

# Provided code:

def greenMergeSortAll(A):
    B = [None] * len(A)
    greenMergeSort(A,B,0,len(A))
    return A


# TODO: Task 2. Detecting already sorted runs.
        
# Build and return queue of sorted runs of length >= sortedRunThreshold
# Queue items are pairs (i,j) where A[i],...,A[j-1] is sorted

#   allSortedRuns(A)

def allSortedRuns(A):
    Q = PeekQueue()
    n = len(A)
    i = 0
    while i < n:
        start = i
        while i + 1 < n and comp(A[i],A[i+1]):  # check if sorted
            i = i + 1   # if sorted, check next num
        
        end = i + 1

        if end - start >= sortedRunThreshold:  # add (start , end) to Q
            Q.push((start, end))
 
        i += 1
        
    return Q




# Test whether A[i],...,A[j-1] is sorted according to information in Q

#   isWithinRun(Q,i,j)

def isWithinRun(Q,i,j):
    sortSet = peekqueue.queueToList(Q)     # take (start,end) group form Q
    for start, end in sortSet:             # check if (i,j) is covered in Q
        if start <= i and j <= end:
            return True
    
    return False


# Improvement on greenMergeSort taking advantage of sorted runs

#   smartMergeSort(A,B,Q,m,n)

def smartMergeSort(A,B,Q,m,n):
    if isWithinRun(Q,m,n):       # if (m,n) is sorted, return
        return

    greenMergeSort(A,B,m,n)      # if (m,n) is not sorted, sort it

# Provided code:

def smartMergeSortAll(A):
    B = [None] * len(A)
    Q = allSortedRuns(A)
    smartMergeSort(A,B,Q,0,len(A))
    return A


# TODO: Task 3. Asymptotic analysis of smartMergeSortAll

# 1. Justification of O(n lg n) bound.
#  Accroding to "Master Theorem" :
#  T(n) = aT(n/b) + Θ(n^k)      
#  in smartMergeSortAll, list was divided into 4 sub list each time
#  merge process each element in the array once, with no duplicate so its time complexity is O(n)
#  so T(n) = 4T(n/4) + Θ(n), k = 1
#  e = logb(a) = log4(4) = 1  -->  k = e = 1    
#  As k = e, so T(n) = Θ(n^1lgn) = Θ(n lg n) 
#  which means O(n lg n)

# 2. Runtime analysis for nearly-sorted inputs.
#   for nearly-sorted inputs, smartMergeSortAll will cheak weather num is sorted in every position
#   worst-case : when unsorted num is found after all over the list
#   As smartMergeSortAll will process each part of array only, so it will skip sorted part by "isWithinRun"
#   when unsorted word is found, only a bit sort and merge take place
#   So worst-case runtime for nearly-sorted inputs is O(n) in smartMergeSortAll
   


# Functions added for automarking purposes - please don't touch these!

def set_comp(f):
    global comp
    comp = f

def set_insertSortThreshold(n):
    global insertSortThreshold
    insertSortThreshold = n

def set_sortedRunThreshold(n):
    global sortedRunThreshold
    sortedRunThreshold = n

def set_insertSort(f):
    global insertSort
    insertSort = f

# End of file
