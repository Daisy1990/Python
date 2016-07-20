#coding:utf-8

world_list = []
world_dict = {}
with open("yuan.txt",'r') as file1,open('out-tj.txt','w') as file2:
    for line in file1:
        world_list.append(line.split('/'))
    for item in world_list:
        for item2 in item:
            if item2.strip() not in "，！。“”":
                if item2 not in world_dict:
                    world_dict[item2] = 1
                else:
                    world_dict[item2] += 1
    for key in world_dict:
        print key,world_dict[key]
        file2.write(key+" "+str(world_dict[key]))