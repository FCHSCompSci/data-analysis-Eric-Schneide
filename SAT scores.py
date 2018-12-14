import csv
import matplotlib.pyplot as plt

filename='dcps_SATScores.csv'


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index,columb_header in enumerate(header_row):
        print(index, columb_header)

    readingscore=[]
    writingscore=[]
    mathscore=[]
    overallscore=[]
    for row in reader:
        readingscore.append(int(row[3]))
        writingscore.append(int(row[4]))
        mathscore.append(int(row[5]))
        overallscore.append(int(row[6]))
    avg_r_score=(sum(readingscore)/len(readingscore))
    avg_w_score=(sum(writingscore)/len(writingscore))
    avg_m_score=(sum(mathscore)/len(mathscore))
    avg_o_score=(sum(overallscore)/len(overallscore))

x_values=['Reading Score','Writing Score','Math Score']
y_values=[avg_r_score,avg_w_score,avg_m_score]

plt.xlabel('SAT Catagory')
plt.ylabel('Average Score')
plt.ylim(300,400)
plt.bar(x_values,y_values)
plt.show()
