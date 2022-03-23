import numpy as np
import matplotlib.pyplot as plt
f = open("test.inp", "r")
lines = np.array(f.readlines())
read1 = np.char.split(lines[9:274])
read2 = np.char.split(lines[275:674])
data1 = []
data2 = []
for row in read1:
    data1.append([float(row[1].replace(',', '')), float(row[2].replace(',', ''))])
for row in read2:
    data2.append([int(row[0].replace(',', '')), int(row[1].replace(',', '')), int(row[2].replace(',', '')), int(row[3].replace(',', ''))])
aspect_ratio = []
area = []
element5 = set()
for data in data2:
    plt_x = []
    plt_y = []
    length = []
    plt_x.append(data1[data[3]-1][0])
    plt_y.append(data1[data[3]-1][1])
    for index in data[1:]:
        plt_x.append(data1[index-1][0])
        plt_y.append(data1[index-1][1])
    for i in range(len(plt_x)-1):
        length.append(pow(pow(plt_x[i+1] - plt_x[i], 2) + pow(plt_y[i+1] - plt_y[i], 2), 0.5))
    plt.plot(plt_x, plt_y)
    aspect_ratio.append(f'aspect_ratio = {max(length) / min(length)}')
    s = sum(length)/2
    area.append(pow(s*(s-length[0])*(s-length[1])*(s-length[2]), 0.5))
    if 5 in data[1:]:
        for element in data[1:]:
            element5.add(element)
    element5.discard(5)
print('max area :', max(area), 'max index :', area.index(max(area)))
print('min area :', min(area), 'min index :', area.index(min(area)))
print('element5', element5)
plt.legend(aspect_ratio, loc='best')
plt.savefig('func2_1.png')
plt.close()