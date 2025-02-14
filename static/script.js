function generateQRCode() {
    let data = document.getElementById("data").value;
    let size = document.getElementById("size").value;
    let bg_color = document.getElementById("bg_color").value;
    let format = document.getElementById("format").value;

    if (!data.trim()) {
        alert("Please enter text or a URL.");
        return;
    }

    fetch("/generate", {
        method: "POST",
        body: JSON.stringify({ data, size, bg_color, format }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("qrImage").src = data.qr_code_url;
        document.getElementById("qrPreview").style.display = "block";
        document.getElementById("downloadLink").href = "/download?format=" + format;
        document.getElementById("downloadLink").style.display = "block";
    })
    .catch(error => console.error("Error:", error));
}

// Reset function
function resetForm() {
    document.getElementById("qrForm").reset();
    document.getElementById("qrPreview").style.display = "none";
    document.getElementById("qrImage").src = "";
    document.getElementById("downloadLink").style.display = "none";
}

// Dark Mode Toggle
function toggleDarkMode() {
    const body = document.body;
    const container = document.querySelector(".container");
    const toggleButton = document.getElementById("darkModeToggle");
    
    body.classList.toggle("dark-mode");
    container.classList.toggle("dark-mode");
    document.querySelectorAll("button").forEach(button => button.classList.toggle("dark-mode"));
    document.querySelectorAll("input, select").forEach(element => element.classList.toggle("dark-mode"));
    document.getElementById("qrPreview").classList.toggle("dark-mode");
    
    // Toggle text and emoji
    if (body.classList.contains("dark-mode")) {
        toggleButton.innerHTML = "Light Mode 🌞";
        toggleButton.classList.remove("sun-mode");
    } else {
        toggleButton.innerHTML = "Dark Mode 🌙";
        toggleButton.classList.add("sun-mode");
    }
}
