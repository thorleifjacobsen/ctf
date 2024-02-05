const seq = "AAABAACAADAAEAAFAAGAAHAAIAAJAAKAALAAMAANAAOAAPAAQAARAASAATAAUAAVAAWAAXAAYAAZAAaAAbAAcAAdAAeAAfAAgAAhAAiAAjAAkAAlAAmAAnAAoAApAAqAA"
const list = ["AjAA", "AiAA", "kAAl", "AAnA", "AiAA", "hAAi", "AnAA", "iAAj", "pAAq", "QAAR", "AAlA", "AYAA", "LAAM", "AgAA", "AgAA", "AAiA", "AiAA", "WAAX", "mAAn", "nAAo", "jAAk", "AZAA", "AlAA", "LAAM", "AqAA"]

list.map((x) => {
    process.stdout.write(String.fromCharCode(seq.indexOf(x)));
})

process.stdout.write("\n")