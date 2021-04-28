from threading import Thread
lst = []
  
n = int(input("Enter number of elements : "))

for i in range(n):
    el = int(input())
    lst.append(el)
      
def maximum(l):
    print("Max number", max(l))

def minimum(l):
    print("Min number", min(l))

def mean(l):
    print("Mean ", sum(l)//len(l))

if __name__ == '__main__':
    print(lst)
    
    t1 = Thread(target=maximum, args=(lst, ))
    t1.start()
    
    t2 = Thread(target=minimum, args=(lst, ))
    t2.start()

    t3 = Thread(target=mean, args=(lst, ))
    t3.start()
    # maximum()
    # minimum()
    # mean()