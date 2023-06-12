# Generador de Contraseñas Aleatorias

Este es un programa simple escrito en Python que te permite crear contraseñas aleatorias de un largo determinado. 

## Requisitos

El programa utiliza las siguientes bibliotecas de Python:

- `string`
- `random`

Puedes instalar las bibliotecas necesarias usando el administrador de paquetes de Python pip. Ejecuta el siguiente comando en tu terminal para instalar las bibliotecas:

```
pip install string random
```

## Uso

1. Ejecuta el programa en tu entorno de Python.
2. Se te solicitará ingresar la longitud deseada para la contraseña.
3. El programa generará una contraseña aleatoria utilizando caracteres alfabéticos (mayúsculas y minúsculas), dígitos y caracteres especiales.
4. La contraseña generada se mostrará en la pantalla.

## Cómo funciona

El programa funciona de la siguiente manera:

1. Importa las bibliotecas necesarias: `string` y `random`.
2. Crea una lista de caracteres que se utilizarán para generar la contraseña, incluyendo letras mayúsculas y minúsculas, dígitos y algunos caracteres especiales.
3. Define una función `generate_password` que permite al usuario especificar la longitud deseada de la contraseña.
4. Mezcla aleatoriamente la lista de caracteres.
5. Genera una lista de caracteres aleatorios seleccionados de la lista mezclada, de acuerdo con la longitud especificada.
6. Mezcla nuevamente la lista de caracteres generados aleatoriamente.
7. Convierte la lista de caracteres en una cadena de texto.
8. Muestra la contraseña generada en la pantalla.
9. Proporciona una opción para que el usuario decida si quiere generar otra contraseña o cerrar el programa.

## Contribución

Si deseas contribuir a este proyecto, siéntete libre de abrir un problema o enviar una solicitud de extracción.

Espero que encuentres útil este generador de contraseñas aleatorias. ¡Disfrútalo!
