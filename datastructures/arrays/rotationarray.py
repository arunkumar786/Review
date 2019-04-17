'''
Created on Apr 17, 2019

@author: root
'''
# let's see rotation of array.

def rotate(a,d,n):
    """
    @param a: array
    @param d: rotate by digist
    @param n: size of an array 
    """
    p = a[:d]
    temp = a[d:]
    return temp + p


rotated_array = rotate([1,2,3,4,5,6,7], 2, 5)

# print("rotated array is:", rotated_array)


# another method of solving this proble but this will of O(n^2)

def rotate_sec(a, d, n):
    """
    @param a: array
    @param d: rotate by digist
    @param n: size of an array 
    """
    temp = []; remaing_items = []
    for i in range(0,d):
        temp.append(i)
    for i in range(d,len(a)):
        remaing_items.append(i)
        
    return remaing_items + temp

rotated_sec_array = rotate([1,2,3,4,5,6,7], 2, 5)

print("rotated_sec array is:", rotated_sec_array)
        
        