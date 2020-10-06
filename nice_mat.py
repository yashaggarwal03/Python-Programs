'''
A matrix of size n×m is called nice, if all rows and columns of the matrix are palindromes. A sequence of integers (a1,a2,…,ak) is a palindrome, if for any integer i (1≤i≤k) the equality ai=ak−i+1 holds.

Sasha owns a matrix a of size n×m. In one operation he can increase or decrease any number in the matrix by one. Sasha wants to make the matrix nice. He is interested what is the minimum number of operations he needs.

Help him!

Input
The first line contains a single integer t — the number of test cases (1≤t≤10). The t tests follow.

The first line of each test contains two integers n and m (1≤n,m≤100) — the size of the matrix.

Each of the next n lines contains m integers ai,j (0≤ai,j≤109) — the elements of the matrix.

Output
For each test output the smallest number of operations required to make the matrix nice.
'''

#soln:
t = int(input())
for cas in range(t):
    n, m = map(int, input().split())
    A = []
    for i in range(n):
        A.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(m):
            a = A[i][j]
            b = A[n-i-1][j]
            c = A[i][m-j-1]
            d = A[n-i-1][m-j-1]
            arr = sorted([a, b, c, d])
            ans += arr[1] - arr[0]
            ans += arr[2] - arr[1]
            ans += arr[3] - arr[1]
    print(ans//4)
