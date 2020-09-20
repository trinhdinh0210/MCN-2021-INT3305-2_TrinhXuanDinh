import math

def prob(n, p):
    return 1/(math.pow(p,n));

def infoMeasure(n, p):
    return -math.log(prob(n,p),2)

def sumProb(N, p):
    i = 0
    sum = 0
    for i in range(1, N+1):
        sum = sum + prob(i, p)
    return sum
'''
Bien luan
    Gia su n = 99 ham sumProb(99, 2) cho gia tri bang 1
    Khi n tien dan den am vo cung tong gia tri xac suat phan bo theo geometry cang tien dan den 1
'''

def approxEntropy(N, p):
    i = 0;
    sum = 0
    averageInfor = 0
    for i in range(1, N+1):
        sum = sum + infoMeasure(i, p)
    averageInfor = sum/N;
    return averageInfor;