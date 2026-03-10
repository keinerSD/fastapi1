<script>
    let tipo_identificacion;
    let numero_identificacion;
    let estudiante = null;
    let encontrado = null; // true si existe, false si no

    async function search_student(event) {
    event.preventDefault();

    try {
        const response = await fetch(`https://fastapi1-production-5179.up.railway.app/estudiantes/get_estudiante/${numero_identificacion}`);

        if (response.ok) {
            const data = await response.json();

            estudiante = data.resultado ? data.resultado : data;
            encontrado = true;

            console.log("Estudiante encontrado:", estudiante);

        } else if (response.status === 404) {

            console.log("Estudiante no encontrado");

            estudiante = null;
            encontrado = false;

        } else {
            console.log("Otro error del servidor");
        }

    } catch (error) {
        console.error("Error en fetch:", error);
    }

    }
    function nuevaConsulta() {
    if (estudiante) {
        window.location.href = `/create_query?id_estudiante=${estudiante.id_estudiante}`;
    }
    }

    function registrarEstudiante() {
    window.location.href = "/create_students";
    }
</script>


<div class="container">

    <h1>Buscar estudiante</h1>

    <form on:submit={search_student}>
        <div>
            <label>Tipo de documento
                <select bind:value={tipo_identificacion}>
                    <option value="CC">Cédula de Ciudadanía</option>
                    <option value="TI">Tarjeta de Identidad</option>
                    <option value="CE">Cédula de Extranjería</option>
                </select>
            </label>
        </div>
        
        <div>
            <label>Documento de identidad
                <input type="text" placeholder="Ingrese el número de documento" bind:value={numero_identificacion}>
            </label>
        </div>
        
        <button type="submit">Buscar estudiante</button>
    </form>

    {#if encontrado === true && estudiante}
    <h2>Estudiante encontrado:</h2>
    <table>
        <tbody>
            <tr><th>Primer Nombre: </th><td>{estudiante.primer_nombre}</td></tr>
            <tr><th>Primer Apellido: </th><td>{estudiante.primer_apellido}</td></tr>
            <tr><th>Tipo de Identificación: </th><td>{estudiante.tipo_identificacion}</td></tr>
            <tr><th>Número de Identificación: </th><td>{estudiante.numero_identificacion}</td></tr>
            <tr><th>Género: </th><td>{estudiante.genero}</td></tr>
            <tr><th>Teléfono: </th><td>{estudiante.telefono}</td></tr>
            <tr><th>Dirección: </th><td>{estudiante.direccion}</td></tr>
            <tr><th>Fecha de Registro: </th><td>{estudiante.fecha_registro}</td></tr>
        </tbody>
    </table>
    <button on:click={nuevaConsulta}>Crear nueva consulta</button>
    {:else if encontrado === false}
    <p>Estudiante no encontrado</p>
    <button on:click={registrarEstudiante}>Registrar estudiante</button>
    {/if}

</div>


<style>

/* Reset */
*{
    box-sizing:border-box;
    margin:0;
    padding:0;
    font-family:"Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

/* Fondo */
.container{
    background:#f4f7fb;
    padding:40px;
}

/* Contenedor */
.container{
    max-width:500px;
    margin:0 auto;
}

/* Título */
h1{
    text-align:center;
    margin-bottom:25px;
    color:#34495e;
}

/* Formulario */
form{
    background:white;
    padding:35px;
    border-radius:12px;
    box-shadow:0 8px 25px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

/* Espaciado */
form div{
    margin-bottom:18px;
}

/* Label */
label{
    display:block;
    font-size:14px;
    font-weight:600;
    color:#34495e;
    margin-bottom:6px;
}

/* Inputs */
input, select{
    width:100%;
    padding:10px 12px;
    border-radius:8px;
    border:1px solid #dcdfe6;
    font-size:14px;
    transition:all 0.2s ease;
}

/* Focus */
input:focus, select:focus{
    outline:none;
    border-color:#2f80ed;
    box-shadow:0 0 0 2px rgba(47,128,237,0.15);
}

/* Botón */
button{
    width:100%;
    padding:12px;
    background:#2f80ed;
    color:white;
    border:none;
    border-radius:8px;
    font-size:15px;
    font-weight:600;
    cursor:pointer;
    transition:background 0.25s ease;
}

button:hover{
    background:#1c65c8;
}

</style>