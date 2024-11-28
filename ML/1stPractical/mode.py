# from collections import Counter 

# arr=[1,2,3,4,5,4]
# n=len(arr)
# data=Counter(arr)
# get_mode=dict(data)
# mode=[k for k , v in get_mode.items() if v==max(list(data.values()))]
# if (len(mode)==n):
#     get_mode="No Mode Found"
# else:
#     get_mode="Mode is Are : "+','.join(map(str,mode))

# print(get_mode)



# from scipy import stats

# speed=[1,2,3,4,5,5]
# x=stats.mode(speed)
# print(x)

from scipy import stats 

speed=[12,32,34,53,64,76]
x=stats.mode(speed)
print(x)
