from collections import deque

def bfs(mat):
    def isValid(i, j):
        if min(i, j) < 0 or i >= len(mat) or j >= len(mat[0]):
            return False
        return True
    
    q = deque([(0, 0, 'r')])
    vis = set()
    vis.add((0, 0, 'r'))
    eng = set()

    while q:
        i, j, dirt = q.popleft()
        eng.add((i, j))
    
        if mat[i][j] == '.':
            if dirt == 'l' and isValid(i, j - 1) and (i, j - 1, dirt) not in vis:
                q.append((i, j - 1, dirt))
                vis.add(((i, j - 1, dirt)))
            elif dirt == 'r'and isValid(i, j + 1) and (i, j + 1, dirt) not in vis:
                q.append((i, j + 1, dirt))
                vis.add(((i, j + 1, dirt)))
            elif dirt == 'u' and isValid(i - 1, j) and (i - 1, j, dirt) not in vis:
                q.append((i - 1, j, dirt))
                vis.add(((i - 1, j, dirt)))
            elif dirt == 'd' and isValid(i + 1, j) and (i + 1, j, dirt) not in vis:
                q.append((i + 1, j, dirt))
                vis.add(((i + 1, j, dirt)))

        elif mat[i][j] == '-':
            if dirt == 'l' and isValid(i, j - 1) and (i, j - 1, dirt) not in vis:
                q.append((i, j - 1, dirt))
                vis.add(((i, j - 1, dirt)))
            elif dirt == 'r'and isValid(i, j + 1) and (i, j + 1, dirt) not in vis:
                q.append((i, j + 1, dirt))
                vis.add(((i, j + 1, dirt)))
            else:
                if isValid(i, j - 1) and (i, j - 1, 'l') not in vis:
                    q.append((i, j - 1, 'l'))
                    vis.add(((i, j - 1, 'l')))
                if isValid(i, j + 1) and (i, j + 1, 'r') not in vis:
                    q.append((i, j + 1, 'r'))
                    vis.add(((i, j + 1, 'r')))

        elif mat[i][j] == '|':
            if dirt == 'u' and isValid(i - 1, j) and (i - 1, j, dirt) not in vis:
                q.append((i - 1, j, dirt))
                vis.add(((i - 1, j, dirt)))
            elif dirt == 'd' and isValid(i + 1, j) and (i + 1, j, dirt) not in vis:
                q.append((i + 1, j, dirt))
                vis.add(((i + 1, j, dirt)))
            else:
                if isValid(i - 1, j) and (i - 1, j, 'u') not in vis:
                    q.append((i - 1, j, 'u'))
                    vis.add(((i - 1, j, 'u')))
                if isValid(i + 1, j) and (i + 1, j, 'd') not in vis:
                    q.append((i + 1, j, 'd'))
                    vis.add(((i + 1, j, 'd')))

        elif mat[i][j] == '/':
            if dirt == 'l' and isValid(i + 1, j) and (i + 1, j, 'd') not in vis:
                q.append((i + 1, j, 'd'))
                vis.add(((i + 1, j, 'd')))
            elif dirt == 'r' and isValid(i - 1, j) and (i - 1, j, 'u') not in vis:
                q.append((i - 1, j, 'u'))
                vis.add(((i - 1, j, 'u')))
            elif dirt == 'd' and isValid(i, j - 1) and (i, j - 1, 'l') not in vis:
                q.append((i, j - 1, 'l'))
                vis.add(((i, j - 1, 'l')))
            elif dirt == 'u' and isValid(i, j + 1) and (i, j + 1, 'r') not in vis:
                q.append((i, j + 1, 'r'))
                vis.add(((i, j + 1, 'r')))
        
        else:
            if dirt == 'l' and isValid(i - 1, j) and (i - 1, j, 'u') not in vis:
                q.append((i - 1, j, 'u'))
                vis.add(((i - 1, j, 'u')))
            elif dirt == 'r' and isValid(i + 1, j) and (i + 1, j, 'd') not in vis:
                q.append((i + 1, j, 'd'))
                vis.add(((i + 1, j, 'd')))
            elif dirt == 'd' and isValid(i, j + 1) and (i, j + 1, 'r') not in vis:
                q.append((i, j + 1, 'r'))
                vis.add(((i, j + 1, 'r')))
            elif dirt == 'u' and isValid(i, j - 1) and (i, j - 1, 'l') not in vis:
                q.append((i, j - 1, 'l'))
                vis.add(((i, j - 1, 'l')))

    return len(eng)

with open('input.txt') as file:
    mat = []
    for line in file:
        mat.append(list(line.strip()))
    
    print(bfs(mat))
