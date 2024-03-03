document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById("drawing");
    const context = canvas.getContext("2d");
    context.fillStyle = "#ffff";
    context.fillRect(0, 0, canvas.width, canvas.height);

    let isDrawing = false;

    function startDrawing(e) {
        isDrawing = true;
        draw(e);
    }

    function stopDrawing() {
        isDrawing = false;
        context.beginPath();
    }

    function draw(e) {
        if (!isDrawing) return;

        context.lineWidth = 5;
        context.lineCap = "round";
        context.strokeStyle = "#000";

        context.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
        context.stroke();
        context.beginPath();
        context.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    }

    canvas.addEventListener("mousedown", startDrawing);
    canvas.addEventListener("mouseup", stopDrawing);
    canvas.addEventListener("mousemove", draw);
});

function saveDrawing() {
    const canvas = document.getElementById("drawing");
    const context = canvas.getContext("2d");
    const imgData = canvas.toDataURL("../data/drawing");

    const link = document.createElement("a");
    link.href = imgData;
    link.download = "drawing.png";
    link.click();
}

function clearDrawing() {
    const canvas = document.getElementById("drawing");
    const context = canvas.getContext("2d");
    context.clearRect(0, 0, canvas.width, canvas.height);
    
    context.fillStyle = "#fff";
    context.fillRect(0, 0, canvas.width, canvas.height);
}