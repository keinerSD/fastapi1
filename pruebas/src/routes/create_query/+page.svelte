<script>
import { onMount } from "svelte";

let estudiante = null;
let nombre_estudiante = "";
let cedula_estudiante = "";
let id_estudiante = null;

// formulario
let id_usuario = "";
let diagnostico = "";
let observaciones = "";
let motivo_consulta = "";
let fecha_entrada = "";
let fecha_salida = "";

const API_URL = "https://fastapi1-production-5179.up.railway.app";

onMount(async () => {

    const params = new URLSearchParams(window.location.search);
    id_estudiante = params.get("id_estudiante");

    console.log("ID recibido:", id_estudiante);

    if(id_estudiante){
        await cargarEstudiante();
    }

});

async function cargarEstudiante(){

    try{

        const response = await fetch(`${API_URL}/estudiantes/get_estudiante/${id_estudiante}`);

        if(!response.ok){
            console.error("Estudiante no encontrado");
            return;
        }

        const data = await response.json();

        estudiante = data.resultado || data;

        nombre_estudiante = estudiante.primer_nombre + " " + estudiante.primer_apellido;
        cedula_estudiante = estudiante.numero_identificacion;

    }catch(error){
        console.error("Error cargando estudiante", error);
    }

}

async function guardarConsulta(event){

    event.preventDefault();

    const formData = {
        id_estudiante,
        id_usuario,
        diagnostico,
        observaciones,
        motivo_consulta,
        fecha_entrada,
        fecha_salida
    };

    try{

        const response = await fetch(`${API_URL}/consultas/create_consulta`,{
            method:"POST",
            headers:{ "Content-Type":"application/json"},
            body:JSON.stringify(formData)
        });

        const data = await response.json();

        if(response.ok){
            alert("Consulta guardada correctamente");
        }else{
            alert(data.detail || "Error al guardar consulta");
        }

    }catch(error){
        console.error("Error guardando consulta", error);
    }

}
</script>

<div class="container">

<h2>Nueva Consulta</h2>

{#if estudiante}

<div class="info">
<p><strong>Estudiante:</strong> {nombre_estudiante}</p>
<p><strong>Cédula:</strong> {cedula_estudiante}</p>
</div>

{/if}

<form on:submit={guardarConsulta}>

<label>
Enfermera
<input type="text" bind:value={id_usuario} required>
</label>

<label>
Diagnóstico
<input type="text" bind:value={diagnostico}>
</label>

<label>
Observaciones
<input type="text" bind:value={observaciones}>
</label>

<label>
Motivo de consulta
<input type="text" bind:value={motivo_consulta}>
</label>

<label>
Fecha entrada
<input type="date" bind:value={fecha_entrada}>
</label>

<label>
Fecha salida
<input type="date" bind:value={fecha_salida}>
</label>

<button type="submit">Guardar Consulta</button>

</form>

<button class="rojo">¡¡¡¡EMERGENCIAS!!!!</button>

</div>

<style>

.container{
max-width:700px;
margin:auto;
padding:40px;
background:#f4f7fb;
font-family:Segoe UI;
}

h2{
text-align:center;
margin-bottom:20px;
}

form{
background:white;
padding:25px;
border-radius:10px;
box-shadow:0 5px 15px rgba(0,0,0,0.1);
}

label{
display:block;
margin-bottom:15px;
}

input{
width:100%;
padding:8px;
border-radius:6px;
border:1px solid #ccc;
}

button{
padding:10px 15px;
background:#2f80ed;
color:white;
border:none;
border-radius:6px;
cursor:pointer;
}

.rojo{
background:red;
margin-top:30px;
}

.info{
background:white;
padding:15px;
margin-bottom:20px;
border-radius:8px;
}

</style>