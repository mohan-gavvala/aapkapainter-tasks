#Q2.Write a code that prints out individual scores of two players in a game of cricket where #score is given as runs per ball in an array. In a game of cricket a person changes #strike if he scores an odd number, and keeps strike with him if he scores an even #number. No need to consider changing strike after every 6 balls or an over.
#-----------------------------------------------------------------------------------
l=[1,2,3,2,1]
scores={'p1':[],'p2':[]}
def changeplayer(cp):
    if cp== scores["p1"]:
        return scores['p2']
    else:
        return scores['p1']
cp= scores['p1']
for i in l:
    if i%2==1:
        cp.append(i)
        cp=changeplayer(cp)
    if i%2==0:
        cp.append(i)
print(scores)
print('p1',sum(scores['p1']))
print('p2',sum(scores['p2']))       
#----------------------------------------------------------------------
#output
#{'p1': [1, 2, 1], 'p2': [2, 3]}
#p1 4
#p2 5