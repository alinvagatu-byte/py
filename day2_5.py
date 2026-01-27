# Exercise find biggest number from array

arr = [22, 33, 3, 100, 1, 0 , -22, 8]
biggest = 0

for element in arr:
    if element > biggest:
        biggest = element

print(f"Biggest number from array is {biggest}")

