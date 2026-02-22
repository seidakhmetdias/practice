import json

def apply_patch(source, patch):
    for k, v in patch.items():
        if v is None:
            source.pop(k, None)
        elif k in source and isinstance(source[k], dict) and isinstance(v, dict):
            apply_patch(source[k], v)
        else:
            source[k] = v
    return source

source = json.loads(input())
patch = json.loads(input())

print(json.dumps(
    apply_patch(source, patch),
    sort_keys=True,
    separators=(',', ':')
))