def​ ​solution(l,​ ​t):
​ ​​ ​​ ​​ ​#​ ​Your​ ​code​ ​here
​ ​​ ​​ ​​ ​j,​ ​sij​ ​=​ ​0,​ ​l[0]
​ ​​ ​​ ​​ ​for​ ​i​ ​in​ ​range(len(l)):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​while​ ​sij<t​ ​and​ ​j<len(l)-1:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​j​ ​+=​ ​1
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​sij​ ​+=​ ​l[j]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​sij​ ​==​ ​t:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​[i,j]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​sij​ ​-=​ ​l[i]
​ ​​ ​​ ​​ ​return​ ​[-1,-1]