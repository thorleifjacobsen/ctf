const fs = require('fs');

// Load dictionary and letter (the commented are the test examples just to verify)
let packages = [
    // { x: 30, y: 30, z: 20 },
    // { x: 30, y: 30, z: 30 },
    // { x: 25, y: 30, z: 20 }
]
// Populate packages with all data. I know it is not pretty but I dont care!
fs.readFileSync('pakker.csv', 'utf8')
    .split("\n")
    .forEach(w => packages.push({
        height: parseInt(w.split(",")[0]),
        length: parseInt(w.split(",")[1]),
        width: parseInt(w.split(",")[2])
    }));


const rollWidth = 110;
let usedRoll = 0;

packages.forEach(pkg => {

    // Unpack
    let { width, length, height } = pkg;

    // Array to store the 3 different orientations
    let sizeArray = [];

    // Put it in all 3 orientations and generate a object with required length and width for it.
    // Orientation 1: Length and height rolls towards the roll, width is put along the roll width axis
    sizeArray.push({ length: length * 2 + height * 2, width: width + (length > height ? height : length) })
    // Orientation 2: Height and width rolls towards the roll, length is put along the roll width axis
    sizeArray.push({ length: height * 2 + width * 2, width: length + (height > width ? width : height) })
    // Orientation 3: Width and length rolls towards the roll, height is put along the roll width axis
    sizeArray.push({ length: width * 2 + length * 2, width: height + (width > length ? length : width) })

    // Initialize the requiredLength to be a impossible high number for the packages.
    let requiredLength = 9999999999999999;

    // Loop through the calculated sizes and do a check if the required size length or width
    // can be put on the roll width and the opposite against the length.
    sizeArray.forEach(size => {
        if (size.length <= rollWidth && size.width < requiredLength) requiredLength = size.width;
        if (size.width <= rollWidth && size.length < requiredLength) requiredLength = size.length;
    })

    // Add required length to roll usage
    usedRoll += requiredLength;

})

// output answer.
console.log(usedRoll);