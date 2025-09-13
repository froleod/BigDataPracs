access_map = {
    'read': 'r',
    'write': 'w',
    'execute': 'x'
}

n = int(input())
permissions = {}

for _ in range(n):
    parts = input().split()
    filename = parts[0]
    perms = set(parts[1:])
    permissions[filename] = perms

m = int(input())
for _ in range(m):
    action, filename = input().split()
    required = access_map[action]
    if required in permissions.get(filename, set()):
        print("OK")
    else:
        print("Access denied")
