function displayFileName(input) {
    const fileNameDisplay = document.getElementById('fileNameDisplay');
    if (input.files && input.files[0]) {
        const fileName = input.files[0].name;
        fileNameDisplay.innerHTML = `<span class="file-icon">📄</span> ${fileName}`;
    } else {
        fileNameDisplay.innerHTML = '';
    }
}