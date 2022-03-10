def​ ​solution(x,​ ​y):
​ ​​ ​​ ​​ ​#​ ​Your​ ​code​ ​here
​ ​​ ​​ ​​ ​steps​ ​=​ ​0
​ ​​ ​​ ​​ ​x,​ ​y​ ​=​ ​int(x),​ ​int​ ​(y)
​ ​​ ​​ ​​ ​while​ ​x>1:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​steps​ ​+=​ ​int((y-x)//x)​ ​+​ ​1
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​x,​ ​y​ ​=​ ​(y-x)%x,​ ​x
​ ​​ ​​ ​​ ​if​ ​not​ ​x:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​"impossible"
​ ​​ ​​ ​​ ​return​ ​str(steps+y-1)