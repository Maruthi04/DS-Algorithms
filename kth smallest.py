# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:59:45 2020

@author: Maruthi Srinivas
"""
def kthsmallest(arr,l,r,k):
    if k>0 and k<=r-l+1:
        n=r-l+1
        i=0
        median=[]
        while i<n//5:
            #find out the median of each group of 5 elements
             median.append(findmedian(arr,l+i*5,5))
             i+=1
        if i*5<n:
            #finf the median of the group which is less than 5
            median.append(findmedian(arr,l+i*5,n%5))
            i+=1
        if i==1:
            #if median length is 1 then return that element
            medofmed=median[i-1]
        else:
            #else go for the kth smallest again which is median of medians
            medofmed=kthsmallest(median,0,i-1,i//2)
        #now find out the actual position of the medain element in the array using the partitio 
            #algorithm
        pos=position(arr,l,r,medofmed)
        if pos-l==k-1:
            return arr[pos]
        if pos-l>k-1:
            #if you have crossed the key then search the left sub arrray
            return kthsmallest(arr,l,pos-1,k)
        #else go for the right part
        return kthsmallest(arr,pos+1,r,k-pos+l-1)
    return 999999
def findmedian(arr,l,n):
    lis=[]
    for i in range(l,l+n):
        lis.append(arr[i])
    lis.sort()
    return lis[n//2]
def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
def position(arr,l,r,x):
    for i in range(l,r):
        if x==arr[i]:
            swap(arr,i,r)
            break
    x=arr[r]
    i=l
    for j in range(l,r):
        if arr[j]<x:
            swap(arr,i,j)
            i+=1
    swap(arr,i,r)
    return i
arr=[7,6,5,8,9,2,1]
# arr=[12, 3, 5, 7, 4, 19, 26] 
print(kthsmallest(arr,0,len(arr)-1,3))
        