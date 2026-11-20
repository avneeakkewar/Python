numbers = [10,20,4,87,67,89,45,90]
numbers.sort()
target = int(input("Enter number to search\n"))

low=0
high=len(numbers)-1


while low < high:
    mid =(low+high) // 2

    if numbers[mid] == target:
        print(f"Element found at {mid}")
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("element not found")
    