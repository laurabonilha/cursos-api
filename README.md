# 🚀 API de Cursos - FastAPI

Esta API foi desenvolvida utilizando **FastAPI** e **SQLAlchemy** para gerenciar um CRUD de cursos, armazenando os dados em um banco **PostgreSQL**. A estrutura do projeto segue uma organização modular, garantindo manutenção e escalabilidade

---

## 🌟 Tecnologias Utilizadas
- 🔹 **Linguagem:** Python
- ⚡ **Framework:** FastAPI
- 🏗 **ORM:** SQLAlchemy (com AsyncSession)
- 🗄 **Banco de Dados:** PostgreSQL
- 💻 **IDE:** VSCode
- 🔑 **Testes de API:** Postman

Desenvolvida com **arquitetura modular**, a API garante eficiência e manutenibilidade, facilitando futuras expansões e integrações!

---

## 📂 Estrutura do Projeto

```
📦 projeto
├── 📂 api
│   ├── 📂 v1
│   │   ├── 📂 endpoints
├── 📂 core  # Configuração do banco e dependências
├── 📂 models # Modelos do banco de dados
├── 📂 schemas # Esquemas de validação
├── 📜 README.md # Documentação do projeto
├── 📜 criar_tabelas.py # Script para criação do banco
├── 📜 main.py # Arquivo principal para rodar a API
├── 📜 requirements.txt # Dependências do projeto
```

Com essa organização clara, o projeto facilita o desenvolvimento colaborativo e permite uma escalabilidade eficiente.

---

## ⚡ Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/laurabonilha/cursos-api.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd cursos-api
   ```
3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\\Scripts\\activate  # Windows
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute a API:
   ```bash
   python main.py
   ```

Pronto! A API estará rodando e pronta para ser testada. 🚀

---

## 🔥 Endpoints

Esta API fornece uma experiência completa para manipulação de cursos, desde a criação até a exclusão, com respostas rápidas e seguras!

Base URL
A URL base para acessar os endpoints da API é: **http://localhost:8000/api/v1/cursos**

### 📌 Criar um Curso
- **Método:** `POST`
- **URL:** `/`
- **Status:** `201 CREATED`
- **Corpo da Requisição:**
  ```json
  {
    "titulo": "Curso de Python",
    "aulas": 30,
    "horas": 60
  }
  ```
- **Resposta:**
  ```json
  {
    "id": 1,
    "titulo": "Curso de Python",
    "aulas": 30,
    "horas": 60
  }
  ```

---

### 📌 Obter Todos os Cursos
- **Método:** `GET`
- **URL:** `/`
- **Status:** `200 OK`
- **Resposta:**
  ```json
  [
    {
      "id": 1,
      "titulo": "Curso de Python",
      "aulas": 30,
      "horas": 60
    }
  ]
  ```

---

### 📌 Obter um Curso por ID
- **Método:** `GET`
- **URL:** `/{curso_id}`
- **Status:** `200 OK` ou `404 NOT FOUND`
- **Resposta:**
  ```json
  {
    "id": 1,
    "titulo": "Curso de Python",
    "aulas": 30,
    "horas": 60
  }
  ```

---

### 📌 Atualizar um Curso
- **Método:** `PUT`
- **URL:** `/{curso_id}`
- **Status:** `202 ACCEPTED`
- **Corpo da Requisição:**
  ```json
  {
    "titulo": "Curso de Python Avançado",
    "aulas": 40,
    "horas": 80
  }
  ```
- **Resposta:**
  ```json
  {
    "id": 1,
    "titulo": "Curso de Python Avançado",
    "aulas": 40,
    "horas": 80
  }
  ```

---

### 📌 Deletar um Curso
- **Método:** `DELETE`
- **URL:** `/{curso_id}`
- **Status:** `204 NO CONTENT`

---

## 🔗 Testando com Swagger

Após rodar a API, você pode explorá-la de maneira interativa com a interface do **Swagger** em:
- 📌 `http://127.0.0.1:8000/docs`
- 📌 `http://127.0.0.1:8000/redoc`

Com essa interface, você pode testar requisições de maneira intuitiva e visualizar os modelos de resposta em tempo real.

---

## 🚧 Melhorias em Progresso

Estou constantemente aprimorando a API para torná-la mais robusta e fácil de usar. Atualmente, estou trabalhando nas seguintes melhorias:

🎨 **Interface Gráfica:** Em andamento a criação de uma interface gráfica simples para facilitar a visualização dos cursos cadastrados e permitir a inserção de novos dados diretamente pela interface.

⚙️ **Novos Endpoints:** Planejamento para adicionar novos endpoints para recursos como filtragem avançada e busca de cursos específicos.

🛠 **Otimizações de Performance:** Foco em melhorias para garantir que a API seja mais eficiente e escalável conforme o número de requisições aumente.

🔐 **Autenticação e Segurança:** Implementação de mecanismos de autenticação para garantir maior segurança nas interações com a API.

Fique à vontade para contribuir e sugerir outras melhorias!

---

## 👨‍💻 Autor
Desenvolvido com 💙 por **[Laura Bonilha](https://github.com/laurabonilha)** 🚀

