#Q3:Write a code that checks if two given strings are anagrams
#Sample Input: Mary Army
#Output: Yes
#--------------------------------------------------------------------------
def Anagram(s):
    #print(s)#['Army', 'Mary']
    if(len(str(s[0])) == len(str(s[1]))):
        for x in str(s[0]):
            if x.lower() not in str(s[1]).lower():
                return 'False'
        return 'Yes'
    return 'Two strings having diffrent length'
print(Anagram(s=input("Sample Input:").split(" ")) )   
#-------------------------------------------------------------------------------
#0utput
#Sample Input:Army Mary
#Yes
#------------------------------------------------------------------
#Explanation:
#First line 12 exicuted we enterd string  Army Mary  based on space it splited two parts
#split() function return type is list i.e ['Army', 'Mary']
#check length of both strings same or not 
#listments conveted into string by using typecasting function str()
#using for loop iterate first string and and check each charcter present second string
#here ignore the case sensitive
