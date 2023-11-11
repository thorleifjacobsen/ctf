import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Read the coordinates for the poles from a file
poles = []
with open('data.txt') as f:
    for line in f:
        x, y = map(float, line.strip().split())
        poles.append((x, y))

# Compute the convex hull for the set of poles
hull = ConvexHull(poles)

area = hull.area

# Plot the poles and the convex hull
x = [p[0] for p in poles]
y = [p[1] for p in poles]
plt.plot(x, y, 'x')
for simplex in hull.simplices:
    for i in simplex:
        print(str(int(poles[i][0])) + " " + str(int(poles[i][1])))
    plt.plot([poles[i][0] for i in simplex], [poles[i][1] for i in simplex], 'k-')


# Add the calculated area to the plot
plt.text(0, 0, f'Area: {area:.0f}', ha='left', va='bottom')

# Print area
print(area);

# Show the plot
plt.show()
