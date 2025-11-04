### 🎬 Flix_API

Este projeto é um estudo comparativo entre duas abordagens para construção de APIs REST com Django:

- **Versão 1.0.0**: CRUD completo utilizando **Django puro**
- **Versão 2.0.0**: Em desenvolvimento — será reimplementado com **Django REST Framework (DRF)**

---

## 📌 Objetivo

Demonstrar como construir uma API RESTful para gerenciamento de filmes, gêneros e outras entidades relacionadas, utilizando Django sem bibliotecas externas. A ideia é comparar posteriormente com uma versão equivalente feita com DRF.

---

## 🚀 Versão 1.0.0 — Django Puro

### Funcionalidades

- CRUD completo para modelos de filmes e gêneros
- URLs organizadas por app
- Views baseadas em funções
- Retorno em JSON manualmente estruturado
- Tratamento de erros com `get_object_or_404`

---

### Estrutura
flix_api/ 
├── app/
│    ├── models.py
│    ├── views.py
│    ├── urls.py
│
├── genres/
│    ├── models.py
│    ├── views.py
│    ├── urls.py
│
├── manage.py
├── db.sqlite3

---

### Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/nicolas-aires-dev/Flix_API.git
   cd Flix_API

2. Instale as dependências:
   ```bash
    python -m venv venv
    source venv/bin/activate  # ou venv\Scripts\activate no Windows
    pip install django

3. Execute as migrações:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   pip install django

4. Inicie o servidor:
    ```bash
    python manage.py runserver
  
5.Teste os endpoints manualmente com ferramentas como Insomnia ou Postman.

---

## 🛠️ Versão 2.0.0 — Django REST Framework (em desenvolvimento)
A próxima versão será construída com DRF para facilitar o desenvolvimento, reaproveitar componentes e melhorar a escalabilidade da API.

---

## 📚 Tecnologias
  - Python 3
  - Django 4+
  - SQLite (default)

---

## 📌 Status
 - ✅ Versão 1.0.0 finalizada
 - 🔄 Versão 2.0.0 em desenvolvimento

---

## Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
