# Problem: https://www.hackerrank.com/challenges/fair-rations/problem

def fairRations(B):
    count = 0
    for i in range(len(B) - 1):
        if B[i] % 2 != 0:
            B[i] += 1
            B[i + 1] += 1
            count += 2

    if sum(B) % 2 == 1:
            return "NO"

    return count

if __name__ == '__main__':

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)
    
    print(rssult)
