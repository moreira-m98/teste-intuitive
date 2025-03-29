import requests
import zipfile

def baixar_pdf(url, nome_arquivo):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        with open(nome_arquivo, 'wb') as arquivo:
            arquivo.write(resposta.content)
        print(f'Download concluído: {nome_arquivo}')
    else:
        print(f'Falha no download. Código de status: {resposta.status_code}')

arquivos = {
    'Anexo_I.pdf': 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN606_RN607.pdf',
    'Anexo_II.pdf': 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN596.pdf'
}

for nome, url in arquivos.items():
    baixar_pdf(url, nome)

zip_filename = "../anexos.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    print(arquivos.keys())
    for nome in arquivos.keys():
        zipf.write(nome)
    print(f'Arquivo ZIP criado: {zip_filename}')
