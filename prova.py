import os
from os import listdir
from os.path import isfile, join

def add_elements(a,b):
    result=[]
    for item_a,item_b in zip(a,b):
        result.append(item_a+item_b)
    return result


if __name__ == '__main__':
    print('piero')

    onlyfiles = [f for f in listdir() if isfile(join("", f))]

    for nomefilein in onlyfiles:
        if nomefilein == "input.txt":
            fin = os.path.join("", nomefilein)


    with open(fin) as f:
        lines=f.readlines()

    last_line1,last_line2 = lines[-2],lines[-1]

    list1=list(map(int,(last_line1[: -1].split(','))))
    list2=list(map(int,(last_line2[: -1].split(','))))
    #
    new_list=add_elements(list1,list2)
    #
    nomefileout=nomefilein.replace("input","output")
    fout = os.path.join("", nomefileout)
    #
    with open('output.txt','a') as fout:
        for i,item in enumerate(new_list):
            fout.write(str(i)+","+str(item))
            if i < len(new_list)-1:
               fout.write(",\n")
            else:
                fout.write('\n')




    print('fineeeeee')








