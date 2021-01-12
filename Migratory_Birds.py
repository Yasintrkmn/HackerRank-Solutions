Problem: https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr):
    s = {}
    for i in range(max(arr)+1):
        s[i] = arr.count(i)

    return max(s, key=s.get)

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
