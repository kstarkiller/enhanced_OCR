const video = document.querySelector("#video");
var streamRef;

function toggleWebcam() {
  if (streamRef) {
    streamRef.getTracks().forEach((track) => track.stop());
    streamRef = null;
    video.srcObject = null;
  } else {
    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then(function (stream) {
        video.srcObject = stream;
        streamRef = stream; 
      })
      .catch(function (error) {
        console.log("Error!");
      });
  }
}

if (navigator.mediaDevices.getUserMedia) {
  toggleWebcam();
}

const button = document.getElementById("save-webcam-pic");
const canvas = document.createElement("canvas");
const context = canvas.getContext("2d");

button.addEventListener("click", function () {
  canvas.width = video.offsetWidth;
  canvas.height = video.offsetWidth * (video.videoHeight / video.videoWidth);

  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  const image = canvas.toDataURL("../data/photo");

  const link = document.createElement("a");
  link.href = image;
  link.download = "picture.png";

  link.click();
});

document
  .getElementById("toggle-webcam")
  .addEventListener("click", toggleWebcam);
