import pandas as pd
dataf = pd.DataFrame({'Marks':[1,2,3,4],'Fee':[33,44,55,66]})
dataf1 = pd.DataFrame({'Sub':['A','b','c','d'],'Div':[1,2,3,4]})
dataset = pd.concat([dataf, dataf1], axis= 1, join='inner')
print(dataset)













heights = [100, 2, 300, 10, 11, 1000]
largest_number = heights[0]
for number in heights:
    if number > largest_number:
        largest_number = number
        print(largest_number)
print(largest_number)

n = [75,33,55,222,6]
num = n[0]
for i in n:
    if i<num:
        num = i

print(num)

rev = [1,2,3,4]
print(max(rev))
print(rev[::-1])
rev.reverse()
print(rev)

def fun1(food):
    for i in food:
        print(i)

food = [1,66,77]
fun1(food)
