# API REST – Cursos e Avaliações (Projeto de Estudo)

Este projeto tem como objetivo **estudar e consolidar boas práticas na elaboração de APIs REST com Django e Django REST Framework (DRF)**. Ele foi desenvolvido com foco **educacional**, priorizando clareza arquitetural, organização do código, padrões REST e preocupações reais de backend, como validações, performance e escalabilidade.

---

## 🎯 Objetivos do Projeto

* Aplicar conceitos fundamentais de **API RESTful**
* Trabalhar com **ViewSets, Serializers e Actions customizadas**
* Implementar **relacionamentos entre recursos** (Cursos ↔ Avaliações)
* Explorar **validações no serializer**
* Discutir **boas práticas de performance** (aggregate, annotate, N+1 queries)
* Testar endpoints com **Postman e autenticação via token**

> ⚠️ Este não é um projeto de produção, mas sim um **laboratório de aprendizado backend**.

---

## 🏗️ Estrutura do Projeto

```text
.
├── cursos/                 # App principal da API
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py           # Models Curso e Avaliacao
│   ├── serializers.py      # Serializers e validações
│   ├── views.py            # ViewSets e actions customizadas
│   ├── urls.py
│   └── tests.py
│
├── escolas/                # Configuração do projeto Django
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── venv/                   # Ambiente virtual
├── db.sqlite3              # Banco de dados (desenvolvimento)
├── manage.py
├── requirements.txt
├── testes_requests.py      # Testes simples via requests
└── README.md
```

---

## 🧩 Modelagem de Domínio (Visão Geral)

### Curso

* Representa um curso disponível na plataforma
* Pode possuir **múltiplas avaliações**
* Possui status ativo/inativo

### Avaliação

* Pertence a um único curso
* Possui nota inteira de 1 a 5
* Inclui nome, e-mail (write-only) e comentário
* Valida se o curso está ativo antes de aceitar avaliação

---

## 🔗 Principais Endpoints

### Cursos

| Método | Endpoint                                  | Descrição                        |
| ------ | ----------------------------------------- | -------------------------------- |
| GET    | `/cursos/`                                | Lista todos os cursos            |
| GET    | `/cursos/{id}/`                           | Detalhe de um curso              |
| GET    | `/cursos/{id}/avaliacoes/`                | Lista avaliações de um curso     |
| GET    | `/cursos/{id}/avaliacoes/{avaliacao_id}/` | Retorna uma avaliação específica |

### Avaliações

| Método | Endpoint       | Descrição                 |
| ------ | -------------- | ------------------------- |
| GET    | `/avaliacoes/` | Lista todas as avaliações |
| POST   | `/avaliacoes/` | Cria uma nova avaliação   |

---

## 🧠 Decisões Arquiteturais Importantes

### Actions customizadas no ViewSet

O projeto utiliza `@action(detail=True)` para representar **sub-recursos REST**, como:

```
/cursos/{curso_id}/avaliacoes/
/cursos/{curso_id}/avaliacoes/{avaliacao_id}/
```

Essa abordagem mantém:

* Coesão semântica
* URLs claras
* Alinhamento com REST

---

### Validações no Serializer

As validações são feitas no nível do serializer, seguindo boas práticas do DRF:

* `validate_avaliacao`: garante nota entre 1 e 5
* `validate_curso`: impede avaliações em cursos inativos
* `email`: definido como `write_only`

Isso evita lógica espalhada na view e centraliza regras de negócio.

---

### Performance e Escalabilidade

Inicialmente, a média das avaliações foi calculada via `SerializerMethodField`, mas o projeto evolui para a abordagem correta:

* Uso de `annotate(Avg())` no queryset
* Eliminação do problema de **N+1 queries**
* Cálculo feito diretamente no banco de dados

Essa evolução faz parte do **aprendizado intencional do projeto**.

---

## 🔐 Autenticação

O projeto está preparado para uso de **Token Authentication** do DRF, testado via Postman.

Exemplo de header:

```
Authorization: Token <seu_token_aqui>
```

---

## 🧪 Testes

* Testes manuais com Postman
* Script simples com `requests` (`testes_requests.py`)
* Estrutura pronta para evolução com `pytest`

---

## 📦 Dependências Principais

* Python 3.11+
* Django 5.2
* Django REST Framework 3.16
* django-filter
* pytest
* requests

Arquivo completo: `requirements.txt`

---

## 🚀 Como Executar o Projeto

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Rodar servidor
python manage.py runserver
```

---

## 📚 Aprendizados Consolidado neste Projeto

* DRF ViewSets e Routers
* Serializers e validações avançadas
* Sub-recursos REST
* Boas práticas de performance
* Organização de API profissional

---

## 📌 Observação Final

Este projeto foi desenvolvido com foco **didático e técnico**, priorizando entendimento profundo das decisões de backend e não apenas funcionamento superficial.

Sugestões, refatorações e extensões são bem-vindas como parte do processo de aprendizado.
