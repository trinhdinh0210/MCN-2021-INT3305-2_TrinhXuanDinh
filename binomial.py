import math

def factorial(x):
    i = 0
    result = 1
    for i in range(1, x+1):
        result = result*i;
    return result;

def prob(n, p, N):
    return factorial(N))/((math.pow(p,n))*factorial(n)*factorial(N-n));

def infoMeasure(n, p, N):
    return - math.log(prob(n,p,N),2)

def sumProb(n, p, N):
    i = 0
    sum = 0
    for i in range(1, n+1):
        sum = sum + prob(i, p, N)
    return sum

def approxEntropy(n, p, N):
    i = 0;
    sum = 0
    averageInfor = 0
    for i in range(1, n+1):
        sum = sum + infoMeasure(i, p, N)
    averageInfor = sum/n;
    return averageInfor;