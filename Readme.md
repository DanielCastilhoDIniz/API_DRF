SEU CÓDIGO DJANGO                     BANCO DE DADOS
      |                                      |
      v                                      v
┌─────────────────┐                ┌─────────────────┐
│   models.py     │                │     TABELAS     │
│  (Definição)    │◄──migrate───── │    (SQLite/     │
└────────┬────────┘                │   PostgreSQL)   │
         │                         └─────────────────┘
         │ makemigrations
         v
┌─────────────────┐                ┌─────────────────┐
│   Migrações     │                │  Serializers    │
│   (0001.py)     │                │ (Validação &    │
└─────────────────┘                │  Transformação) │
                                   └────────┬────────┘
                                            │
                                            v
                                   ┌─────────────────┐
          Cliente ◄─────────────── │     Views       │
          (Frontend)  JSON Response│  (Lógica API)   │
                                   └────────┬────────┘
                                            │
                                            v
                                   ┌─────────────────┐
                                   │      URLs       │
                                   │   (Rotas API)   │
                                   └─────────────────┘