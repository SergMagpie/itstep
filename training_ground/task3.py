class my_sum(int):
    def __call__(self, number=0):
        return my_sum(self + number) 
        
print(my_sum(3)(4)(8))