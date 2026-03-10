<script>
    import { onMount } from "svelte";

    let facultades = [];
    let usuarios = [];
    let programas = [];

    let id_estudiante;
    let id_facultad; 
    let id_programa;
    let id_usuario;
    let primer_nombre;
    let primer_apellido;
    let tipo_identificacion;
    let numero_identificacion;
    let genero;
    let telefono;
    let direccion;
    let fecha_registro; 

    onMount(async () => {
        const response = await fetch("https://fastapi1-production-5179.up.railway.app/usuarios/get_usuarios/")
        const data = await response.json();
        usuarios = data.resultado;
    })

    onMount(async () => {
        const response = await fetch("https://fastapi1-production-5179.up.railway.app/facultades/get_facultades/");
        const data = await response.json();
        facultades = data.resultado;
    });

    $: if(id_facultad){
        fetchProgramas(id_facultad);
    } else {
        programas = [];
    }

    async function fetchProgramas(facultadId) {
        try {
            const response = await fetch(`https://fastapi1-production-5179.up.railway.app/programas/get_programas_por_facultad/${facultadId}`);
            const data = await response.json();
            programas = data.resultado;
        } catch (error) {
            console.error("Error al cargar programas:", error);
        }
    }

     function limpiarCampos(data){
        Object.keys(data).forEach(key => {
            if(data[key] === "" || data[key] === undefined){
                data[key] = null;
            }
        });
        return data;
    }

    async function submitForm(event) {
        event.preventDefault();

        let formData = {
            id_estudiante,
            id_facultad,
            id_programa,
            id_usuario,
            primer_nombre,
            primer_apellido,
            tipo_identificacion,
            numero_identificacion,
            genero,
            telefono,
            direccion,
            fecha_registro
        }

        formData = limpiarCampos(formData);

        try {
            const response = await fetch("https://fastapi1-production-5179.up.railway.app/estudiantes/create_estudiante", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            })

            const data = await response.json()

            if(response.ok){
                alert("Estudiante registrado correctamente")

            }else{
                alert(data.detail || "Error al registrar usuario")
            }

        } catch (error) {
            console.error(error)
        }
    }
</script>

<div class="body">
<div>

<form on:submit={submitForm}>
<div>
<label>Facultad:
<select bind:value={id_facultad} required>
<option value="">Seleccione una facultad</option>
{#each facultades as facultad}
<option value={facultad.id_facultad}>{facultad.nombre}</option>
{/each}
</select>
</label>
</div>

<div>
<label>Programa
<select bind:value={id_programa} required>
<option value="">Seleccione un programa</option>
{#each programas as programa}
<option value={programa.id_programa}>{programa.nombre}</option>
{/each}
</select>
</label>
</div>

<div>
<label>Enfermera que atendió la consulta
<select bind:value={id_usuario} required>
<option value="">Seleccione usuario</option>
{#each usuarios as usuario}
<option value={usuario.id_usuario}>{usuario.primer_nombre + " " + usuario.primer_apellido}</option>
{/each}
</select>
</label>
</div>

<div>
<label>Primer Nombre
<input type="text" bind:value={primer_nombre} placeholder="Primer nombre" required>
</label>
</div>

<div>
<label>Primer Apellido
<input type="text" bind:value={primer_apellido} placeholder="Primer apellido" required>
</label>
</div>

<div>
<label>Tipo de Identificación
<select bind:value={tipo_identificacion} required>
<option value="">Seleccione</option>
<option value="CC">Cédula</option>
<option value="TI">Tarjeta de identidad</option>
<option value="CE">Cédula de extranjería</option>
</select>
</label>
</div>

<div>
<label>Número de Identificación
<input type="text" bind:value={numero_identificacion} placeholder="Número de identificación" required>
</label>
</div>

<div>
<p class="genero">Género
<label>Masculino
<input type="radio" value="Masculino" bind:group={genero}>
</label>

<label>Femenino
<input type="radio" value="Femenino" bind:group={genero}>
</label>
</p>
</div>

<div>
<label>Teléfono
<input type="tel" bind:value={telefono} placeholder="Número de teléfono">
</label>
</div>

<div>
<label>Dirección
<input type="text" bind:value={direccion} placeholder="Dirección">
</label>
</div>

<div>
<label>Fecha de registro
<input type="datetime-local" bind:value={fecha_registro} placeholder="Fecha de registro">
</label>
</div>

<button type="submit">Agregar información</button>

</form>

</div>
</div>

<style>
/* Reset básico */
*{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

/* Fondo general */
.body{
    background: #f4f7fb;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

/* Contenedor del formulario */
form{
    background: white;
    padding: 35px;
    border-radius: 12px;
    width: 100%;
    max-width: 750px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
}

/* Separación entre campos */
form div{
    margin-bottom: 18px;
}

/* Labels */
label{
    display: block;
    font-size: 14px;
    font-weight: 600;
    color: #34495e;
    margin-bottom: 6px;
}

/* Inputs */
input, select{
    width: 100%;
    padding: 10px 12px;
    border-radius: 8px;
    border: 1px solid #dcdfe6;
    font-size: 14px;
    transition: all 0.2s ease;
}

/* Focus */
input:focus, select:focus{
    outline: none;
    border-color: #2f80ed;
    box-shadow: 0 0 0 2px rgba(47,128,237,0.15);
}

/* Radio buttons */
input[type="radio"]{
    width: auto;
    margin-left: 6px;
    margin-right: 4px;
}

/* Texto de preguntas */
p{
    font-size: 14px;
    font-weight: 600;
    color: #34495e;
    margin-bottom: 8px;
}

/* Botón */
button{
    width: 100%;
    padding: 12px;
    background: #2f80ed;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.25s ease;
}

/* Hover botón */
button:hover{
    background: #1c65c8;
}

/* Responsive */
@media (min-width: 600px){

    form{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
    }

    form div{
        margin-bottom: 0;
    }

    /* Botón ocupa todo el ancho */
    button{
        grid-column: span 2;
        justify-self: center;
        width: 100%;
    }

}
</style>

