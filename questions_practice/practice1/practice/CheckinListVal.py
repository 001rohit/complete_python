# Write a Python program that checks whether a specified value is contained within a group of values.
def is_group_member(lst,n):
    for i in lst:
        if n==i:
            return True
        
    return False

print(is_group_member([1,2,3,4,5],3))