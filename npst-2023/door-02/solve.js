// The object represents the cube folded out as a cross. 
//
//            [ Index 0 ]
// [ Index 1 ][ Index 2 ][ Index 3 ]
//            [ Index 4 ]
//            [ Index 5 ]
//
// Each cube has 3 rows and 3 columns.

let rubicsCube = [
  [["R1", "R2", "R3"], ["R4", "R5", "R6"], ["R7", "R8", "R9"]],
  [["B1", "B2", "B3"], ["B4", "B5", "B6"], ["B7", "B8", "B9"]],
  [["W1", "W2", "W3"], ["W4", "W5", "W6"], ["W7", "W8", "W9"]],
  [["G1", "G2", "G3"], ["G4", "G5", "G6"], ["G7", "G8", "G9"]],
  [["O1", "O2", "O3"], ["O4", "O5", "O6"], ["O7", "O8", "O9"]],
  [["Y1", "Y2", "Y3"], ["Y4", "Y5", "Y6"], ["Y7", "Y8", "Y9"]],
];

// This is the letters from the challenge on their correct positions:
rubicsCube = [
  [["_ ", "_ ", ": "], ["_ ", "O ", "S "], ["U ", "S ", "M "]],
  [["L ", "D ", "P "], ["B ", "T ", "L "], ["_ ", "E ", "Ø "]],
  [["R ", "D ", "T "], ["S ", "N ", "? "], ["P ", "E ", "P "]],
  [["E ", "L ", "{ "], ["L ", "S ", "E "], ["W ", ") ", "O "]],
  [["_ ", "K ", "} "], ["U ", "E ", "B "], ["I ", "G ", "L "]],
  [["U ", "L ", "E "], ["S ", "E ", "N "], ["_ ", "Y ", "R "]],
];

// Ascii art draw the cube
function drawCube() {
  let cube = `
           ${rubicsCube[0][0].join(" ")}
           ${rubicsCube[0][1].join(" ")}
           ${rubicsCube[0][2].join(" ")}
  ${rubicsCube[1][0].join(" ")} ${rubicsCube[2][0].join(" ")} ${rubicsCube[3][0].join(" ")}
  ${rubicsCube[1][1].join(" ")} ${rubicsCube[2][1].join(" ")} ${rubicsCube[3][1].join(" ")}
  ${rubicsCube[1][2].join(" ")} ${rubicsCube[2][2].join(" ")} ${rubicsCube[3][2].join(" ")}
           ${rubicsCube[4][0].join(" ")}
           ${rubicsCube[4][1].join(" ")}
           ${rubicsCube[4][2].join(" ")}
           ${rubicsCube[5][0].join(" ")}
           ${rubicsCube[5][1].join(" ")}
           ${rubicsCube[5][2].join(" ")}
  `
  console.log(cube);
}

