import requests
from bs4 import BeautifulSoup

# URL do site que você deseja extrair dados
url = 'http://table.loc/'  # Substitua com o URL do site real

# Fazer a requisição para o site
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Obter o conteúdo da página
    page_content = response.text
    
    # Analisar o conteúdo HTML
    soup = BeautifulSoup(page_content, 'html.parser')
    
    # Encontrar todos os campos com a classe 'field-get_info_principal'
    info_fields = soup.find_all('td', class_='field-get_info_principal')
    
    # Abrir um arquivo de texto para salvar os nomes e e-mails
    with open('dados.txt', 'w') as file:
        file.write('nome,matricula,email\n')
        for field in info_fields:
            # Extrair o nome
            full_text = field.find('dd', class_='negrito').get_text(strip=True)
            name, id = full_text.rsplit(' ', 1)
            id = id.replace('(', '').replace(')', '')
            
            # Extrair o e-mail
            email_tag = field.find('a', href=True)
            email = email_tag.get_text(strip=True) if email_tag else "E-mail não encontrado"
            
            # Escrever no arquivo
            file.write(f'{name},{id},{email}\n')
    
    print("Dados extraídos com sucesso. (dados.txt)")
else:
    print("Página não encontrada...")
