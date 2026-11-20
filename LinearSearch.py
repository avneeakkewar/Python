numbers = [10,20,4,87,67,89,45,90]
target = int(input("Enter number to search\n"))

# 1st approach when we want to get only index
# for i in range(len(numbers)):
#     if target == numbers[i]:
#         print(f"Element found at index {i+1}")

#  2nd approach for index and value 
# enumerate() is a built-in function that allows you to access 
# both the index and the value of elements while looping through 
# a sequence.
#  syntex === enumerate(iterable, start=0)

for index, value in enumerate(numbers,start=1):
    if target == value:
        print("Element found", index,":",value)



