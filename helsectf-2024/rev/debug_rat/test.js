function xorBuffers(destBuffer, sourceBuffer) {
    let numBytes = destBuffer.length;
    let sourceLength = sourceBuffer.length;

    for (let i = 0; i < numBytes; i++) {
        destBuffer[i] ^= sourceBuffer[i % sourceLength];
    }
}

// Example usage
let destBuffer = Buffer.from('HELSECTF_IS_SO_MUCH_FUN', 'utf-8');
let sourceBuffer = Buffer.from(Array(destBuffer.length).fill(0x41));
xorBuffers(destBuffer, sourceBuffer);

console.log(destBuffer.toString('hex')); // Output will be the XORed result
