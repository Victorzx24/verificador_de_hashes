import subprocess

nome_arquivo = input('Digite o caminho do arquivo: ')

certutil_arquivo = f'certutil -hashfile {nome_arquivo} SHA256'

processo = subprocess.run(certutil_arquivo, shell=True, capture_output=True, text=True)
print(processo.stdout)