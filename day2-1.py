from aoc_lib import file_to_array
day2list=file_to_array("day2-1.txt", False)
SCORE={"X":1,"Y":2,"Z":3}
WIN_LOSE={0:3, 1:6, 2:0}

total=0

for i in day2list:
    if i=="":
        break
    this_round=i.split(" ")
    total+=SCORE[this_round[1]]
    result=ord(this_round[1])-ord(this_round[0])-23
    print(this_round, result)
    if result<0:
        result+=3
    total+=WIN_LOSE[result]

print(total)    