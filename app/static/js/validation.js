// validation.js

function validateForm() {
    var fileInput = document.getElementById('json_file');
    var textAreaInput = document.getElementById('json_data');

    // Check if either file or JSON data is present
    if (!fileInput.files.length && !textAreaInput.value.trim()) {
        alert('Please upload a JSON file or paste JSON data before submitting.');
        return false;
    }

    return true;
}
