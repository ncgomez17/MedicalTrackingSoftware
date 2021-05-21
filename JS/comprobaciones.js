
function comprobar_registro() {
    const nss = document.getElementById("nss");
    const paciente = document.getElementById("paciente");
    const domicilio = document.getElementById("domicilio");
    const telefono = document.getElementById("telefono");
    const codmedico = document.getElementById("codMedico");
    const nombremedico = document.getElementById("nombreMedico");


    var toret = false;

    if (nss.value.trim().length > 0 && paciente.value.trim().length > 0 && domicilio.value.trim().length > 0 && telefono.value.trim().length > 0
        && codmedico.trim().length > 0 && nombremedico.value.trim().length > 0) {
        toret = true;
    }
    if (toret == false) {
        alert("Rellena todos los campos por favor");
    }
    return toret;
};

function comprobar_diagnostico() {
    const nss = document.getElementById("nss");
    const paciente = document.getElementById("paciente");
    const tipo = document.getElementById("tipo_diagnostico");


    var toret = false;

    if (nss.value.trim().length > 0 && paciente.value.trim().length > 0 && tipo.value.trim().length > 0) {
        toret = true;
    }
    if (toret == false) {
        alert("Rellena todos los campos por favor");
    }
    return toret;
};

function comprobar_medicamento() {
    const nss = document.getElementById("nss");
    const paciente = document.getElementById("paciente");
    const medicamento = document.getElementById("medicamento");
    const fecha = document.getElementById("fechavencimiento");


    var toret = false;

    if (nss.value.trim().length > 0 && paciente.value.trim().length > 0 && medicamento.value.trim().length > 0
        && fecha.value.trim().length > 0) {
        toret = true;
    }
    if (toret == false) {
        alert("Rellena todos los campos por favor");
    }
    return toret;
};