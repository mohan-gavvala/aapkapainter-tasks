#Q1.Write a code that prints out the first occurrence of a duplicate in a given array of integers
#Sample Input: [1,2,3,2,1]
#Output: 2
#--------------------------------------------------------------------------------------
#Q1.code
#--------------------------------------------------------------------------------------
def find_first_occureenceof_duplicate(numbers):
    numlist = list()#list() is indiacates empty list . 
    for i in range(len(numbers)):#range(len(numbers)) -->range(5)---->0 to 4
        if numbers[i] in numlist:
            return numbers[i]
        numlist.append(numbers[i])
    return "no duplicates found"

print(find_first_occureenceof_duplicate([1, 2, 3, 2,1]))
#---------------------------------------------------------------------
#output for this program
#2
#Flow of the code
#--------------------------------------------------------------------
 
 #first iteration i=0 -->numbers[0] is 1 . 1 is not in numlist. so line 4 is false control go to line 6 and 1 will added given list. numlist=[1] 
 #second  iteration i=1 -->numbers[1] is 2 . 2 is not in numlist. so line 4 is false control go to line 6 and 2 will added given list. numlist=[1,2]
 #Thired  iteration i=2 -->numbers[2] is 3 . 3 is not in numlist. so line 4 is false control go to line 6 and 3 will added given list.numlist=[1,2,3]
 #Fourth   iteration i=3 -->numbers[3] is 2 . 2 is  in numlist. so line 4 is True control go to line 5 and numbers[3] i.e 2 will be returened
 #If no duplicates found function returnd "no duplicates found"
 #________________________________________________________________________________________
 