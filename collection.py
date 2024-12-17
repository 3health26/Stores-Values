# Variable which stores number of values
# 1 list[] edit, 2 tupple() cannot edit, 3 set{} not breakable, not index, not duplicate
# a= []
# print(type(a))
# a = [1, 2, 3]

# print(a[1])
# print(a[:3])

# b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]#left to right
# print(b[0])
# print(b[0:3])
# print(b[0:4:2])

b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]# to right
# print(b[-1:-4:-1])
# b.insert(3, 100)
# print(b)
# b.append(200)
# print(b)
# b.extend([21, 22, 23])
# print(b)
# b.remove(15)
# print(b)
# del b[6]
# print(b)
# b.pop(4)
# print(b)
# b[0]=100
# print(b)
# x=(1,2,3,4,5)
# print(x)
# print(x[0])
# print(x[0:3])
# print (x.count(1))
# print(x.index(2))
# d=x.copy()
# print(d)
# a=(1,2,3)
# l=list(a)
# l.append(4)
# a=tuple(l)
# print(a)
#set is collection of data but has no index {}. Duplicate value not add
# s={10,6,4,3,2,11,15,6,12,8}
# # print(s)
# s.add(13)
# s.pop()
# print(s)
# dictionary is collection of data and accept value in pair form. first is index called key and second is value
# d={1:"delhi", 2:"Mumbai"}
# print(d[1])
d2={"userid":"admin","password":12345, "age":27}
print(d2["userid"])
print(d2.get("age"))

l1= [1,2,3]
l2=["aa", "bb","cc"]
d3=dict(zip(l1,l2))
print(d3,d2)