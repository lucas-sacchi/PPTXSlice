document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("divisions").addEventListener("change", generateInputs);
    document.getElementById("pptxForm").addEventListener("submit", executeSplit);
});

function generateInputs() {
    let divisions = document.getElementById("divisions").value;
    let slideInputs = document.getElementById("slideInputs");
    slideInputs.innerHTML = "";

    for (let i = 1; i <= divisions; i++) {
        let div = document.createElement("div");
        div.className = "slide-range";
        div.innerHTML = `
            <label>PPTX ${i}:</label>
            <input type="text" class="file-name" placeholder="Nome do arquivo ${i}">
            <br>
            <label>Página Inicial </label>
            <input type="number" class="start-slide" min="1">
            <label> Página Final: </label>
            <input type="number" class="end-slide" min="1">
        `;
        slideInputs.appendChild(div);
    }
}

function executeSplit(event) {
    event.preventDefault();
    
    let alertBox = document.getElementById("alertBox");
    alertBox.style.display = "none";
    alertBox.innerHTML = ""; // Limpa qualquer mensagem anterior

    let formData = new FormData();
    let fileInput = document.getElementById("file");
    
    if (fileInput.files.length === 0) {
        showAlert("Por favor, selecione um arquivo PowerPoint.");
        return;
    }

    formData.append("file", fileInput.files[0]);

    let slideRanges = [];
    let fileNames = [];
    let missingFields = false;

    document.querySelectorAll(".slide-range").forEach((div) => {
        let fileName = div.querySelector(".file-name").value.trim();
        let start = div.querySelector(".start-slide").value;
        let end = div.querySelector(".end-slide").value;

        if (!fileName || !start || !end) {
            missingFields = true;
        }

        slideRanges.push(`${start}-${end}`);
        fileNames.push(fileName);
    });

    if (missingFields) {
        showAlert("Por favor, preencha todos os campos antes de executar.");
        return;
    }

    slideRanges.forEach((range) => {
        formData.append("slideRanges[]", range);
    });

    fileNames.forEach((name) => {
        formData.append("fileNames[]", name);
    });

    fetch("/split_pptx", {
        method: "POST",
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        let url = window.URL.createObjectURL(blob);
        let a = document.createElement("a");
        a.href = url;
        a.download = "arquivos_divididos.zip"; 
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    })
    .catch(error => console.error("Erro ao dividir:", error));
}

function showAlert(message) {
    let alertBox = document.getElementById("alertBox");
    alertBox.innerHTML = message;
    alertBox.style.display = "block";
}
