# with open('./data.json','r',encoding='utf-8') as f:
#     res = f.read()
#     print(res)


# {'r': 1, '4': 150, 'l': [1, 2, {'a': 1001}, 3, 'str'], 'o': {'r': 5, 'b': 7, 'c': 'bc', 's': '中文'}}
import json

dic = {}
with open('./data.json', 'r', encoding='utf-8') as f:
    res = json.load(f)
    for key, value in res.items():
        if type(value) == int:
            dic[key] = value
        elif type(value) == list:
            for value1 in value:
                if type(value1) == dict:
                    ret = dict(value1)
                    for key2, value2 in ret.items():
                        if type(value2) == int:
                            dic[key2] = value2
        elif type(value) == dict:
            for key3, value3 in value.items():
                if type(value3) == int:
                    dic[key3] = value3


lst = sorted(dic.items(), key=lambda x: x[1], reverse=True)
for key, value in lst:
    res = {key: value}
    with open('./p2.txt', 'a', encoding='utf-8') as f:
        json.dump(res, f)
