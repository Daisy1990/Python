#coding:utf-8

file1 = open('test.txt','r')
file2 = open('out-bcsl.txt','w')

while True:
    line = file1.readline()
    s1 = line.find("***编号****")
    s2 = line.find("公司行业")
    s3 = line.find("公司性质")
    s4 = line.find("公司规模")
    if s1 >=0:
        file2.write(line+'\n')
        line = file1.readline()
        line = file1.readline()
        file2.write("公司名稱：\n")
        file2.write(line+"\n")
        # line = file1.readline()
    if s2>=0:
        file2.write(line[s2:s3]+"\n")
        file2.write(line[s3:s4]+"\n")
        file2.write(line[s4:]+"\n")
        mylist = []
        while True:
            line = file1.readline()
            s5 = line.find("***编号****")
            if s5 <0:
                mylist.append(line)
            if s5>=0:
                file2.write("公司簡介：\n")
                file2.write("".join(mylist))
                file2.write(line+'\n')
                line = file1.readline()
                line = file1.readline()
                file2.write("公司名稱：\n")
                file2.write(line+"\n")
                break
            if not line:
                file2.write("公司簡介：\n")
                file2.write("".join(mylist))
                break

    if not line:
        break
file1.close()
file2.close()
