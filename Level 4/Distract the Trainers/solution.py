class​ ​CustomPriorityQueue:
​ ​​ ​​ ​​ ​​ ​​ ​
​ ​​ ​​ ​​ ​def​ ​__init__(self,​ ​MAX_LEN=100):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.H​ ​=​ ​[0]*MAX_LEN
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.original_index​ ​=​ ​[-1]*MAX_LEN​ ​#​ ​from​ ​h​ ​index​ ​to​ ​given​ ​index​ ​(insert​ ​order)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.h_index​ ​=​ ​[-1]*MAX_LEN​ ​#​ ​from​ ​insert​ ​order​ ​to​ ​h​ ​index
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.size​ ​=​ ​-1​ ​#​ ​maximum​ ​valid​ ​index
​ ​​ ​​ ​​ ​def​ ​parent(self,​ ​i)​ ​:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​(i-1)​ ​//​ ​2
​ ​​ ​​ ​​ ​def​ ​leftChild(self,​ ​i)​ ​:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​((2*i)​ ​+​ ​1)
​ ​​ ​​ ​​ ​def​ ​rightChild(self,​ ​i)​ ​:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​((2*i)​ ​+​ ​2)
​ ​​ ​​ ​​ ​def​ ​shiftUp(self,​ ​i)​ ​:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​while​ ​(i​ ​>​ ​0​ ​and​ ​self.H[self.parent(i)]​ ​>​ ​self.H[i])​ ​:​ ​#​ ​Min​ ​Prioriy
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.swap(self.parent(i),​ ​i)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​i​ ​=​ ​self.parent(i)
​ ​​ ​​ ​​ ​def​ ​shiftDown(self,​ ​i)​ ​:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​maxIndex​ ​=​ ​i
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​l​ ​=​ ​self.leftChild(i)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​(l​ ​<=​ ​self.size​ ​and​ ​self.H[l]​ ​<​ ​self.H[maxIndex])​ ​:​ ​#​ ​Min​ ​Prioriy
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​maxIndex​ ​=​ ​l
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​r​ ​=​ ​self.rightChild(i)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​(r​ ​<=​ ​self.size​ ​and​ ​self.H[r]​ ​<​ ​self.H[maxIndex])​ ​:​ ​#​ ​Min​ ​Prioriy
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​maxIndex​ ​=​ ​r
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​(i​ ​!=​ ​maxIndex):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.swap(i,​ ​maxIndex)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.shiftDown(maxIndex)
​ ​​ ​​ ​​ ​def​ ​insert(self,​ ​p)​ ​:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.size​ ​=​ ​self.size​ ​+​ ​1
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.H[self.size]​ ​=​ ​p
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.original_index[self.size]​ ​=​ ​self.size​ ​#​ ​maintaining​ ​index
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.h_index[self.size]​ ​=​ ​self.size
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.shiftUp(self.size)
​ ​​ ​​ ​​ ​def​ ​extractMin(self)​ ​:​ ​#​ ​Min​ ​Prioriy
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​result​ ​=​ ​[self.H[0],​ ​self.original_index[0]]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.H[0]​ ​=​ ​self.H[self.size]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.original_index[0]​ ​=​ ​self.original_index[self.size]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.h_index[self.original_index[0]]​ ​=​ ​0
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.size​ ​=​ ​self.size​ ​-​ ​1
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.shiftDown(0)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​result
​ ​​ ​​ ​​ ​def​ ​changePriority(self,i,p=None)​ ​:​ ​#​ ​decrease​ ​1​ ​by​ ​default
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​oldp​ ​=​ ​self.H[i]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​p==None:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​p​ ​=​ ​oldp​ ​-​ ​1
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.H[i]​ ​=​ ​p
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​(p​ ​<​ ​oldp)​ ​:​ ​#​ ​Min​ ​Prioriy
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.shiftUp(i)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​else​ ​:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.shiftDown(i)
​ ​​ ​​ ​​ ​def​ ​getMin(self)​ ​:​ ​#​ ​Min​ ​Prioriy
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​self.H[0]
​ ​​ ​​ ​​ ​def​ ​Remove(self,i)​ ​:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.H[i]​ ​=​ ​self.getMin()​ ​-​ ​1​ ​#​ ​Min​ ​Prioriy
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.shiftUp(i)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.extractMin()​ ​#​ ​Min​ ​Prioriy
​ ​​ ​​ ​​ ​def​ ​swap(self,​ ​i,​ ​j)​ ​:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​temp​ ​=​ ​self.H[i]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.H[i]​ ​=​ ​self.H[j]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.H[j]​ ​=​ ​temp
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​temp​ ​=​ ​self.original_index[i]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.original_index[i]​ ​=​ ​self.original_index[j]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.original_index[j]​ ​=​ ​temp
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.h_index[self.original_index[i]]​ ​=​ ​i
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​self.h_index[self.original_index[j]]​ ​=​ ​j

def​ ​isDesiredPair(a,​ ​b):
​ ​​ ​​ ​​ ​if​ ​a>b:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​a,​ ​b​ ​=​ ​b,​ ​a
​ ​​ ​​ ​​ ​if​ ​b%a​ ​>​ ​0:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​True
​ ​​ ​​ ​​ ​ratio​ ​=​ ​b//a
​ ​​ ​​ ​​ ​if​ ​ratio​ ​&​ ​(ratio+1)​ ​==​ ​0:​ ​#​ ​ratio+1​ ​power​ ​of​ ​two
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​False
​ ​​ ​​ ​​ ​else:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​return​ ​True

def​ ​solution(banana_list):
​ ​​ ​​ ​​ ​n​ ​=​ ​len(banana_list)
​ ​​ ​​ ​​ ​connection​ ​=​ ​[0]*n
​ ​​ ​​ ​​ ​pair​ ​=​ ​[[]​ ​for​ ​i​ ​in​ ​range(n)]

​ ​​ ​​ ​​ ​for​ ​i​ ​in​ ​range(n):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​for​ ​j​ ​in​ ​range(i+1,n):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​isDesiredPair(banana_list[i],​ ​banana_list[j]):
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​connection[i]​ ​+=​ ​1
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​connection[j]​ ​+=​ ​1
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​pair[i].append(j)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​pair[j].append(i)

​ ​​ ​​ ​​ ​q​ ​=​ ​CustomPriorityQueue()
​ ​​ ​​ ​​ ​for​ ​c​ ​in​ ​connection:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​q.insert(c)

​ ​​ ​​ ​​ ​busy_instruc​ ​=​ ​0
​ ​​ ​​ ​​ ​while​ ​q.size>0:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​cnt,​ ​i​ ​=​ ​q.extractMin()​ ​#​ ​cnt​ ​is​ ​number​ ​of​ ​connections
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​if​ ​cnt>0:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​partner​ ​=​ ​pair[i][0]
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​busy_instruc​ ​+=​ ​2
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​for​ ​j​ ​in​ ​pair[i]:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​q.changePriority(q.h_index[j])
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​pair[j].remove(i)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​for​ ​j​ ​in​ ​pair[partner]:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​q.changePriority(q.h_index[j])
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​pair[j].remove(partner)
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​q.Remove(q.h_index[partner])
​ ​​ ​​ ​​ ​return​ ​n​ ​-​ ​busy_instruc