// Rotate the cube
function rotateFace(face) {
  // Copy the object so we can modify it
  let newRubics = JSON.parse(JSON.stringify(rubicsCube))

  // Perform rotations for the "Front" face
  if (face == "F") {
    newRubics[0][2][0] = rubicsCube[1][2][2];
    newRubics[0][2][1] = rubicsCube[1][1][2];
    newRubics[0][2][2] = rubicsCube[1][0][2];

    newRubics[3][0][0] = rubicsCube[0][2][0];
    newRubics[3][1][0] = rubicsCube[0][2][1];
    newRubics[3][2][0] = rubicsCube[0][2][2];

    newRubics[4][0][0] = rubicsCube[3][2][0];
    newRubics[4][0][1] = rubicsCube[3][1][0];
    newRubics[4][0][2] = rubicsCube[3][0][0];

    newRubics[1][0][2] = rubicsCube[4][0][0];
    newRubics[1][1][2] = rubicsCube[4][0][1];
    newRubics[1][2][2] = rubicsCube[4][0][2];

    newRubics[2] = rotate3DArray(rubicsCube[2]);
  }

  // Perform rotations for the "Right" face
  else if (face == "R") {
    newRubics[2][2] = rubicsCube[1][2];
    newRubics[3][2] = rubicsCube[2][2];
    newRubics[5][0] = rubicsCube[3][2].reverse();
    newRubics[1][2] = rubicsCube[5][0].reverse();
    newRubics[4] = rotate3DArray(rubicsCube[4]);
  }

  // Perform rotations for the "Left" face
  else if (face == "L") {
    newRubics[1][0] = rubicsCube[2][0];
    newRubics[2][0] = rubicsCube[3][0];
    newRubics[3][0] = rubicsCube[5][2].reverse();
    newRubics[5][2] = rubicsCube[1][0].reverse();
    newRubics[0] = rotate3DArray(rubicsCube[0]);
  }

  // Perform rotations for the "Down" face
  else if (face == "D") {
    newRubics[0][0][0] = rubicsCube[5][0][0];
    newRubics[0][1][0] = rubicsCube[5][1][0];
    newRubics[0][2][0] = rubicsCube[5][2][0];

    newRubics[2][0][0] = rubicsCube[0][0][0];
    newRubics[2][1][0] = rubicsCube[0][1][0];
    newRubics[2][2][0] = rubicsCube[0][2][0];

    newRubics[4][0][0] = rubicsCube[2][0][0];
    newRubics[4][1][0] = rubicsCube[2][1][0];
    newRubics[4][2][0] = rubicsCube[2][2][0];

    newRubics[5][0][0] = rubicsCube[4][0][0];
    newRubics[5][1][0] = rubicsCube[4][1][0];
    newRubics[5][2][0] = rubicsCube[4][2][0];
    newRubics[1] = rotate3DArray(rubicsCube[1]);
  }

  // Perform rotations for the "Up" face
  else if (face == "U") {
    newRubics[0][0][2] = rubicsCube[2][0][2];
    newRubics[0][1][2] = rubicsCube[2][1][2];
    newRubics[0][2][2] = rubicsCube[2][2][2];

    newRubics[2][0][2] = rubicsCube[4][0][2];
    newRubics[2][1][2] = rubicsCube[4][1][2];
    newRubics[2][2][2] = rubicsCube[4][2][2];

    newRubics[4][0][2] = rubicsCube[5][0][2];
    newRubics[4][1][2] = rubicsCube[5][1][2];
    newRubics[4][2][2] = rubicsCube[5][2][2];

    newRubics[5][0][2] = rubicsCube[0][0][2];
    newRubics[5][1][2] = rubicsCube[0][1][2];
    newRubics[5][2][2] = rubicsCube[0][2][2];
    newRubics[3] = rotate3DArray(rubicsCube[3]);
  }

  // Perform rotations for the "Back" face
  else if (face == "B") {
    newRubics[0][0][0] = rubicsCube[3][0][2];
    newRubics[0][0][1] = rubicsCube[3][1][2];
    newRubics[0][0][2] = rubicsCube[3][2][2];

    newRubics[3][0][2] = rubicsCube[4][2][2];
    newRubics[3][1][2] = rubicsCube[4][2][1];
    newRubics[3][2][2] = rubicsCube[4][2][0];

    newRubics[1][0][0] = rubicsCube[0][0][2];
    newRubics[1][1][0] = rubicsCube[0][0][1];
    newRubics[1][2][0] = rubicsCube[0][0][0];

    newRubics[4][2][0] = rubicsCube[1][0][0];
    newRubics[4][2][1] = rubicsCube[1][1][0];
    newRubics[4][2][2] = rubicsCube[1][2][0];

    newRubics[5] = rotate3DArray(rubicsCube[5]);
  }
  // Overwrite the current cube with this new one.
  rubicsCube = newRubics;
}

// Rotate a flat 3x3 array around the edges:
function rotate3DArray(array) {
  let newArray = JSON.parse(JSON.stringify(array));
  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array[0].length; j++) {
      newArray[i][j] = array[array.length - j - 1][i];
    }
  }
  return newArray;
}

// Algorithm I got from the solve website when inputing the colors from the image:
const algorithm = "U B U' B L' B R L' B2 U F B2 U' B2 R2 F2 B2 D2 B2 D"

// Perform the algorithm on the cube:
algorithm.split(" ").forEach(face => {
  // Rotate twice
  if (face.includes("2")) { rotateFace(face.substring(0, 1)); rotateFace(face.substring(0, 1)); }
  // Backwards (same as rotate 3 times)
  else if (face.includes("'")) { rotateFace(face.substring(0, 1)); rotateFace(face.substring(0, 1)); rotateFace(face.substring(0, 1)); }
  // Rotate once
  else { rotateFace(face.substring(0, 1)); }
});

// Draw the answer
drawCube();
