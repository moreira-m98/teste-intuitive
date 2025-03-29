# Teste Intuitive

Este repositório contém as soluções desenvolvidas para os testes técnicos do processo seletivo da Intuitive Care.

## Estrutura do Repositório

- `teste_1_e_2/`: Contém as soluções para os Testes 1 e 2.
- `teste_3/`: Contém a solução para o Teste 3.
- `teste_4/`: Contém a solução para o Teste 4.
- `requirements.txt`: Lista de dependências necessárias para executar os testes.

## Teste 1 e 2: Web Scraping e Processamento de Dados

### Descrição

O objetivo dos Testes 1 e 2 foi realizar web scraping para obter um arquivo PDF do site da ANS (Agência Nacional de Saúde Suplementar) e, em seguida, extrair e processar dados específicos desse arquivo.


### Como Executar

1. Navegue até o diretório `teste_1_e_2`:
   ```bash
   cd teste_1_e_2
   ```
2. Execute o script de scraping:
   ```bash
   python scraper.py
   ```
3. Execute o script data:
    ```bash
   python data.py
   ```

## Teste 3: API RESTful com FastAPI

### Descrição

O Teste 3 consistiu em desenvolver uma API RESTful utilizando FastAPI para disponibilizar os dados processados no Teste 2.

### Estrutura

- `server.py`: Script principal que inicializa a API e define os endpoints.
- `data/Relatorio_cadop.csv`: Arquivo CSV contendo os dados a serem servidos pela API.

### Como Executar

1. Navegue até o diretório `teste_3`:
   ```bash
   cd teste_3
   ```
2. Inicie o servidor FastAPI:
   ```bash
   python server.py
   ```
3. Acesse a documentação interativa da API em `http://localhost:8000/docs`.

## Teste 4: Integração Frontend com Vue.js

### Descrição

No Teste 4, foi desenvolvida uma interface frontend utilizando Vue.js para interagir com a API criada no Teste 3.

### Estrutura

- `App.vue`: Componente principal que contém a interface de busca e exibição dos dados.
- `main.js`: Script que inicializa a aplicação Vue.js.

### Como Executar

1. Navegue até o diretório `teste_4`:
   ```bash
   cd teste_4
   ```
2. Instale as dependências do projeto:
   ```bash
   npm install
   ```
3. Inicie o servidor de desenvolvimento:
   ```bash
   npm run dev
   ```
4. Acesse a aplicação em `http://localhost:5173`.

## Dependências

As dependências necessárias para executar os testes estão listadas no arquivo `requirements.txt`. Para instalá-las, execute:

```bash
pip install -r requirements.txt
```

## Coleção do Postman

Para facilitar os testes dos endpoints da API, uma coleção do Postman foi disponibilizada. Você pode acessá-la através do seguinte link:

[https://matheusmoreira-1197676.postman.co/workspace/Matheus-Moreira's-Workspace~e445ba35-cf5a-48bc-88bd-0d33d9deae1d/request/43576099-310155db-2f5e-4511-b858-d9f2b3b3fc24?action=share&source=copy-link&creator=43576099](https://matheusmoreira-1197676.postman.co/workspace/Matheus-Moreira's-Workspace~e445ba35-cf5a-48bc-88bd-0d33d9deae1d/request/43576099-310155db-2f5e-4511-b858-d9f2b3b3fc24?action=share&source=copy-link&creator=43576099)
