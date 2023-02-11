const fs = require('fs');

// Read the coordinates for the poles from a file
const poles = [];
const data = fs.readFileSync('data.txt', 'utf8');
data.split('\n').forEach((line) => {
    const [x, y] = line.trim().split(/\s+/).map(Number);
    poles.push([x, y]);
});

// Compute the convex hull for the set of poles
const hull = [];
poles.forEach((p1) => {
    poles.forEach((p2) => {
        poles.forEach((p3) => {
            if (isLeft(p1, p2, p3)) {
                if (hull.every(([p4, p5, p6]) => !isLeft(p4, p5, p6, p1, p2, p3))) {
                    hull.push([p1, p2, p3]);
                }
            }
        });
    });
});

// Calculate the total area enclosed by the convex hull
let area = 0;
hull.forEach(([p1, p2, p3]) => {
    area += (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2;
});

// Print area
console.log(Math.abs(area));

// Helper function for computing the convex hull
function isLeft(p1, p2, p3, ...rest) {
    const result = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]);
    if (rest.length === 0) {
        return result >= 0;
    }
    return result * isLeft(...rest) >= 0;
}