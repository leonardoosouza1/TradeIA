from platform import python_revision
import pandas as pd
import numpy as np
import time

from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

counter = 0
hit = 0
check = 0
file0 = pd.read_csv('2010.csv', usecols=['TIME', 'C'])
file1 = pd.read_csv('2011.csv', usecols=['TIME', 'C'])
file2 = pd.read_csv('2012.csv', usecols=['TIME', 'C'])
file3 = pd.read_csv('2013.csv', usecols=['TIME', 'C'])
file4 = pd.read_csv('2014.csv', usecols=['TIME', 'C'])
file5 = pd.read_csv('2015.csv', usecols=['TIME', 'C'])
file6 = pd.read_csv('2016.csv', usecols=['TIME', 'C'])
file7 = pd.read_csv('2017.csv', usecols=['TIME', 'C'])
file8 = pd.read_csv('2018.csv', usecols=['TIME', 'C'])
file9 = pd.read_csv('2019.csv', usecols=['TIME', 'C'])
file10 = pd.read_csv('2020.csv', usecols=['TIME', 'C'])
file11 = pd.read_csv('2021.csv', usecols=['TIME', 'C'])


fx = file0['C']
fy = file1['C']
fz = file2['C']
fa = file3['C']
fb = file4['C']
fc = file5['C']
fd = file6['C']
fe = file7['C']
ff = file8['C']
fg = file9['C']
fh = file10['C']
fi = file11['C']


for i in range(0, len(file0[0:352000])):

    first = fx[i] - fx[i+1]
    second = fy[i] - fy[i+1]
    third = fz[i] - fz[i+1]
    fourth = fa[i] - fa[i+1]
    fifth = fb[i] - fb[i+1]
    sixth = fc[i] - fc[i+1]
    seventh = fd[i] - fd[i+1]
    eighth = fe[i] - fe[i+1]
    ninth = ff[i] - ff[i+1]
    tenth = fg[i] - fg[i+1]
    # eleventh = fh[i] - fh[i+1]

    numbers = [first, second, third, fourth, fifth,
               sixth, seventh, eighth, ninth, tenth]

    for i in range(0, len(numbers)):
        if numbers[i] > 0:

            numbers[i] = ['up', numbers[i], 2010 + i]
            check = 'up'
        else:
            numbers[i] = ['down', numbers[i], 2010 + i]
            check = 'down'

    check = (len(set(numbers[i])) == 'up')
    check2 = (len(set(numbers[i])) == 'down')
    print(check)
    print(check2)
    for i in range(0, len(numbers)):
        if numbers[i][1] > 0:
            hit += 1
        elif numbers[i][1] < 0:
            hit -= 1

    if True == False:
        print('')
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print(i)
        print(numbers[0][0])
        print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
        print(fx[i], '-', fy[i], '-', fz[i], '-', fa[i], '-', fb[i], '-', fc[i],
              '-', fd[i], '-', fe[i], '-', ff[i], '-', fg[i], '-', fh[i], '-', fi[i])
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(fx[i+1], '-', fy[i+1], '-', fz[i+1], '-', fa[i+1], '-', fb[i+1], '-', fc[i+1],
              '-', fd[i+1], '-', fe[i+1], '-', ff[i+1], '-', fg[i+1], '-', fh[i+1], '-', fi[i+1])
        print('IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')
        print(f'{(fx[i]-fx[i+1]):.5f} - {(fy[i]-fy[i+1]):.5f} - {(fz[i]-fz[i+1]):.5f} - {(fa[i]-fa[i+1]):.5f} - {(fb[i]-fb[i+1]):.5f} - {(fc[i]-fc[i+1]):.5f} - {(fd[i]-fd[i+1]):.5f} - {(fe[i]-fe[i+1]):.5f} - {(ff[i]-ff[i+1]):.5f} - {(fg[i]-fg[i+1]):.5f} - {(fh[i]-fh[i+1]):.5f} - {(fi[i]-fi[i+1]):.5f}')
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        print('')

        counter += 1

print('')
print('_________________________')
print('Janeiro: ', counter, 'hits')
# y = file['style']
# x = file.drop('style', axis=1)

# x_learing, x_test, y_learning, y_test = train_test_split(x, y, test_size=0.3)

# model = ExtraTreesClassifier()
# model.fit(x_learing, y_learning)

# result = model.score(x_test, y_test)
# print("Resultado: ", result)

# prev = model.predict(x_test[400:403])

# print(prev)
