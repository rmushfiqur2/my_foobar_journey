def​ ​forward(n,b):
​ ​​ ​​ ​​ ​small​ ​=​ ​sorted(n)
​ ​​ ​​ ​​ ​big​ ​=​ ​sorted(n,reverse=True)
​ ​​ ​​ ​​ ​d​ ​=​ ​['']​ ​*​ ​len(n)
​ ​​ ​​ ​​ ​carry​ ​=​ ​0
​ ​​ ​​ ​​ ​for​ ​i​ ​in​ ​range(len(n)-1,-1,-1):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​di​ ​=​ ​ord(big[i])-ord(small[i])-carry
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​carry​ ​=​ ​0
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​di<0:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​di​ ​+=​ ​b
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​carry​ ​=​ ​1
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​d[i]​ ​=​ ​chr(di+48)
​ ​​ ​​ ​​ ​return​ ​''.join(d)
def​ ​solution(n,​ ​b):
​ ​​ ​​ ​​ ​#Your​ ​code​ ​here
​ ​​ ​​ ​​ ​current​ ​=​ ​n
​ ​​ ​​ ​​ ​prev​ ​=​ ​[n]
​ ​​ ​​ ​​ ​while​ ​True:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​current​ ​=​ ​forward(current,b)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​for​ ​i​ ​in​ ​range(1,len(prev)+1):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​current​ ​==​ ​prev[-i]:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​i
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​prev.append(current)