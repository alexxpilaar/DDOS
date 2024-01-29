import subprocess

def run():
    # Aquí puedes cambiar el comando que deseas ejecutar en el cmd
    comando = "whoami"
    
    # Ejecutar el comando en el cmd
    resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Imprimir la salida estándar y el error estándar del comando
    print("Salida estándar:", resultado.stdout)
    print("Error estándar:", resultado.stderr)

# Llamamos a la función run()
run()
