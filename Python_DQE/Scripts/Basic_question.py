"""
create list of 100 random numbers from 0 to 1000
sort list from min to max (without using sort())
calculate average for even and odd numbers
print both average result in console 
Each line of code should be commented with description.

"""

# create list of 100 random numbers from 0 to 1000
import random
random_100 = [random.randint(0,1000) for i in range(0,1000)]

print(random_100)

#sort list from min to max (without using sort())
for i in range(0, len(random_100)):
    for j in range(i,len(random_100)):
        if random_100[i] > random_100[j]:
            random_100[i], random_100[j] = random_100[j], random_100[i]

print("Äfter sorting",random_100)


# calculate average for even and odd numbers
arr = random_100
even_elem, odd_elem = [], [] # holding even and odd elem
for i in arr:
    even_elem.append(i) if i % 2 == 0 else odd_elem.append(i)

print("average for even: ", sum(even_elem)/len(even_elem))
print("average for odd: ", sum(odd_elem)/len(odd_elem))
