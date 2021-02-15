nums = [386, 462, 47, 418, 907, 344, 236, 375, 462, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 826, 248, 866, 950, 626, 949, 687, 217]
repit_elems=[]
for elem in nums:
    if nums.count(elem)>1:
        repit_elems.append(elem)


print(set(repit_elems) or 'никто не','повторяется')
        
