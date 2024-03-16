function getInputFile() {
    let fileInput = document.getElementById("file");
    if (fileInput.length == 0) {
        return;
    }
    return fileInput.files[0];
}

function blobToBase64(blob) {
    return new Promise((resolve, _) => {
        let reader = new FileReader();
        reader.onloadend = () => resolve(reader.result);
        reader.readAsDataURL(blob);
    });
}

async function displayImage(blob) {
    blob = blob.slice(0, blob.size, "image/png");
    var dataUrl = await blobToBase64(blob);

    let resultImage = document.getElementById("resized_img");
    resultImage.src = dataUrl;

    let resultDownload = document.getElementById("resized_download");
    resultDownload.href = dataUrl;

    document.getElementById("results").style.display = "flex";
}

function download(text, name, type) {
    var a = document.getElementById("a");
    var file = new Blob([text], { type: type });
    a.href = URL.createObjectURL(file);
    a.download = name;
}

async function onSubmit(event) {
    event.preventDefault();
    console.log("resizing file");
    file = getInputFile();
    if (file) {
        let response = await fetch("/resize", { method: "POST", body: file });
        if (response.ok) {
            let content = await response.blob();
            displayImage(content);
        } else {
            console.log(`resize failed: ${response.status}`);
        }
    }
}

const form = document.getElementById("form");
form.addEventListener("submit", onSubmit);
