"""
汽车油耗 12 km/l。输入行驶时间（小时）和平均速度（km/h），求消耗的燃料量（升）。
"""
t=int(input())
v=int(input())
sum=t*v/12
print(f"{sum:.3f}")