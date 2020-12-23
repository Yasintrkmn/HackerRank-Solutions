# Bir kare matris verildiğinde, köşegenlerinin toplamları arasındaki mutlak farkı hesaplama

def diagonalDifference(arr):
    lt,tl=0,0
    j=len(arr)-1
    for i in range(len(arr)):
        lt += arr[i][i]

        tl += arr[i][j]
        j-=1
    return abs(tl-lt)
if __name__ == '__main__':
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
