# 🚀 Focus Performance API

API desenvolvida para registrar sessões de foco e gerar diagnósticos inteligentes de produtividade com base nos dados registrados.

## 📌 Objetivo

O projeto tem como objetivo ajudar desenvolvedores e estudantes a monitorarem seu nível de foco durante sessões de trabalho ou estudo, permitindo análises de produtividade ao longo do tempo.

---

# 🛠 Tecnologias Utilizadas

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

# 📂 Estrutura do Projeto

```bash
app/
├── models/
├── routes/
├── schemas/
├── services/
├── utils/
├── database.py
└── main.py
```

---

# ⚙️ Como Executar o Projeto

## 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

---

## 2. Acesse a pasta do projeto

```bash
cd teste-tecnico-python-backend
```

---

## 3. Crie o ambiente virtual

```bash
python -m venv venv
```

---

## 4. Ative o ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 6. Execute o projeto

```bash
uvicorn app.main:app --reload
```

---

# 📘 Documentação Swagger

Após iniciar a aplicação:

```bash
http://127.0.0.1:8000/docs
```

---

# 📌 Endpoints

## ✅ POST /focus-sessions

Cria uma nova sessão de foco.

### Exemplo Request

```json
{
  "focus_level": 5,
  "duration_minutes": 120,
  "comment": "Implemented JWT authentication",
  "category": "backend"
}
```

---

## ✅ GET /productivity-diagnosis

Gera um diagnóstico inteligente baseado nas sessões registradas.

### Exemplo Response

```json
{
  "average_focus_level": 4.67,
  "total_focus_time": 360,
  "total_sessions": 3,
  "most_productive_category": "backend",
  "feedback": "Você está em um fluxo de alta produtividade!"
}
```

---

# 🧠 Regras de Negócio

A API realiza:

- cálculo da média de foco
- soma do tempo total produtivo
- identificação da categoria mais produtiva
- geração automática de feedback inteligente

---

# ✅ Validações Implementadas

- nível de foco entre 1 e 5
- duração maior que zero
- comentário obrigatório
- tipagem forte com Pydantic

---

# 🤖 Uso de Inteligência Artificial

Foram utilizadas ferramentas de IA como ChatGPT para:

- apoio na arquitetura da aplicação
- refinamento de regras de negócio
- revisão de boas práticas
- suporte educacional durante o desenvolvimento

Toda implementação foi revisada, adaptada e validada manualmente.

---

# 👨‍💻 Autor

Fernando Tenório