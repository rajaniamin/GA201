const URL = "./my_model/giL8aVLYH/"; // Update this with your model URL

let model, webcam, labelContainer, maxPredictions;

async function init() {
  const modelURL = URL + "model.json";
  const metadataURL = URL + "metadata.json";

  model = await tmImage.load(modelURL, metadataURL);
  maxPredictions = model.getTotalClasses();

  const flip = true; // whether to flip the webcam
  webcam = new tmImage.Webcam(200, 200, flip);
  await webcam.setup();
  await webcam.play();
  window.requestAnimationFrame(loop);

  const webcamContainer = document.getElementById("webcam-container");
  webcamContainer.appendChild(webcam.canvas);

  labelContainer = document.getElementById("label-container");
  for (let i = 0; i < maxPredictions; i++) {
    const labelDiv = document.createElement("div");
    labelDiv.classList.add("label-prediction");
    labelContainer.appendChild(labelDiv);
  }
}

async function loop() {
  webcam.update();
  await predict();
  window.requestAnimationFrame(loop);
}

async function predict() {
  const prediction = await model.predict(webcam.canvas);
  for (let i = 0; i < maxPredictions; i++) {
    const classPrediction =
      prediction[i].className + ": " + prediction[i].probability.toFixed(2);
    labelContainer.childNodes[i].innerHTML = classPrediction;
  }
}
