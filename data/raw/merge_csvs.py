from glob import glob

with open('Happy/Happy_csv.csv', 'a') as singleFile:
    for csv in glob('Happy/*.csv'):
        if csv == 'Happy/Happy_csv.csv':
            pass
        else:
            for line in open(csv, 'r'):
                singleFile.write(line)
