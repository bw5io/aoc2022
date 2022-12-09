from aoc_lib import fileToArray

def parse_data(input_file):
    output=[]
    for i in input_file:
        if i=="":
            break
        this_line=i.split(" ")
        this_line[1]=int(this_line[1])
        output.append(this_line)
    return output

def determine_tail_position(head, tail):
    if not (tail[0] in range(head[0] - 1, head[0] + 2) and tail[1] in range(head[1] - 1, head[1] + 2)):
        if tail[0]!=head[0]:
            if head[0]-tail[0]>0:
                tail[0]+=1
            else:
                tail[0]-=1
        if tail[1]!=head[1]:
            if head[1]-tail[1]>0:
                tail[1]+=1
            else:
                tail[1]-=1
    return tail

def travel_part_1(input_data):
    direction = {
        "R": [1,0],
        "L": [-1,0],
        "U": [0,1],
        "D": [0,-1]
    }
    output=set()
    output.add((0,0))
    head, tail=[0,0],[0,0]
    for i in input_data:
        for _ in range(i[1]):
            head[0]+=direction[i[0]][0]
            head[1]+=direction[i[0]][1]
            tail=determine_tail_position(head, tail)
            output.add((tail[0],tail[1]))
    return output

def travel_part_2(input_data):
    direction = {
        "R": [1,0],
        "L": [-1,0],
        "U": [0,1],
        "D": [0,-1]
    }
    output=set()
    output.add((0,0))
    knots=[[0,0] for _ in range(10)]
    for i in input_data:
        for _ in range(i[1]):
            knots[0][0]+=direction[i[0]][0]
            knots[0][1]+=direction[i[0]][1]
            for j in range(1, len(knots)):
                knots[j]=determine_tail_position(knots[j-1], knots[j])
            output.add((knots[9][0], knots[9][1]))
    return output

input_data = parse_data(fileToArray("day9-1.txt"))
print(input_data)

print(travel_part_2(input_data))
print(len(travel_part_2(input_data)))
# print(list([0,0]))