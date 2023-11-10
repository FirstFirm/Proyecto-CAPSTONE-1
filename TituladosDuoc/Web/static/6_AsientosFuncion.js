const planIzquierda = document.querySelector(".plan-izquierda");
const planDerecha = document.querySelector(".plan-derecha");
const confirmarBtn = document.querySelector(".confirmar");
const triggerElement = document.querySelector("#sidebar-trigger");
const sidebarDesplegable = document.querySelector("#sidebar-desplegable");
const cerrarSidebarBtn = document.querySelector("#cerrar-sidebar");
let sidebarVisible = false;

let selectedSeat = null;

const numRowsPerGroup = 12;
const numColsPerGroup = 9;

for (let row = 1; row <= numRowsPerGroup; row++) {
    const seatRow = document.createElement("div");
    seatRow.classList.add("seat-row");
    for (let col = 1; col <= numColsPerGroup; col++) {
        const asiento = document.createElement("div");
        asiento.classList.add("asiento");
        const seatNumber = (row - 1) * numColsPerGroup + col;
        asiento.textContent = seatNumber;
        seatRow.appendChild(asiento);

        asiento.addEventListener("click", () => {
            toggleSeatSelection(asiento);
        });
    }
    planIzquierda.appendChild(seatRow);
}

for (let row = 1; row <= numRowsPerGroup; row++) {
    const seatRow = document.createElement("div");
    seatRow.classList.add("seat-row");
    for (let col = 1; col <= numColsPerGroup; col++) {
        const asiento = document.createElement("div");
        asiento.classList.add("asiento");
        const seatNumber = (row - 1) * numColsPerGroup + col + 108;
        asiento.textContent = seatNumber;
        seatRow.appendChild(asiento);

        asiento.addEventListener("click", () => {
            toggleSeatSelection(asiento);
        });
    }
    planDerecha.appendChild(seatRow);
}

function toggleSidebar() {
    if (!sidebarVisible) {
        sidebarDesplegable.style.right = "0"; 
    } else {
        sidebarDesplegable.style.right = "-250px";
    }
    sidebarVisible = !sidebarVisible;
}

triggerElement.addEventListener("click", toggleSidebar);
