from​ ​math​ ​import​ ​floor,​ ​sqrt
def​ ​solution(area):
​ ​​ ​​ ​​ ​#​ ​Your​ ​code​ ​here
​ ​​ ​​ ​​ ​sol​ ​=​ ​[]
​ ​​ ​​ ​​ ​while​ ​area>0:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​l​ ​=​ ​int(floor(sqrt(area)))
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​a​ ​=​ ​l**2
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​n,​ ​area​ ​=​ ​int(area//a),​ ​area%a
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​sol.extend([a]*n)
​ ​​ ​​ ​​ ​return​ ​sol