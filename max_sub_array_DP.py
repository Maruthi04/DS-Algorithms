arr=[-2,1,-3,4,-1,2,1,-5,4]
max_till_here=0
max_far=-1000
for i in arr:
    max_till_here=max_till_here+i
    if(max_far<max_till_here):
        max_far=max_till_here
    if(max_till_here<0):
        max_till_here=0
print(max_far)