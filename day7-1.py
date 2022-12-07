from aoc_lib import fileToArray

class folder:
    def __init__(self, container):
        self.files=[]
        self.folders={}
        self.container=container
    
    def get_size(self):
        result = sum(x.get_size() for x in self.folders.values()) + sum(self.files)
        return result
    
    def add_folder(self, folder_name):
        self.folders[folder_name]=folder(self)
        return self.folders[folder_name]
    
    def get_folder(self, folder_name):
        if folder_name in self.folders:
            return self.folders[folder_name]
        else:
            return self.add_folder(folder_name)
    
    def add_file(self, file_size):
        self.files.append(file_size)
        return True
    
    def eligible_folder(self, file_size_limit):
        eligible_folder_size = 0
        current_folder_size = 0
        for i in self.folders.values():
            result, eligible_subfolder_size = i.eligible_folder(file_size_limit)
            eligible_folder_size+=eligible_subfolder_size
            current_folder_size+=result
        current_folder_size+=sum(self.files)
        if current_folder_size<file_size_limit:
            eligible_folder_size+=current_folder_size
        return current_folder_size, eligible_folder_size
    
    def minimum_viable_folder(self, target):
        current_folder_size=0
        minimum_viable_folder_size = 999999999999999999
        for i in self.folders.values():
            result, current_minimum_viable_folder_size = i.minimum_viable_folder(target)
            current_folder_size+=result
            if current_minimum_viable_folder_size!=-1 and current_minimum_viable_folder_size<minimum_viable_folder_size:
                minimum_viable_folder_size = current_minimum_viable_folder_size
        current_folder_size+=sum(self.files)
        if current_folder_size>target:
            print(current_folder_size)
        if current_folder_size>target and current_folder_size<minimum_viable_folder_size:
            minimum_viable_folder_size=current_folder_size
        return current_folder_size, minimum_viable_folder_size


    def __repr__(self):
        return f"Files ${self.files} Folders ${self.folders}"

rootNode=folder(None)
currentNode=rootNode

day7input = fileToArray("day7-1.txt")
for i in day7input:
    if i=="":
        break
    thisline = i.split(" ")
    if thisline[0]=="$":
        if thisline[1]=="cd":
            if thisline[2]=="/":
                currentNode=rootNode
            elif thisline[2]=="..":
                currentNode=currentNode.container
            else:
                currentNode=currentNode.get_folder(thisline[2])
    else:
        if thisline[0].isnumeric():
            currentNode.add_file(int(thisline[0]))

print(rootNode)
print(rootNode.eligible_folder(100000))
print(rootNode.get_size())

target=40000000
print(rootNode.get_size()-target)
# print(rootNode.get_size)
print(rootNode.minimum_viable_folder(rootNode.get_size()-target))