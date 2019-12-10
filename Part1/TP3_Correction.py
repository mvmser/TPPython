# MyStack = []
StackSize = 10


def DisplayStack(MyStack):
    print("Stack currently contains:")
    for Item in MyStack:
        print(Item)


def Push(MyStack, Value):
    if len(MyStack) < StackSize:
        MyStack.append(Value)
    else:
        print("Stack is full!")


def Pop(MyStack):
    if len(MyStack) > 0:
        MyStack.pop()
    else:
        print("Stack is empty.")


MyStack = []
Push(MyStack, 1)
Push(MyStack, 2)
Push(MyStack, 3)
DisplayStack(MyStack)


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i]),
