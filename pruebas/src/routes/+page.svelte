<script>

    let email = ""
    let password = ""

    async function login(event){

        event.preventDefault()

        const usuario = {
            email: email,
            password: password
        }

        try{
            const response = await fetch("https://fastapi1-production-5179.up.railway.app/login", {
                method: "POST",
                headers:{
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(usuario)
            });

            const data = await response.json()

            console.log(data)

            if(response.ok){
                alert("Login exitoso")
                window.location.href = "/search_student"
            }else{
                alert(data.detail || "Credenciales inválidas")
            }

        }catch(error){
            console.error(error)
        }

    }

</script>


<div class="container">

    <h1>Bienvenido a la página</h1>

    <form on:submit={login}>

        <div>
            <label>Email
            <input type="text" bind:value={email} required>
            </label>
        </div>

        <div>
            <label>Password
            <input type="password" bind:value={password} required>
            </label>
        </div>

        <button type="submit">Iniciar sesión</button>

        <a class="register-link" href="/register">
            ¿No tienes una cuenta? Regístrate aquí
        </a>

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
    margin-bottom:15px;
}

button:hover{
    background:#1c65c8;
}

/* Link registro */
.register-link{
    display:block;
    text-align:center;
    font-size:14px;
    color:#2f80ed;
    text-decoration:none;
}

.register-link:hover{
    text-decoration:underline;
}

</style>