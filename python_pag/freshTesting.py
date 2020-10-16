# print(lambda x,y:x+y,[1,2,3])
# print(eval("123"))
# def toNum(nums,targer):
#     for i in range(len(nums)):
#         if num in nums[i+1:]:
#             return [i,nums.index(num,i+1)]

# print([x for x in [1,2,3] if x%2==0 and [1,2,3].index(x)%2==0])

# class A:
#     def spam(self):
#         print('A.spam')
#
# class B(A):
#     def spam(self):
#         print('B.spam')
#         super().spam()  # Call parent spam(
# class C(A):
#     def __init__(self):
#         super().__init__()
#         self.y = 1
# B().spam()
# C()
import datetime
def timelang(func):
    def wrapper(*args,**kws):
        startTime = datetime.datetime.now()
        func()
        endtime = datetime.datetime.now()
    return wrapper