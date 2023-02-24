

const canvas = document.getElementById("pizarra");
const contexto = canvas.getContext("2d");
const COLOR = "black"
const GROSOR = 2;
let xAnterior = 0, yAnterior = 0, xActual = 0, yActual=0;
const obtenerXReal = (clientX) => clientX - canvas.getBoundingClientRect().left;
const obteneryReal = (clientY) => clientY - canvas.getBoundingClientRect().top;
let haComenzadoDibujo = false;
canvas.addEventListener("mousedown", evento => {
    xAnterior = xActual;
    yAnterior = yActual;
    xActual = obtenerXReal(evento.clientX);
    yActual = obteneryReal(evento.clientY);
    contexto.beginPath();
    contexto.fillStyle = COLOR;
    contexto.fillRect(xActual, yActual, GROSOR, GROSOR);
    contexto.closePath();
    haComenzadoDibujo = true
});

canvas.addEventListener("mousemove", (evento) => {
    if (!haComenzadoDibujo) {
        return;
    }
    xAnterior = xActual;
    yAnterior = yActual;
    xActual = obtenerXReal(evento.clientX);
    yActual = obteneryReal(evento.clientY);
    contexto.beginPath(); 
    contexto.moveTo(xAnterior, yAnterior);
    contexto.lineTo(xActual, yActual);
    contexto.strokeStyle = COLOR;
    contexto.lineWith = GROSOR;
    contexto.stroke()
    contexto.closePath();
});
["mouseup", "mouseout"].forEach(nombreDeEvento =>{
    canvas.addEventListener(nombreDeEvento, ()=>{
        haComenzadoDibujo = false
    });
});

var limpiar = document.getElementById("boton");
limpiar.addEventListener("click", function(){
    canvas.width = canvas.width;
}, false);


var mdoelo = null;
//Cargar modelo
(async () => {
    console.log("Creando modelo...");
    modelo = await tf.loadLayersModel("./Modelo_AI/model.json");
    console.log("Modelo Cargado");
})();

// async predit(img)

// const pred = await tf.tidy(()=>{
//     let img = tf.fromPixel(im)
// })


//https://parzibyte.me/blog/2021/09/08/dibujar-canvas-mouse-javascript/
