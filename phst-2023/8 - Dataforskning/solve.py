import matplotlib.pyplot as plt
import csv

x = []
y = []

# vingespenn, gjennomsnittlig antall egg samlet per dag, kyllingtype

with open('innsamlet.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        if row[2] == "'1'":
            x.append(int(row[0]))
            y.append(int(row[1]))

# Reverse X 
x.reverse()

# Set the figure size to (6, 4) inches
fig, ax = plt.subplots(figsize=(8, 1.5))

plt.scatter(x, y, color = 'g', label = "Egg Collection")
plt.xlabel('Wing Span')
plt.ylabel('Average Eggs Collected per Day')
plt.title('Egg Collection vs Wing Span')
plt.savefig('graphs.png')
