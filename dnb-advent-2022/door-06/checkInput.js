function checkInput(input = "123456789abcdef") {
    input = Buffer.from(input);

    // Found in the binary.
    let exponent = Buffer.from([0x41, 0x42, 0x43, 0x44]);
    let password = Buffer.from([0x09, 0x23, 0x35, 0x21, 0x18, 0x2d, 0x36, 0x06, 0x24, 0x27, 0x2d, 0x03, 0x71, 0x72, 0x27]);

    if (input.length == 15) { 
        for (let i=0; i<15; i++) {
            if ((input[i] ^ exponent[i % 4]) != password[i]) {
                console.log("Fail!?");
                return 0
            }            
        }
        return 1;
    }
    return 0;
}

console.log(checkInput("HaveYouBeenG00d"));