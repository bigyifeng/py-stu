import pickle
import json

# pickle-----------------
# 将对象从内存写入磁盘
obj = dict(name="zs", age=18)
f = open("./file/test1.txt", "wb")
pickle.dump(obj, f)
f.close()

# 将磁盘数据转换为内存对象
r_f = open("./file/test1.txt", "rb")
r_obj = pickle.load(r_f)
print(r_obj)

# json-----------------
# 将对象从内存写入磁盘
obj = dict(name="zs", age=18)
f = open("./file/test1.txt", "wb")
json_str = json.dumps(obj)
f.close()
print(json_str)

# 将磁盘数据转换为内存对象
r_f = open("./file/test1.txt", "rb")
f.close()
r_obj = json.loads(json_str)
print(r_obj)


obj = dict(name="小明", age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)
ensure_ascii = True
# {"name": "\u5c0f\u660e", "age": 20}
ensure_ascii = False
# {"name": "小明", "age": 20}
