const planIzquierda = document.querySelector(".plan-izquierda");
const planDerecha = document.querySelector(".plan-derecha");
const confirmarBtn = document.querySelector(".confirmar");

const numRowsPerGroup = 12;  
const numColsPerGroup = 20;  


for (let row = 1; row <= numRowsPerGroup; row++) {
    const seatRowIzquierda = document.createElement("div");
    seatRowIzquierda.classList.add("seat-row");
  
    for (let col = 1; col <= numColsPerGroup; col++) {
      const asientoIzquierda = document.createElement("div");
      asientoIzquierda.classList.add("asiento");
  
      const seatNumberIzquierda = (col - 1) * numRowsPerGroup + row;
  
      asientoIzquierda.textContent = seatNumberIzquierda;
      seatRowIzquierda.appendChild(asientoIzquierda);
  
      asientoIzquierda.addEventListener("click", () => {
        toggleSeatSelection(asientoIzquierda);
      });
    }
  
    planIzquierda.appendChild(seatRowIzquierda);
  }
  
  for (let row = 1; row <= numRowsPerGroup; row++) {
    const seatRowDerecha = document.createElement("div");
    seatRowDerecha.classList.add("seat-row");
  
    for (let col = 1; col <= numColsPerGroup; col++) {
      const asientoDerecha = document.createElement("div");
      asientoDerecha.classList.add("asiento");
  
      const seatNumberDerecha = (col - 1) * numRowsPerGroup + row + 250; // Modificado
  
      asientoDerecha.textContent = seatNumberDerecha;
      seatRowDerecha.appendChild(asientoDerecha);
  
      asientoDerecha.addEventListener("click", () => {
        toggleSeatSelection(asientoDerecha);
      });
    }
  
    planDerecha.appendChild(seatRowDerecha);
  }

/*confirmarBtn.addEventListener("click", () => {
    if (selectedSeat) {
        alert(`Has seleccionado el asiento: ${selectedSeat.textContent}`);
    } else {
        alert("Por favor, selecciona un asiento.");
    }
});*/

/*function toggleSeatSelection(seat) {
    if (selectedSeat && selectedSeat !== seat) {
        selectedSeat.classList.remove("selected");
    }
    if (!seat.classList.contains("selected")) {
        seat.classList.add("selected");
        selectedSeat = seat;
    } else {
        seat.classList.remove("selected");
        selectedSeat = null;
    }
}*/


/* function toggleSidebar() {
    if (!sidebarVisible) {
        sidebarDesplegable.style.right = "0"; 
    } else {
        sidebarDesplegable.style.right = "-250px";
    }
    sidebarVisible = !sidebarVisible;
}

triggerElement.addEventListener("click", toggleSidebar);*/
