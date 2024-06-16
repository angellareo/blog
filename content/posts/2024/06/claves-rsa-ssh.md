Title: Claves RSA para conexiones SSH
Slug: claves-rsa-ssh
Date: 2024-06-08 12:39
Category: General
Tags: ssh, RSA
Author: Angel Lareo
Cover: images/ssh_server.png
Summary: Te cuento cómo conectar por SSH a tu(s) servidor(es) usando claves RSA


Los que administramos servidores nos pasamos el día conectando por SSH a distintas máquinas. Hacerlo mediante pares de claves RSA (pública y privada) nos aporta distintas ventajas de seguridad:


- Las claves RSA (generalmente de 2048 bits o más) son extremadamente difíciles de descifrar en comparación con una contraseña típica. 
- Las claves RSA no necesitan ser recordadas ni ingresadas manualmente, lo que elimina el riesgo de que alguien las observe o las adivine.
- Al cifrar con AES la clave privada mediante contraseña añadimos un factor adicional de seguridad, que impedirá el acceso a nuestros servidores incluso si nuestro sistema es comprometido.


# Generar el par de claves

Vamos a generar un par de claves RSA de 4096 bits:
```
ssh-keygen -t rsa -b 4096
# Podemos indicar el nombre y la ruta para el par de claves
# Por defecto se generará en ~/.ssh/id_rsa
# Podemos elegir (y recomiendo) cifrar la clave privada con una contraseña
```

La mayoría de tutoriales utilizan la ruta por defecto, aquí vamos a seguir otra vía: utilizar una clave específica para cada par de usuario-servidor. En adelante supondremos que hemos generado el par de claves `~/.ssh/usuario_servidor_rsa` (la clave pública estará en la misma ruta, en un segundo fichero terminado en `.pub`).

Si hemos elegido no cifrar la clave privada y cambiamos de opinión, o si la hemos cifrado con una contraseña que deseamos cambiar, podemos utilizar:
```
ssh-keygen -p -f ~/.ssh/usuario_servidor_rsa
```

# Instalar clave en nuestro servidor
 Ahora procedemos a instalar la clave pública en nuestro usuario del server. Suponemos que nuestro usuario es `usuario` y nuestro servidor es `servidor.es`. Para elegir la clave a copiar utilizaremos el parámetro `-i <ruta-a-la-clave>`:
```
ssh-copy-id -i ~/.ssh/usuario_servidor_rsa usuario@servidor.es
```
Nos pedirá la contraseña que habitualmente utilizamos para conectarnos e instalará la clave pública en la ruta `~/.ssh/authorized_keys` de nuestro servidor (puedes confirmarlo haciendo `cat` de este archivo). Esto le indica al servidor que el usuario que disponga de la clave privada que encaje con la clave pública que acabamos de instalar está autorizado a conectarse. Vamos a probarlo.

# Conectar al servidor
Para conectar al servidor lanzamos:
```
ssh -i ~/.ssh/usuario_servidor_rsa usuario@servidor.es
```
Y únicamente tendremos que introducir la contraseña con la que hemos cifrado la clave privada para conectarnos.

Como último paso, si queremos asociar la clave a toda conexión ssh con ese usuario a ese servidor, podemos establecerlo en nuestro fichero `~/.ssh/config`:
```
Host servidor.es
    User usuario
    IdentityFile ~/.ssh/usuario_servidor_rsa
```

Ahora bastará con que conectemos mediante:
```
ssh servidor.es
```

¡Listo! Espero que os resulte útil.

PD: Si utilizas **Konsole** como [emulador de terminal](https://es.wikipedia.org/wiki/Emulador_de_terminal) y acostumbras a conectarte a diferentes servidores, te puede resultar útil el [plugin SSH Manager](https://invent.kde.org/utilities/konsole/-/merge_requests/360).