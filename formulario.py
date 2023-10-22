< !DOCTYPE
html >
< html >
< heard >
< title > Pagina
Shirley < / title >
< style >
body
{background - color: pink}
h1
{color: black;}
p1
{color: black;}
p
{color: red;}
< / style >
< / heard >
< body >
< h1 > Formulario < / h1 >
< p1 > Ingreso
de
datos < / p1 >
< form >
< p >
< label
for ="nombre" > Nombre: <
    label / >
< input
type = "text"
name = "nombre"
id = "nombre" >
< / p >
< p >
< label
for ="apellido" > Apellido: <
    label / >
< input
type = "text"
name = "apellido"
id = "apellido" >
< / p >
< p >
< label
for ="edad" > Edad: <
    label / >
< input
type = "number"
name = "Edad"
id = "edad" >
< / p >
< p > Sexo: < / p >
< form
action = "/action_page.php" >
< input
type = "radio"
id = "mujer"
name = "sexo"
value = "MUJER" >
< label
for ="mujer" > Mujer < /label > < br >
< input
type = "radio"
id = "hombre"
name = "sexo"
value = "Hombre" >
< label
for ="hombre" > Hombre < /label > < br >

< p >
< label
for ="nivel de estudios" > Nivel de estudios < /label >
< select
id = "nivel de estudios"
name
"nivel de estudios" >
< option
value = "primaria" > primaria < / option >
< option
value = "bachillerato" > bachillerato < / option >
< option
value = "superior" > superior < / option >
< / select >
< / p >
< p >
< label
for ="usuario" > Usuario:<
    label / >
< input
type = "text"
name = "usuario"
id = "usuario" >
< / p >
< p >
< label
for ="contrasena" > Contraseña: <
    label / >
< input
type = "text"
name = "contrasena"
id = "contrasena" >
< / p >
< p >
< label
for ="contrasena" > Confirmacion de contraseña: <
    label / >
< input
type = "text"
name = "contrasena"
id = "contrasena" >
< / p >
< style >
table, th, td
{
    border: 1px solid black;
}
< / style >
< body >

< h2 > Tabla
de
Datos < / h2 >

< table
style = "width:100%" >
< tr >
< th > Nombre < / th >
< th > Apellido < / th >
< th > Sexo < / th >
< th > Nivel
de
estudio < / th >
< th > Usuario < / th >
< / tr >
< tr >
< td > Peter < / td >
< td > Villamar < / td >
< td > Hombre < / td >
< td > Bachillerato < / td >
< td > Peterv < / td >
< / tr >
< tr >
< td > Shirley < / td >
< td > Olvera < / td >
< td > Mujer < / td >
< td > Superior < / td >
< td > Olver < / td >
< / tr >
< / table > < br >

< button
type = "button"
onclick = "alert('Hola, Bienvenido!')" > Click! < / button >

< form / >
< / p >
< / body >
< / html >