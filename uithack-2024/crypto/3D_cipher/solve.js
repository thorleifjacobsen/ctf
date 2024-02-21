// The object represents the cube folded out as a cross. 
//
//            [ Index 0 ]
// [ Index 1 ][ Index 2 ][ Index 3 ]
//            [ Index 4 ]
//            [ Index 5 ]
//
// Each cube has 3 rows and 3 columns.

let rubicsCube = [
  [["n ", "d ", "_ "], ["0 ", "a ", "r "], ["f ", "H ", "0 "]],
  [["U ", "c ", "} "], ["2 ", "_ ", "m "], ["r ", "3 ", "{ "]],
  [["4 ", "3 ", "T "], ["_ ", "l ", "3 "], ["h ", "1 ", "4 "]],
  [["3 ", "5 ", "k "], ["1 ", "_ ", "_ "], ["7 ", "i ", "h "]],
  [["5 ", "3 ", "4 "], ["m ", "g ", "! "], ["_ ", "0 ", "l "]],
  [["3 ", "l ", "_ "], ["y ", "3 ", "7 "], ["n ", "c ", "3 "]],
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
