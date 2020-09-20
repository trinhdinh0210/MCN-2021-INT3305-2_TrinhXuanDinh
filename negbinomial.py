import math

def factorial(x):
    i = 0
    result = 1
    for i in range(1, x+1):
        result = result*i;
    return result;

def prob(n, p, N, r):
    return (factorial(n))/((math.pow(p,n))*factorial(n-r+1)*factorial(r-1));

def infoMeasure(n, p, N, r):
    return -math.log(prob(n,p,N,r),2)

def sumProb(n, p, N, r):
    i = 0
    sum = 0
    for i in range(1, n+1):
        sum = sum + prob(i, p, N, r)
    return sum

def approxEntropy(n, p, N, r):
    i = 0;
    sum = 0
    averageInfor = 0
    for i in range(1, n+1):
        sum = sum + infoMeasure(i, p, N, r)
    averageInfor = sum/n;
    return averageInfor;