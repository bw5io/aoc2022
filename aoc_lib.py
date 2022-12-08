def fileToArray(filename, return_int=False):
    output=[]
    openedfile=open(filename)
    flag=False
    while True:
        thisline = openedfile.readline().strip()
        if return_int==True and thisline.isnumeric():
            thisline=int(thisline)
            flag=False
        if thisline=='':
            if flag == True:
                break
            else:
                flag = True
        output.append(thisline)
    return output

def fileToArrayNoStrip(filename, return_int=False):
    output=[]
    openedfile=open(filename)
    flag=False
    while True:
        thisline = openedfile.readline()
        if return_int==True and thisline.isnumeric():
            thisline=int(thisline)
            flag=False
        if thisline=='':
            if flag == True:
                break
            else:
                flag = True
        output.append(thisline)
    return output

def fileToMap(filename, sep, return_int=False):
    input=fileToArray(filename)
    output=[]
    for i in input:
        if i=="":
            break
        if sep=="":
            line=list(i)
        else:
            line=i.split(sep)
        if return_int==True:
            line=[int(element) for element in line]
        output.append(line)
    return output

def addDictList(obj, key, value):
    if key in obj:
        obj[key].append(value)
    else:
        obj[key]=[value]

def addDict(obj, key, value):
    if key in obj:
        obj[key]+=value
    else:
        obj[key]=value