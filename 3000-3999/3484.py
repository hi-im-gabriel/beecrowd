class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if value < root.value:
        if root.left:
            insert(root.left, value)
        else:
            root.left = Node(value)
    else:
        if root.right:
            insert(root.right, value)
        else:
            root.right = Node(value)

def dfs(node, level, min_per_level):
    if not node:
        return
    if level not in min_per_level:
        min_per_level[level] = node.value
    else:
        min_per_level[level] = min(min_per_level[level], node.value)
    dfs(node.left, level + 1, min_per_level)
    dfs(node.right, level + 1, min_per_level)

N = int(input())
heights = list(map(int, input().split()))

root = Node(heights[0])
for h in heights[1:]:
    insert(root, h)

min_per_level = {}
dfs(root, 0, min_per_level)

for level in sorted(min_per_level):
    print(level, min_per_level[level])
