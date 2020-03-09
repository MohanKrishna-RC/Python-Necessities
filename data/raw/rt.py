import glob
count = 0
for _file in glob.glob('/home/mohan/demo_testing/exp_1/entity_1788' + '/*/*/*.jpg'):
    print(_file)
    count+=1

print(count)