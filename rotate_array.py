#to rotate an array by d number

arr=[1,2,3,4,5,6]


def rotate(arr,d,n):
    for i in range(d):
        temp=arr[1]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=temp


rotate(arr,2,6)
for i in range(6):
    print(arr[i],end="")
