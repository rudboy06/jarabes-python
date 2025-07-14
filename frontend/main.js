const API = "http://localhost:5000/jarabes";
const tabla = document.getElementById("tabla-jarabes");
const formulario = document.getElementById("formulario");
const nombre = document.getElementById("nombre");
const ingredientes = document.getElementById("ingredientes");
const descripcion = document.getElementById("descripcion");
const id = document.getElementById("id");
const canvas = document.getElementById("graficaJarabes");
let chart = null;

function cargarJarabes() {
  fetch(API)
    .then(res => res.json())
    .then(data => {
      tabla.innerHTML = "";
      const conteo = {};

      data.forEach(j => {
        tabla.innerHTML += `
          <tr>
            <td>${j.nombre}</td>
            <td>${j.ingredientes}</td>
            <td>${j.descripcion || ""}</td>
            <td>
              <button class="btn btn-sm btn-warning" onclick='editar(${JSON.stringify(j)})'>Editar</button>
              <button class="btn btn-sm btn-danger" onclick="eliminar(${j.id})">Eliminar</button>
            </td>
          </tr>
        `;

        // Acumular conteo por nombre
        conteo[j.nombre] = (conteo[j.nombre] || 0) + 1;
      });

      actualizarGrafica(conteo);
    });
}

formulario.onsubmit = e => {
  e.preventDefault();
  const jarabe = {
    nombre: nombre.value,
    ingredientes: ingredientes.value,
    descripcion: descripcion.value,
  };

  const metodo = id.value ? "PUT" : "POST";
  const url = id.value ? `${API}/${id.value}` : API;

  console.log("enviando:", jarabe);

  fetch(url, {
    method: metodo,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(jarabe)
  }).then(res => res.json())
.then(data => {
  console.log("Respuesta de la API:", data);
  formulario.reset();
  cargarJarabes(); // Asegúrate de que esto se llame
  });
};

function editar(jarabe) {
  id.value = jarabe.id;
  nombre.value = jarabe.nombre;
  ingredientes.value = jarabe.ingredientes;
  descripcion.value = jarabe.descripcion;
}

function eliminar(idJarabe) {
  fetch(`${API}/${idJarabe}`, { method: "DELETE" }).then(() => cargarJarabes());
}

function actualizarGrafica(data) {
  const labels = Object.keys(data);
  const values = Object.values(data);

  if (chart) chart.destroy(); // Destruir gráfica previa

  chart = new Chart(canvas, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [{
        label: "Cantidad de jarabes",
        data: values,
        backgroundColor: "rgba(54, 162, 235, 0.6)",
        borderColor: "rgba(54, 162, 235, 1)",
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
}

cargarJarabes();
