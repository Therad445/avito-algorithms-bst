import sys


class Node:
    def __init__(self, x):
        self.x = x
        self.l = None
        self.r = None
        self.h = 1


def h(v):
    return v.h if v is not None else 0


def upd(v):
    v.h = max(h(v.l), h(v.r)) + 1


def left(v):
    t = v.r
    v.r = t.l
    t.l = v
    upd(v)
    upd(t)
    return t


def right(v):
    t = v.l
    v.l = t.r
    t.r = v
    upd(v)
    upd(t)
    return t


def fix(v):
    upd(v)
    b = h(v.r) - h(v.l)
    if b == 2:
        if h(v.r.l) > h(v.r.r):
            v.r = right(v.r)
        return left(v)
    if b == -2:
        if h(v.l.r) > h(v.l.l):
            v.l = left(v.l)
        return right(v)
    return v


def add(v, x):
    if v is None:
        return Node(x)
    if x < v.x:
        v.l = add(v.l, x)
    elif x > v.x:
        v.r = add(v.r, x)
    else:
        return v
    return fix(v)


def take_min(v):
    if v.l is None:
        return v.r, v.x
    v.l, x = take_min(v.l)
    return fix(v), x


def delete(v, x):
    if v is None:
        return None
    if x < v.x:
        v.l = delete(v.l, x)
    elif x > v.x:
        v.r = delete(v.r, x)
    else:
        if v.l is None:
            return v.r
        if v.r is None:
            return v.l
        v.r, v.x = take_min(v.r)
    return fix(v)


def exists(v, x):
    while v is not None:
        if v.x == x:
            return True
        v = v.l if x < v.x else v.r
    return False


def next_key(v, x):
    res = None
    while v is not None:
        if v.x >= x:
            res = v.x
            v = v.l
        else:
            v = v.r
    return res


def prev_key(v, x):
    res = None
    while v is not None:
        if v.x <= x:
            res = v.x
            v = v.r
        else:
            v = v.l
    return res


def walk(v):
    if v is None:
        return 'Empty'
    st = [v]
    a = []
    while st:
        t = st.pop()
        a.append(str(t.x))
        if t.r is not None:
            st.append(t.r)
        if t.l is not None:
            st.append(t.l)
    return ' '.join(a)


q = int(sys.stdin.readline())
root = None
out = []
for _ in range(q):
    a = sys.stdin.readline().split()
    op = a[0]
    if op == 'add':
        root = add(root, int(a[1]))
    elif op == 'del':
        root = delete(root, int(a[1]))
    elif op == 'exists':
        out.append('YES' if exists(root, int(a[1])) else 'NO')
    elif op == 'next':
        x = next_key(root, int(a[1]))
        out.append(str(x) if x is not None else 'None')
    elif op == 'prev':
        x = prev_key(root, int(a[1]))
        out.append(str(x) if x is not None else 'None')
    elif op == 'root':
        out.append(str(root.x) if root is not None else 'Empty')
    elif op == 'height':
        out.append(str(h(root)))
    else:
        out.append(walk(root))

sys.stdout.write('\n'.join(out) + ('\n' if out else ''))
