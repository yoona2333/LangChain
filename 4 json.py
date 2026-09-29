import json

d = {
    "name": "李",
    "age": 0,
    "gender": "男",
}
print(str(d))

print(json.dumps(d, ensure_ascii=False))  # 无转义 确保中文正常显示
print(type(json.dumps(d, ensure_ascii=False)))

l = [
    {
        "name": "李",
        "age": 0,
        "gender": "男",
    },
    {
        "name": "张",
        "age": 0,
        "gender": "女",
    }, {
        "name": "赵",
        "age": 0,
        "gender": "男",
    }
]
print(json.dumps(l, ensure_ascii=False))
json_array='[{"name": "李", "age": 0, "gender": "男"}, {"name": "张", "age": 0, "gender": "女"}, {"name": "赵", "age": 0, "gender": "男"}]'
print(type(json.loads(json_array)))
