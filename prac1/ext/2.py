n = int(input())
existing = dict()
for _ in range(n):
    name = input().strip()
    if name in existing:
        i = existing[name]
        print(f"{name}{i}")
        existing[name] = i + 1
        existing[f"{name}{i}"] = 1
    else:
        print("OK")
        existing[name] = 1
