import json

def deep_diff(a, b, path="", diffs=None):
    if diffs is None:
        diffs = []

    # все ключи из обоих объектов
    keys = set(a.keys()) | set(b.keys())

    for key in keys:
        new_path = f"{path}.{key}" if path else key

        if key not in a:
            diffs.append(f"{new_path} : <missing> -> {json.dumps(b[key], separators=(',', ':'))}")

        elif key not in b:
            diffs.append(f"{new_path} : {json.dumps(a[key], separators=(',', ':'))} -> <missing>")

        else:
            va, vb = a[key], b[key]

            if isinstance(va, dict) and isinstance(vb, dict):
                deep_diff(va, vb, new_path, diffs)

            elif va != vb:
                diffs.append(
                    f"{new_path} : {json.dumps(va, separators=(',', ':'))} -> {json.dumps(vb, separators=(',', ':'))}"
                )

    return diffs


# input
obj1 = json.loads(input())
obj2 = json.loads(input())

# find differences
diffs = deep_diff(obj1, obj2)

# output
if not diffs:
    print("No differences")
else:
    for line in sorted(diffs):
        print(line)