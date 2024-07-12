# SWApi Favoritos

## Nome
SWApi Favoritos

## Descrição
A SWApi Favoritos é um serviço de gerenciamento de favoritos que permite que os usuários salvem, atualizem, leiam e removam seus itens favoritos do universo de Star Wars. Cada favorito é associado a um usuário e inclui detalhes como descrição, ID do item na SWAPI (Star Wars API) e tipo do item (filme, personagem, etc.).

## Para que serve
Este projeto serve para armazenar e gerenciar os favoritos de usuários, fazendo verificações com a SWAPI para garantir que os IDs fornecidos existem. É útil para aplicações que desejam oferecer funcionalidades de favoritos ou listas de desejos relacionados ao universo de Star Wars.

## O que foi usado
- **Linguagem de Programação**: Python
- **Framework Web**: Flask
- **Banco de Dados**: SQLite
- **ORM**: SQLAlchemy
- **Validação de Dados**: Marshmallow
- **API Documentation**: Flask-RESTX
- **Timezone**: Pytz
- **SWAPI**: Star Wars API para verificar a existência de IDs

## Requisitos
- Porta 5000 disponível
- Docker (se for usar via container)
- Python 3.12+ (se for usar localmente)
- Acesso à internet para verificar IDs na SWAPI

## Como usar no Docker

1. **Construir a imagem Docker**:

   ```bash
   docker build -t swapi_favoritos-api .
   ```

2. **Rodar o container**:

   ```bash
   docker run -d -p 5000:5000 --name swapi_favoritos-api swapi_favoritos-api
   ```

3. **Acessar a API**:

   A API estará disponível em [http://localhost:5000](http://localhost:5000).

## Como usar Localmente

1. **Clonar o repositório**:

   ```bash
   git clone https://github.com/ViniciusCTeixeira/PUC_MVP_SWApi_Favoritos_Api.git
   cd PUC_MVP_SWApi_Favoritos_Api
   ```

2. **Criar e ativar um ambiente virtual**:

   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate # Windows
   ```

3. **Instalar as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Rodar a aplicação**:

   ```bash
   flask run
   ```

5. **Acessar a API**:

   A API estará disponível em [http://localhost:5000](http://localhost:5000).

---

Com essas informações, você pode configurar e rodar a SWApi Favoritos tanto em um ambiente Docker quanto localmente, proporcionando uma forma simples e eficiente de gerenciar os favoritos dos usuários.