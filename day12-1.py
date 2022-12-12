import sys
from aoc_lib import file_to_array
sys.setrecursionlimit(15000)

def parse_data(input_filename):
    input_data=file_to_array(input_filename)
    output=[]
    for i in input_data:
        if i=="":
            return output
        else:
            output.append(list(i))

def find_route(data, current_depth=0, visited=None, x=0, y=0):
    if (visited==None):
        visited=set()
    visited.add((x,y))
    possible_route=[]
    if x-1 in range(0,len(data)):
        if data[x-1][y]=="E" and data[x][y]=="z":
            print(x,y,visited)
            return current_depth+1
        if ord(data[x-1][y])-ord(data[x][y])<=1 and ((x-1,y) not in visited ):
            possible_route.append(find_route(data, current_depth+1, visited, x-1, y))
    if x+1 in range(0,len(data)):
        if data[x+1][y]=="E" and data[x][y]=="z":
            print(x,y,visited)
            return current_depth+1
        if ord(data[x+1][y])-ord(data[x][y])<=1 and ((x+1,y) not in visited ):
            possible_route.append(find_route(data, current_depth+1, visited, x+1, y))
    if y-1 in range(0,len(data[x])):
        if data[x][y-1]=="E" and data[x][y]=="z":
            print(x,y,visited)
            return current_depth+1
        if ord(data[x][y-1])-ord(data[x][y])<=1 and ((x,y-1) not in visited ): 
            possible_route.append(find_route(data, current_depth+1, visited, x, y-1))
    if y+1 in range(0,len(data[x])):
        if data[x][y+1]=="E" and data[x][y]=="z":
            print(x,y,visited)
            return current_depth+1
        if ord(data[x][y+1])-ord(data[x][y])<=1 and ((x,y+1) not in visited):
            possible_route.append(find_route(data, current_depth+1, visited, x, y+1))
    try:
        return min(possible_route)
    except:
        return 9999999999999

print(find_route(parse_data("day12-1.txt")))