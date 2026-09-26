#把 5 个旅行目的地读进列表，体会 sorted() 和 reverse() 的区别：sorted() 返回排好序的新列表、原列表不变；reverse() 直接把原列表倒过来。按步骤输出。
place=input().split()
print(place)
print(sorted(place))
print(place)
print(sorted(place,reverse=True))
print(place)

(place.reverse())
print(place)
