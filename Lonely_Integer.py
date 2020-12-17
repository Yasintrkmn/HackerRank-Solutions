# Listedeki yalnız elemanı bulma uygulaması
# n=len(a) örn: a=[0,0,1,2,1] 

def lonelyinteger(a):
    for i in a:
        if a.count(i)==1:
            return i

if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    print(result)
