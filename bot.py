
import subprocess

def run():
    
    comando = "whoami"
    
    
    resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    
    print("Salida estándar:", resultado.stdout)
    print("Error estándar:", resultado.stderr)

run()
