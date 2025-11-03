airtime_remaining = 15+3
print(airtime_remaining)
airtime_remaining = 7
print(airtime_remaining)

#loop variable
#it should be only visible inside the loop
for i in {'red', 'blue', 'yellow'}:
    print(i)
    
#python is kind in allowing access to the last value of the loop variable i
print("printing outside the loop")
print(i)

a=5
b=a #after executing this line, a and b are both equal
a=3 #after executing this line, a is no longer equal to b

print(a,b)

def mysum(xs):
    """Sum of all numbers in the list is xs, and return the total"""
    running_total=0
    for x in xs:
        running_total=running_total + x
    return running_total

def sum_to(n):
    """Return the sum of 1+2+3+...n"""
    ss=0
    v=1
    while v<==n:
        ss=ss+v
        v=v+1
        return ss

#TESTING_AREA
def test(pass_fail):
    if pass_fail:
       return (True)
    else:
         return (False)

def testsuite():
    #Add tests like these to your test suite
    print(test(mysum([1,2,3,4])==10))
    print(test(mysum(1.25, 2.5, 1.75)==5.5))
    print(test(mysum([1,-2,3])==2))
    print(test(mysum([])==0))
    print(test(mysum(range(11))==55)) #11 is not included in the list
    
    testsuite()