from aoc_lib import fileToMap

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


day8_map=fileToMap("day8-1.txt", "", True)

# print(day8_map)

# eligibleTrees=len(day8_map)*2+len(day8_map[0])*2-4
# print(eligibleTrees+check_eligibility(day8_map))

print(check_best_spot(day8_map))