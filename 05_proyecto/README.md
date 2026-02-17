Proyecto cliente-servidor sencillo (KV store)

Descripción
- Este proyecto implementa un servidor TCP simple que actúa como un almacén de pares clave-valor (KV).
- El cliente es una interfaz CLI mínima que envía comandos al servidor y muestra las respuestas.

Comandos soportados (desde el cliente)
- SET key value   → almacena el valor para la clave
- GET key         → obtiene el valor (o NOT_FOUND)
- DEL key         → elimina la clave (o NOT_FOUND)
- KEYS            → lista las claves separadas por espacios
- QUIT            → cierra la conexión

Archivos
- cliente.py: cliente CLI para interactuar con el servidor.
- servidor.py: servidor TCP multi-hilo que mantiene el almacén en memoria.

Uso rápido
1) Desde una terminal, iniciar el servidor:

```bash
python3 05_proyecto/servidor.py
```

2) En otra terminal, iniciar el cliente (por defecto conecta a 127.0.0.1:5000):

```bash
python3 05_proyecto/cliente.py
```

También puedes pasar host y puerto al cliente:

```bash
python3 05_proyecto/cliente.py 192.168.1.10 5000
```

Ejemplo de sesión
> SET nombre Alice
OK
> GET nombre
Alice
> KEYS
nombre
> DEL nombre
DELETED
> GET nombre
NOT_FOUND

Notas
- El servidor mantiene los datos en memoria; al reiniciarlo se pierden.
- Está pensado como proyecto didáctico para aprender arquitectura cliente-servidor.
