from glob import glob

with open('main.csv', 'a') as singleFile:
    for csv in glob('final_csv/*.csv'):
        if csv == '../main.csv':
            pass
        else:
            for line in open(csv, 'r'):
                singleFile.write(line)
