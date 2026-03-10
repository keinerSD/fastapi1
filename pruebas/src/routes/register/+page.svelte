<script>

    let primer_nombre;
    let primer_apellido;
    let email;
    let password;

    async function register(event){

        event.preventDefault()

        const usuario = {
            primer_nombre,
            primer_apellido,
            email,
            password
        }

        try{

            const response = await fetch("https://fastapi1-production-5179.up.railway.app/register", {
                method: "POST",
                headers:{
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(usuario)
            })

            const data = await response.json()

            console.log(data)

            if(response.ok){
                alert("Usuario registrado correctamente")
                window.location.href = "/login"
            }else{
                alert(data.detail || "Error al registrar usuario")
            }

        }catch(error){
            console.error(error)
        }

    }

</script>


<div class="container">

    <h1>Registro de usuario</h1>

    <form action="/login" on:submit={register}>

        <div>
            <label>Nombre
            <input type="text" bind:value={primer_nombre} required>
            </label>
        </div>

        <div>
            <label>Apellido
            <input type="text" bind:value={primer_apellido} required>
            </label>
        </div>

        <div>
            <label>Email
            <input type="email" bind:value={email} required>
            </label>
        </div>

        <div>
            <label>Contraseña
            <input type="password" bind:value={password} required>
            </label>
        </div>

        <button type="submit">Registrarse</button>

    </form>

</div>


<style>

/* Reset básico */
*{
    box-sizing:border-box;
    margin:0;
    padding:0;
    font-family:"Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

/* Fondo general */
.container{
    background:#f4f7fb;
    padding:40px;
}

/* Contenedor centrado */
.container{
    max-width:600px;
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
}

/* Separación entre campos */
form div{
    margin-bottom:18px;
}

/* Labels */
label{
    display:block;
    font-size:14px;
    font-weight:600;
    color:#34495e;
    margin-bottom:6px;
}

/* Inputs */
input{
    width:100%;
    padding:10px 12px;
    border-radius:8px;
    border:1px solid #dcdfe6;
    font-size:14px;
    transition:all 0.2s ease;
}

/* Focus */
input:focus{
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

/* Hover */
button:hover{
    background:#1c65c8;
}

/* Responsive */
@media (min-width:600px){

    form{
        display:grid;
        grid-template-columns:1fr 1fr;
        gap:20px;
    }

    form div{
        margin-bottom:0;
    }

    button{
        grid-column:span 2;
        width:250px;
        justify-self:center;
    }

}

</style>