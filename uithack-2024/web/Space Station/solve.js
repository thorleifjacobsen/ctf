
const decrypt = (encrypted, rotors) => {
    let result = "";
    for (let i = 0; i < encrypted.length; i++) {
        let char = encrypted[i];
        let rotor1 = rotors.rotor1[char];
        let rotor2 = rotors.rotor2[rotor1];
        let rotor3 = rotors.rotor3[rotor2];
        result += rotor3;
    }
    return result;
}

fetch("https://uithack.td.org.uit.no:8009/get_rotors").then(response => response.json()).then(rotors => {
    fetch("https://uithack.td.org.uit.no:8009/get_encrypted").then(response => response.json()).then(encrypted => {
        const key = decrypt(encrypted[0], rotors[0]);
        // Post as form data where key is decrypted and value is the decrypted string
        fetch("https://uithack.td.org.uit.no:8009/post_decrypt", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ key })
        }).then(response => response.text()).then(console.log);
    });
});