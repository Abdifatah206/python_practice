#python lists
nums = [25,12,11,45,47]
#print all
print(nums)
#print by index number
print(nums[4])
print(nums[-4])



#string list
names = ['abdi','ali','jama']
print(names)
print(names[1])

#mixed list of different values
values = [9.5,'ali',8]
print(values)

#combining two lists
mil = [names,values]
print(mil)

#list operations
nums.append(22)
print(nums)

nums.remove(25)
print(nums)

nums.pop(1)
print(nums)


#max min sum

print(max(nums))
print(min(nums))
print(sum(nums))


nums.sort()
print(nums)