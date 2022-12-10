from aoc_lib import file_to_map

def check_eligibility(map):
    count=0
    for i in range(1,len(map)-1):
        for j in range(1,len(map[i])-1):
            if map[i][j]>max(map[x][j] for x in range(0,i)) or map[i][j]>max(map[x][j] for x in range(i+1, len(map))) or map[i][j]>max(map[i][x] for x in range(0, j)) or map[i][j]>max(map[i][x] for x in range(j+1, len(map[i]))):
                print(i,j)
                count+=1
    return count

def check_best_spot(map):
    max_score=1
    for i in range(1,len(map)-1):
        for j in range(1,len(map[i])-1):
            score=1
            step=0
            for x in range(i-1,-1,-1):
                step+=1
                if map[i][j]<=map[x][j]:
                    break
            score*=step
            step=0
            for x in range(i+1,len(map),1):
                step+=1
                if map[i][j]<=map[x][j]:
                    break
            score*=step
            step=0
            for x in range(j-1,-1,-1):
                step+=1
                if map[i][j]<=map[i][x]:
                    break
            score*=step
            step=0
            for x in range(j+1,len(map[i]),1):
                step+=1
                if map[i][j]<=map[i][x]:
                    break
                
            score*=step
            if score>=max_score:
                max_score=score
            print(score)
    return max_score


day8_map=file_to_map("day8-1.txt", "", True)
print(check_best_spot(day8_map))