from aoc_lib import file_to_array_no_strip

day6input = file_to_array_no_strip("day6-1.txt")

def find_unique_characters(input, target):
    head=0
    for index in range(len(input)):
        for i in range(head,index):
            if input[i]==input[index]:
                head=i+1
                break
        if index-head==target-1:
            return index+1
    return False

for i in day6input:
    if i=="":
        break
    else:
        print(find_unique_characters(i,4))
        print(find_unique_characters(i,14))