def​ ​fun_gcd(m,n):
​ ​​ ​​ ​​ ​while​ ​n!=0:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​m,​ ​n​ ​=​ ​n,​ ​m%n
​ ​​ ​​ ​​ ​return​ ​m
def​ ​fun_lcm(m,n):
​ ​​ ​​ ​​ ​return​ ​int((m*n)//fun_gcd(m,n))
def​ ​fraction_add(a,b):
​ ​​ ​​ ​​ ​den​ ​=​ ​fun_lcm(a[1],b[1])
​ ​​ ​​ ​​ ​num​ ​=​ ​a[0]*int(den//a[1])​ ​+​ ​b[0]*int(den//b[1])
​ ​​ ​​ ​​ ​return​ ​[num,den]
def​ ​fraction_sub(a,b):
​ ​​ ​​ ​​ ​den​ ​=​ ​fun_lcm(a[1],b[1])
​ ​​ ​​ ​​ ​num​ ​=​ ​a[0]*int(den//a[1])​ ​-​ ​b[0]*int(den//b[1])
​ ​​ ​​ ​​ ​return​ ​[num,den]
def​ ​fraction_mul(a,b):
​ ​​ ​​ ​​ ​num,​ ​den​ ​=​ ​a[0]*b[0],​ ​a[1]*b[1]
​ ​​ ​​ ​​ ​common​ ​=​ ​fun_gcd(num,den)
​ ​​ ​​ ​​ ​num,​ ​den​ ​=​ ​int(num//common),​ ​int(den//common)
​ ​​ ​​ ​​ ​return​ ​[num,den]
def​ ​fraction_div(a,b):
​ ​​ ​​ ​​ ​num,​ ​den​ ​=​ ​a[0]*b[1],​ ​a[1]*b[0]
​ ​​ ​​ ​​ ​common​ ​=​ ​fun_gcd(num,den)
​ ​​ ​​ ​​ ​num,​ ​den​ ​=​ ​int(num//common),​ ​int(den//common)
​ ​​ ​​ ​​ ​return​ ​[num,den]
def​ ​gauss_eli(a):
​ ​​ ​​ ​​ ​#​ ​a​ ​is​ ​a​ ​n​ ​X​ ​n+1​ ​matrix
​ ​​ ​​ ​​ ​n​ ​=​ ​len(a)
​ ​​ ​​ ​​ ​x​ ​=​ ​[[0,1]]*n
​ ​​ ​​ ​​ ​for​ ​i​ ​in​ ​range(n):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​for​ ​j​ ​in​ ​range(i+1,​ ​n):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​ratio​ ​=​ ​fraction_div(a[j][i],a[i][i])
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​for​ ​k​ ​in​ ​range(n+1):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​a[j][k]​ ​=​ ​fraction_sub(a[j][k],​ ​fraction_mul(ratio,​ ​a[i][k]))
​ ​​ ​​ ​​ ​x[n-1]​ ​=​ ​fraction_div(a[n-1][n],a[n-1][n-1])
​ ​​ ​​ ​​ ​for​ ​i​ ​in​ ​range(n-2,-1,-1):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​x[i]​ ​=​ ​a[i][n]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​for​ ​j​ ​in​ ​range(i+1,n):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​x[i]​ ​=​ ​fraction_sub(x[i],​ ​fraction_mul(a[i][j],x[j]))
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​x[i]​ ​=​ ​fraction_div(x[i],a[i][i])
​ ​​ ​​ ​​ ​return​ ​x
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​
def​ ​solution(markov_tr):
​ ​​ ​​ ​​ ​stable​ ​=​ ​[]
​ ​​ ​​ ​​ ​looping​ ​=​ ​[]
​ ​​ ​​ ​​ ​for​ ​i​ ​in​ ​range(len(markov_tr)):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​sum(markov_tr[i]):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​looping.append(i)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​else:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​stable.append(i)
​ ​​ ​​ ​​ ​if​ ​not​ ​sum(markov_tr[0]):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​answer​ ​=​ ​[0]*len(stable)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​answer[0]​ ​=​ ​1
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​answer.append(1)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​answer
​ ​​ ​​ ​​ ​hp_num​ ​=​ ​[]​ ​#hitting​ ​probablility​ ​of​ ​s0​ ​(numerator)
​ ​​ ​​ ​​ ​hp_den​ ​=​ ​[]​ ​#hitting​ ​probablility​ ​of​ ​s0​ ​(denominator)
​ ​​ ​​ ​​ ​common_den​ ​=​ ​1
​ ​​ ​​ ​​ ​for​ ​k​ ​in​ ​stable:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​a​ ​=​ ​[]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​for​ ​i​ ​in​ ​range(len(looping)):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​b​ ​=​ ​[]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​for​ ​j​ ​in​ ​range(len(looping)+1):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​b.append([0,1])
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​a.append(b)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​ia​ ​=​ ​0
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​for​ ​i​ ​in​ ​looping:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​den​ ​=​ ​sum(markov_tr[i])
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​ja​ ​=​ ​0
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​for​ ​j​ ​in​ ​looping:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​a[ia][ja][0]​ ​=​ ​-markov_tr[i][j]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​a[ia][ja][1]​ ​=​ ​den
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​i==j:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​a[ia][ja]​ ​=​ ​fraction_add(a[ia][ja],[1,1])
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​ja​ ​+=​ ​1
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​a[ia][-1][0]​ ​=​ ​markov_tr[i][k]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​a[ia][-1][1]​ ​=​ ​den
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​ia​ ​+=​ ​1
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​x​ ​=​ ​gauss_eli(a)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​hp_num.append(x[0][0])
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​hp_den.append(x[0][1])
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​common_den​ ​=​ ​fun_lcm(common_den,x[0][1])
​ ​​ ​​ ​​ ​answer​ ​=​ ​[]
​ ​​ ​​ ​​ ​for​ ​i​ ​in​ ​range(len(hp_num)):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​answer.append(hp_num[i]*int(common_den//hp_den[i]))
​ ​​ ​​ ​​ ​answer.append(common_den)
​ ​​ ​​ ​​ ​return​ ​answer