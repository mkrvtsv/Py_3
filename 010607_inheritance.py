'''
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
Или эквивалентно записи:
class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:
class B(A):
    pass

Класс A является предком класса B, если
    A = B;
    A - прямой предок B
    существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass
class C(B):
    pass
# A -- предок С

Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.
В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
В следующей строке содержится число q - количество запросов.
В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.

Sample Input:
4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output:
Yes
Yes
Yes
No'''

import re
from collections import deque

def readGraph():
    graph = {}
    for e in range (int(input())):
        path = re.split('\W+', input().strip())
        value = path.pop(0)
        if value not in graph: graph[value] = []
        for i in path:
            if i not in graph: graph[i] = [value,]
            else:
                if value not in graph[i]: graph[i].append(value)
    return graph

def bfs(graph, start, goal):
    if start == goal: return True
    queue = deque([start])
    parent = {}
    parent[start] = start
    while queue:
        currNode = queue.popleft()
        if currNode in graph:
            for neighbor in graph[currNode]:
                if neighbor == goal: return True
                if neighbor not in parent:
                    parent[neighbor] = currNode
                    queue.append(neighbor)
    return False

graph = readGraph()
#print(graph)

for element in range (int(input())):
    list = input().split()
    start = list[0]
    if len(list) == 2: end = list[1]
    else: end = 'Nan'
    if start in graph and (bfs(graph, start, end) or end == 'Nan'): print('Yes')
    else: print('No')

''' Tests    
12
G : F
A
B : A
C : A
D : B C
E : D
F : D
X
Y : X A
Z : X
V : Z Y
W : V
8
A G
A Z
A W
X W
X QWE
A X
X X
1 1
Y
N
Y
Y
N
N
Y
N
{'V': ['W'], 'Y': ['V'], 'A': ['B', 'C', 'Y'], 'B': ['D'], 'F': ['G'], 'C': ['D'], 'Z': ['V'], 'X': ['Y', 'Z'], 'D': ['E', 'F']}

10
classA : classB classC classD classG classH
classB : classC classE classG classH classK classL
classC : classE classD classH classK classL
classE : classD classF classK classL
classD : classG classH
classF : classK
classG : classF
classH : classL
classK : classH classL
classL
38
classK classD
classD classA
classG classD
classH classA
classE classE
classH classG
classE classL
classB classD
classD classL
classD classG
classD classE
classA classF
classA classC
classK classA
classA classH
classK classD
classH classB
classK classB
classD classL
classG classG
classA classH
classK classL
classG classE
classB classA
classC classK
classK classL
classC classL
classG classC
classD classD
classC classG
classE classA
classF classK
classB classG
classH classL
classL classF
classH classG
classD classA
classH classL
{'classE': ['classD', 'classF', 'classK', 'classL'], 'classH': ['classL'], 'classK': ['classH', 'classL'], 'classG': ['classF'], 'classC': ['classE', 'classD', 'classH', 'classK', 'classL'], 'classB': ['classC', 'classE', 'classG', 'classH', 'classK', 'classL'], 'classA': ['classB', 'classC', 'classD', 'classG', 'classH'], 'classF': ['classK'], 'classD': ['classG', 'classH'], 'classL': []}
Yes
Yes
Yes
Yes
Yes
Yes
No
No
No
No
Yes
No
No
Yes
No
Yes
Yes
Yes
No
Yes
No
No
Yes
Yes
No
No
No
Yes
Yes
No
Yes
No
No
No
Yes
Yes
Yes
No


15
G : F
A
B : A
C : A
D : B C
E : D
F : D
X
Y : X A
Z : X
V : Z Y
W : V
Q : P
Q : R
Q : S
9
A G
A Z
A W
X W
X QWE
A X
X X
1 1
Q

Yes
No
Yes
Yes
No
No
Yes
No
Yes
'''
