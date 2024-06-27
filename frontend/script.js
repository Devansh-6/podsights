document.getElementById('uploadForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData();
    const fileInput = document.getElementById('audioFile');
    formData.append('audioFile', fileInput.files[0]);

    const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('predictionResult').innerText = 'Prediction: ' + result.prediction;
});
