const Plan = document.querySelector(".Plan");

// Número de filas y columnas
const numRows = 20;
const numCols = 20;

// Generación de asientos
for (let row = 1; row <= numRows; row++) {
    for (let col = 1; col <= numCols; col++) {
        const asiento = document.createElement("div");
        asiento.classList.add("asiento");
        asiento.textContent = `${row}-${col}`;
        Plan.appendChild(asiento);
    }
}
