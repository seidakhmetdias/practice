import json
import re

data = json.loads(input())
q = int(input())

pattern = re.compile(r"""
    ([a-zA-Z_]\w*)   # имя ключа
    |\[(\d+)\]       # или индекс массива
""", re.VERBOSE)

for _ in range(q):
    query = input().strip()
    cur = data
    ok = True

    for key, idx in pattern.findall(query):
        try:
            if key:
                # доступ по ключу
                if isinstance(cur, dict) and key in cur:
                    cur = cur[key]
                else:
                    ok = False
                    break
            else:
                # доступ по индексу
                idx = int(idx)
                if isinstance(cur, list) and 0 <= idx < len(cur):
                    cur = cur[idx]
                else:
                    ok = False
                    break
        except:
            ok = False
            break

    if ok:
        print(json.dumps(cur, separators=(',', ':')))
    else:
        print("NOT_FOUND")