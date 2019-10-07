
def calc (s):
    print('s=',s)
    nums = map(int,s.split('*'))
    print('nums=',nums)
    return numpy.prod(nums)



print(calc("2*4"))
