function drawRectangle() {
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");
    
    const width = parseInt(document.getElementById("width").value);
    const height = parseInt(document.getElementById("height").value);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < width / 10; i++) {
        for (let j = 0; j < height / 10; j++) {
            const myRand = Math.random()
            if (myRand < 0.33) {
                ctx.fillStyle = "red";    
            } else if (myRand < 0.66) {
                ctx.fillStyle = "black";    
            } else {
                ctx.fillStyle = "blue";    
            }
            ctx.fillRect(i * 10, j * 10, (i + 1) * 10, (j + 1) * 10);                    
        }
    }    
  }