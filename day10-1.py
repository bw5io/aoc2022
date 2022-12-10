from aoc_lib import fileToArray

def parse_data(file_name):
    output_data=fileToArray(file_name)
    output_data.pop()
    output=[i.split(" ") for i in output_data]
    return output

def print_hit_or_miss(level, index):
    if index%40==0: print("")
    print("#" if index % 40 in range(level-1, level+2) else " ", end="")

def calculate_first(input):
    output=0
    index=1
    target_index=20
    level=1
    for i in input:
        pre_level=int(level)
        if i[0]=="noop":
            index+=1
        else:
            index+=2
            level+=int(i[1])
        if index>target_index:
            output+=pre_level*target_index
            target_index+=40
        if target_index>220:
            break
    return output

def calculate_second(input):
    index=0
    level=1
    for i in input:
        if i[0]=="noop":
            print_hit_or_miss(level, index)
            index+=1
        else:
            print_hit_or_miss(level, index)
            index+=1
            print_hit_or_miss(level, index)
            index+=1
            level+=int(i[1])


data=parse_data("day10-1.txt")
print(calculate_first(data))
calculate_second(data)


    