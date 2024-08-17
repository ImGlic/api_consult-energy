
# API de Consulta de Fornecedores de Energia

Esta API permite que os usuários consultem fornecedores de energia elétrica com base em seu consumo mensal. A API foi desenvolvida utilizando FastAPI e pode ser executada localmente.

## Funcionalidades

### 1. Listar Fornecedores

**Endpoint:** `/fornecedores`

**Método:** `GET`

**Descrição:** Retorna uma lista de todos os fornecedores disponíveis. Cada fornecedor possui as seguintes informações:
- Nome
- Logo
- Estado de origem
- Custo por kWh
- Limite mínimo de kWh
- Número total de clientes
- Avaliação média dos clientes

**Exemplo de Resposta:**

```json
[
    {
        "nome": "Fornecedor A",
        "logo": "logo_a.png",
        "estado": "SP",
        "custo_por_kwh": 0.45,
        "limite_minimo_kwh": 10000.0,
        "numero_total_clientes": 1500,
        "avaliacao_media": 4.5
    },
    {
        "nome": "Fornecedor B",
        "logo": "logo_b.png",
        "estado": "RJ",
        "custo_por_kwh": 0.50,
        "limite_minimo_kwh": 12000.0,
        "numero_total_clientes": 2000,
        "avaliacao_media": 4.7
    }
]
```

### 2. Escolher Fornecedores com Base no Consumo

**Endpoint:** `/escolha`

**Método:** `POST`

**Descrição:** Retorna uma lista de fornecedores que podem atender o consumo mensal de energia informado pelo usuário.

**Parâmetro de Entrada:**
- `consumo`: (float) Consumo mensal de energia em kWh.

**Exemplo de Requisição:**

```json
{
    "consumo": 15000.0
}
```

**Exemplo de Resposta:**

```json
[
    {
        "nome": "Fornecedor B",
        "logo": "logo_b.png",
        "estado": "RJ",
        "custo_por_kwh": 0.50,
        "limite_minimo_kwh": 12000.0,
        "numero_total_clientes": 2000,
        "avaliacao_media": 4.7
    },
    {
        "nome": "Fornecedor D",
        "logo": "logo_d.png",
        "estado": "RS",
        "custo_por_kwh": 0.48,
        "limite_minimo_kwh": 15000.0,
        "numero_total_clientes": 1600,
        "avaliacao_media": 4.6
    }
]
```

## Como Executar Localmente

### Pré-requisitos

- Python 3.7+
- `pip` instalado

### Passos para Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/ImGlic/api_consult-energy.git
   cd api_consult-energy
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o servidor:

   ```bash
   uvicorn main:app --reload
   ```

   Aqui, `main` é o nome do arquivo onde a API está definida e `app` é a instância da aplicação FastAPI.

4. Acesse a API em:

   ```
   http://127.0.0.1:8000
   ```

### Documentação da API

A documentação interativa da API pode ser acessada em:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

## Licença

Este projeto está licenciado sob os termos da licença MIT.
