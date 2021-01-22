import sys

input_= sys.stdin.read().split()

l,k,h=int(input_[0]),int(input_[1]),int(input_[2])
if not l%(k):
    min_=max_=(l/(k))*h
    
elif l <= k:
    min_=max_=h
    
#elif l < k*h:
#    min_=k*h
#    max_=min_+h

else:
    min_=(l//(k))*h
    max_=min_+h
        
print('%.8f %.8f'%(min_,max_))
 
