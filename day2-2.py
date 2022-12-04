from aoc_lib import fileToArray
day2list=fileToArray("day2-1.txt", False)
SCORE_OPTION={65:1,66:2,67:3}
SCORE_WIN_LOSE={"X":0,"Y":3,"Z":6}
WIN_LOSE={"X":-1,"Y":0,"Z":1}

total=0

for i in day2list:
    if i=="":
        break
    this_round=i.split(" ")
    total+=SCORE_WIN_LOSE[this_round[1]]
    print(total)
    this_option=ord(this_round[0])+WIN_LOSE[this_round[1]]
    if this_option>67:
        this_option-=3
    if this_option<65:
        this_option+=3
    print(this_round, this_option)
    total+=SCORE_OPTION[this_option]
    print(total)
print(total)    