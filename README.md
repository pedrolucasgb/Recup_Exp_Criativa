# 🍽️ Sistema de Gerenciamento de Restaurante

Um sistema completo para gerenciamento de comandas, pedidos e pagamentos em restaurantes, desenvolvido em Python com Flask.

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Arquitetura do Sistema](#-arquitetura-do-sistema)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação e Configuração](#-instalação-e-configuração)
- [Banco de Dados](#-banco-de-dados)
- [Modelos de Dados](#-modelos-de-dados)
- [Sistema de Autenticação](#-sistema-de-autenticação)
- [Controle de Permissões](#-controle-de-permissões)
- [Fluxo de Operação](#-fluxo-de-operação)
- [Endpoints da Aplicação](#-endpoints-da-aplicação)
- [Uso do Sistema](#-uso-do-sistema)
- [Troubleshooting](#-troubleshooting)

---

## 🎯 Visão Geral

Este sistema foi projetado para automatizar e gerenciar o fluxo de atendimento em restaurantes, desde o registro de clientes até o fechamento e pagamento de comandas. O sistema implementa diferentes níveis de acesso (Cliente, Atendente e Caixa) com permissões específicas para cada perfil.

### Principais Características

- **Gerenciamento de Usuários**: Sistema multiusuário com 3 tipos de perfil
- **Controle de Comandas**: Abertura, edição e fechamento de comandas por mesa
- **Cardápio Digital**: Cadastro e visualização de itens do cardápio
- **Sistema de Pedidos**: Adição e remoção de itens nas comandas
- **Processamento de Pagamentos**: Múltiplas formas de pagamento
- **Controle de Acesso**: Permissões diferenciadas por tipo de usuário

---

## ✨ Funcionalidades

### Para Clientes 👤
- ✅ Criar conta e fazer login
- ✅ Visualizar cardápio completo
- ✅ Abrir comandas para sua mesa
- ✅ Adicionar itens à sua comanda
- ✅ Visualizar suas comandas ativas

### Para Atendentes 🙋
- ✅ Todas as funcionalidades de cliente
- ✅ Abrir comandas para qualquer cliente
- ✅ Adicionar itens em qualquer comanda aberta
- ✅ Editar quantidade de itens em comandas abertas
- ✅ Remover itens de comandas abertas
- ✅ Fechar comandas (enviar para o caixa)

### Para Caixa 💰
- ✅ Todas as funcionalidades de atendente
- ✅ Gerenciar usuários (criar, editar, ativar/desativar)
- ✅ Editar comandas fechadas (antes do pagamento)
- ✅ Processar pagamentos
- ✅ Visualizar comandas pagas
- ✅ Acesso total ao sistema

---

## 🏗️ Arquitetura do Sistema

O sistema segue o padrão **MVC (Model-View-Controller)** adaptado para Flask:

```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────┐
│     Templates (Views)            │
│  - HTML + Jinja2                 │
│  - CSS (Bootstrap)               │
└──────┬──────────────────────────┘
       │
       ▼
┌─────────────────────────────────┐
│   Controllers (Blueprints)       │
│  - auth_controller.py            │
│  - sensor_controller.py          │
└──────┬──────────────────────────┘
       │
       ▼
┌─────────────────────────────────┐
│     Models (SQLAlchemy)          │
│  - usuarios.py                   │
│  - comanda.py                    │
│  - item_comanda.py               │
│  - itens_cardapio.py             │
│  - pagamento.py                  │
└──────┬──────────────────────────┘
       │
       ▼
┌─────────────────────────────────┐
│   Database (MySQL)               │
└─────────────────────────────────┘
```

---

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.x**: Linguagem principal
- **Flask 3.0.0**: Framework web minimalista
- **Flask-Login 0.6.3**: Gerenciamento de sessões de usuário
- **Flask-SQLAlchemy 3.1.1**: ORM para banco de dados
- **Werkzeug 3.0.1**: Utilitários WSGI e hash de senhas

### Banco de Dados
- **MySQL**: Sistema de gerenciamento de banco de dados
- **PyMySQL 1.1.0**: Conector Python para MySQL
- **SQLAlchemy**: ORM (Object-Relational Mapping)

### Frontend
- **HTML5/CSS3**: Estrutura e estilização
- **Jinja2**: Template engine do Flask
- **Bootstrap**: Framework CSS (via CDN nos templates)

### Segurança
- **Werkzeug Security**: Hash de senhas com PBKDF2
- **Flask Session**: Gerenciamento seguro de sessões
- **cryptography 41.0.7**: Criptografia adicional

---

## 📁 Estrutura do Projeto

```
Recup_Exp_Criativa/
│
├── app/
│   ├── main.py                      # Arquivo principal da aplicação
│   ├── database.sql                 # Script SQL para criação do banco
│   ├── README.md                    # Documentação interna
│   │
│   ├── controllers/                 # Controladores (Blueprints)
│   │   ├── auth_controller.py      # Autenticação e usuários
│   │   └── sensor_controller.py    # Comandas e pedidos
│   │
│   ├── models/                      # Modelos de dados (ORM)
│   │   ├── __init__.py
│   │   ├── db.py                   # Configuração do SQLAlchemy
│   │   ├── usuarios.py             # Modelo de usuários
│   │   ├── comanda.py              # Modelo de comandas
│   │   ├── item_comanda.py         # Itens das comandas
│   │   ├── itens_cardapio.py       # Cardápio
│   │   └── pagamento.py            # Pagamentos
│   │
│   ├── static/                      # Arquivos estáticos
│   │   └── css/
│   │       └── style.css           # Estilos personalizados
│   │
│   └── templates/                   # Templates HTML
│       ├── base.html               # Template base
│       ├── login.html              # Página de login
│       ├── register.html           # Cadastro de clientes
│       ├── dashboard.html          # Painel principal
│       ├── cardapio.html           # Visualização do cardápio
│       ├── manage_users.html       # Gerenciamento de usuários
│       ├── edit_sensor.html        # (Não utilizado)
│       └── register_sensor.html    # (Não utilizado)
│
├── pyproject.toml                   # Configuração do projeto
├── requirements.txt                 # Dependências Python
└── README.md                        # Este arquivo
```

---

## 🚀 Instalação e Configuração

### Pré-requisitos

1. **Python 3.8+** instalado
2. **MySQL Server** instalado e rodando
3. **pip** (gerenciador de pacotes Python)

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/pedrolucasgb/Recup_Exp_Criativa.git
cd Recup_Exp_Criativa
```

### Passo 2: Criar Ambiente Virtual (Recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Configurar Banco de Dados

#### Opção 1: Usar o Script SQL

```bash
# Conectar ao MySQL
mysql -u root -p

# Executar o script
source app/database.sql
```

#### Opção 2: Deixar o Flask criar automaticamente

O arquivo `main.py` possui a função `init_db()` que cria as tabelas automaticamente.

### Passo 5: Configurar Variáveis de Ambiente (Opcional)

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua-chave-secreta-aqui
DB_USER=root
DB_PASSWORD=sua-senha-mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=restaurante
```

### Passo 6: Executar a Aplicação

```bash
cd app
python main.py
```

A aplicação estará disponível em: **http://localhost:5000**

---

## 💾 Banco de Dados

### Schema do Banco

O sistema utiliza 5 tabelas principais:

#### 1. **usuarios**
Armazena informações dos usuários do sistema.

| Campo      | Tipo         | Descrição                          |
|------------|--------------|-------------------------------------|
| id         | INT (PK)     | Identificador único                 |
| nome       | VARCHAR(100) | Nome completo                       |
| email      | VARCHAR(100) | Email (único)                       |
| senha      | VARCHAR(256) | Hash da senha                       |
| tipo       | VARCHAR(20)  | 'cliente', 'atendente' ou 'caixa'  |
| ativo      | BOOLEAN      | Status do usuário                   |
| created_at | TIMESTAMP    | Data de criação                     |

#### 2. **itens_cardapio**
Catálogo de produtos disponíveis.

| Campo       | Tipo         | Descrição                         |
|-------------|--------------|-----------------------------------|
| id          | INT (PK)     | Identificador único               |
| nome        | VARCHAR(100) | Nome do item                      |
| descricao   | VARCHAR(255) | Descrição detalhada               |
| categoria   | VARCHAR(50)  | 'bebida', 'comida' ou 'sobremesa' |
| preco       | FLOAT        | Preço unitário                    |
| disponivel  | BOOLEAN      | Disponibilidade                   |
| created_at  | TIMESTAMP    | Data de criação                   |
| updated_at  | TIMESTAMP    | Última atualização                |

#### 3. **comandas**
Registro de comandas por mesa.

| Campo        | Tipo        | Descrição                        |
|--------------|-------------|----------------------------------|
| id           | INT (PK)    | Identificador único              |
| numero_mesa  | INT         | Número da mesa                   |
| cliente_id   | INT (FK)    | ID do cliente (usuarios)         |
| status       | VARCHAR(20) | 'aberta', 'fechada' ou 'paga'    |
| valor_total  | FLOAT       | Valor total calculado            |
| created_at   | TIMESTAMP   | Data de abertura                 |
| fechada_at   | TIMESTAMP   | Data de fechamento (nullable)    |
| paga_at      | TIMESTAMP   | Data do pagamento (nullable)     |

#### 4. **itens_comanda**
Itens adicionados em cada comanda.

| Campo             | Tipo         | Descrição                    |
|-------------------|--------------|------------------------------|
| id                | INT (PK)     | Identificador único          |
| comanda_id        | INT (FK)     | ID da comanda                |
| item_cardapio_id  | INT (FK)     | ID do item do cardápio       |
| quantidade        | INT          | Quantidade pedida            |
| preco_unitario    | FLOAT        | Preço no momento do pedido   |
| subtotal          | FLOAT        | quantidade × preco_unitario  |
| observacoes       | VARCHAR(255) | Observações do pedido        |
| created_at        | TIMESTAMP    | Data/hora do pedido          |

#### 5. **pagamentos**
Registro de pagamentos das comandas.

| Campo            | Tipo         | Descrição                               |
|------------------|--------------|-----------------------------------------|
| id               | INT (PK)     | Identificador único                     |
| comanda_id       | INT (FK)     | ID da comanda                           |
| valor            | FLOAT        | Valor do pagamento                      |
| forma_pagamento  | VARCHAR(50)  | 'cartao_credito', 'cartao_debito', 'pix'|
| status           | VARCHAR(20)  | 'pendente', 'aprovado'                 |
| processado_por_id| INT (FK)     | ID do usuário que processou             |
| observacoes      | VARCHAR(255) | Observações adicionais                  |
| created_at       | TIMESTAMP    | Data de criação                         |
| processado_at    | TIMESTAMP    | Data de processamento                   |

### Relacionamentos

```
usuarios (1) ──────< (N) comandas
comandas (1) ──────< (N) itens_comanda
itens_cardapio (1) ─< (N) itens_comanda
comandas (1) ──────< (1) pagamentos
usuarios (1) ──────< (N) pagamentos (processado_por)
```

---

## 📊 Modelos de Dados

### 1. Usuario (`models/usuarios.py`)

**Responsabilidades:**
- Autenticação e autorização de usuários
- Hash seguro de senhas
- Controle de tipos de usuário (cliente, atendente, caixa)

**Métodos principais:**

```python
# Criação e gestão
Usuario.save_usuario(nome, email, senha, tipo)
Usuario.atualizar_usuario(usuario_id, nome, email, senha, tipo)
Usuario.desativar_usuario(usuario_id)
Usuario.ativar_usuario(usuario_id)
Usuario.remover_usuario(usuario_id)

# Consultas
Usuario.get(user_id)
Usuario.get_by_email(email)
Usuario.get_by_tipo(tipo)

# Validação
usuario.check_password(senha)

# Verificação de tipo
usuario.is_cliente()
usuario.is_atendente()
usuario.is_caixa()
```

**Segurança:**
- Senhas são hashadas usando `werkzeug.security.generate_password_hash()`
- Usa PBKDF2 com salt aleatório
- Verificação segura com `check_password_hash()`

### 2. ItemCardapio (`models/itens_cardapio.py`)

**Responsabilidades:**
- Gerenciar catálogo de produtos
- Controlar disponibilidade
- Organizar por categorias

**Métodos principais:**

```python
# CRUD
ItemCardapio.save_item(nome, descricao, categoria, preco, disponivel)
ItemCardapio.update_item(item_id, nome, descricao, categoria, preco, disponivel)
ItemCardapio.delete_item(item_id)

# Consultas
ItemCardapio.get_itens()
ItemCardapio.get_itens_disponiveis()
ItemCardapio.get_by_categoria(categoria)
ItemCardapio.get_item(item_id)
```

**Categorias suportadas:**
- `bebida`: Refrigerantes, sucos, cervejas, etc.
- `comida`: Lanches, porções, pratos
- `sobremesa`: Doces e sobremesas

### 3. Comanda (`models/comanda.py`)

**Responsabilidades:**
- Controlar ciclo de vida das comandas
- Calcular valores totais
- Gerenciar status (aberta → fechada → paga)

**Métodos principais:**

```python
# Criação
Comanda.save_comanda(numero_mesa, cliente_id)

# Consultas
Comanda.get_comandas()
Comanda.get_comandas_abertas()
Comanda.get_comandas_fechadas()
Comanda.get_comandas_pagas()
Comanda.get_comandas_by_cliente(cliente_id)
Comanda.get_comanda(comanda_id)

# Operações
comanda.calcular_total()
comanda.fechar_comanda()
comanda.reabrir_comanda()
comanda.marcar_como_paga()
```

**Ciclo de vida:**

```
ABERTA → FECHADA → PAGA
  ↑         ↓
  └─────────┘ (reabrir)
```

- **Aberta**: Aceita novos itens
- **Fechada**: Não aceita novos itens, aguardando pagamento
- **Paga**: Finalizada, não pode ser modificada

### 4. ItemComanda (`models/item_comanda.py`)

**Responsabilidades:**
- Relacionar itens do cardápio com comandas
- Controlar quantidades
- Calcular subtotais

**Métodos principais:**

```python
# Gerenciamento
ItemComanda.add_item_to_comanda(comanda_id, item_cardapio_id, quantidade, preco_unitario)
ItemComanda.update_item_comanda(item_id, quantidade)
ItemComanda.delete_item_comanda(item_id)

# Consultas
ItemComanda.get_itens_by_comanda(comanda_id)
ItemComanda.get_item_comanda(item_id)
```

**Cálculo de Subtotal:**
```python
subtotal = quantidade × preco_unitario
```

O preço é capturado no momento do pedido para manter histórico correto mesmo se o preço do item mudar no cardápio.

### 5. Pagamento (`models/pagamento.py`)

**Responsabilidades:**
- Processar pagamentos de comandas
- Suportar múltiplas formas de pagamento
- Registrar quem processou o pagamento

**Métodos principais:**

```python
# Criação e processamento
Pagamento.create_pagamento(comanda_id, valor, forma_pagamento, observacoes)
Pagamento.processar_pagamento(pagamento_id, usuario_id, aprovar)

# Consultas
Pagamento.get_pagamentos()
Pagamento.get_pagamentos_pendentes()
Pagamento.get_pagamentos_by_comanda(comanda_id)
Pagamento.get_pagamento(pagamento_id)
```

**Formas de pagamento:**
- `cartao_credito`
- `cartao_debito`
- `pix`

**Status de pagamento:**
- `pendente`: Criado mas não processado
- `aprovado`: Pagamento confirmado
- `cancelado`: Pagamento rejeitado

---

## 🔐 Sistema de Autenticação

### Flask-Login Integration

O sistema usa **Flask-Login** para gerenciar sessões de usuário.

**Configuração** (`main.py`):

```python
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.get(int(user_id))
```

### Fluxo de Login

```
1. Usuário acessa /login
2. Insere email e senha
3. Sistema busca usuário por email
4. Verifica senha usando check_password_hash()
5. Se válido: login_user(user)
6. Redireciona para dashboard
```

### Proteção de Rotas

Todas as rotas exceto login e registro são protegidas:

```python
@app.route('/dashboard')
@login_required  # Decorator que exige autenticação
def dashboard():
    # ...
```

### Logout

```python
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
```

---

## 🔒 Controle de Permissões

### Matriz de Permissões

| Ação                          | Cliente | Atendente | Caixa |
|-------------------------------|---------|-----------|-------|
| Ver cardápio                  | ✅      | ✅        | ✅    |
| Abrir própria comanda         | ✅      | ✅        | ✅    |
| Abrir comanda para outro      | ❌      | ✅        | ✅    |
| Adicionar item (comanda aberta)| ✅     | ✅        | ✅    |
| Adicionar item (comanda fechada)| ❌    | ❌        | ✅    |
| Editar item (comanda aberta)  | ❌      | ✅        | ✅    |
| Editar item (comanda fechada) | ❌      | ❌        | ✅    |
| Remover item (comanda aberta) | ❌      | ✅        | ✅    |
| Remover item (comanda fechada)| ❌      | ❌        | ✅    |
| Fechar comanda                | ❌      | ✅        | ✅    |
| Processar pagamento           | ❌      | ❌        | ✅    |
| Gerenciar usuários            | ❌      | ❌        | ✅    |

### Implementação de Verificações

**Exemplo 1: Verificação de tipo de usuário**

```python
@auth_bp.route('/gerenciar-usuarios')
@login_required
def gerenciar_usuarios():
    if not current_user.is_caixa():
        flash('Acesso negado. Apenas caixa pode gerenciar usuários.', 'error')
        return redirect(url_for('auth.dashboard'))
    # ...
```

**Exemplo 2: Validação de propriedade**

```python
# Cliente só pode adicionar em sua própria comanda
if current_user.is_cliente() and comanda.cliente_id != current_user.id:
    flash('Você só pode modificar suas próprias comandas.', 'error')
    return redirect(url_for('auth.dashboard'))
```

**Exemplo 3: Validação de status**

```python
# Atendente só pode editar comandas abertas
if current_user.is_atendente() and comanda.status != 'aberta':
    flash('Atendentes só podem editar itens de comandas abertas.', 'error')
    return redirect(url_for('auth.dashboard'))
```

---

## 🔄 Fluxo de Operação

### 1. Fluxo Completo de uma Comanda

```
┌─────────────────────────────────────────────────────────┐
│                    INÍCIO                                │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ 1. ABERTURA DA COMANDA                                   │
│    - Cliente/Atendente/Caixa abre comanda               │
│    - Informa número da mesa                             │
│    - Status: ABERTA                                     │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ 2. ADIÇÃO DE ITENS                                       │
│    - Clientes veem cardápio                             │
│    - Adicionam itens à comanda                          │
│    - Podem adicionar múltiplos itens                    │
│    - Atendente pode editar/remover                      │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ 3. CÁLCULO DO TOTAL                                      │
│    - Sistema calcula automaticamente                    │
│    - Soma todos os subtotais                            │
│    - Atualiza valor_total da comanda                    │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ 4. FECHAMENTO                                            │
│    - Atendente/Caixa fecha a comanda                    │
│    - Status: FECHADA                                    │
│    - Não aceita mais novos itens                        │
│    - Caixa ainda pode editar se necessário              │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ 5. PAGAMENTO                                             │
│    - Caixa processa pagamento                           │
│    - Escolhe forma de pagamento                         │
│    - Cria registro em 'pagamentos'                      │
│    - Status: APROVADO                                   │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│ 6. FINALIZAÇÃO                                           │
│    - Comanda marcada como PAGA                          │
│    - Não pode mais ser modificada                       │
│    - Registro permanece no histórico                    │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│                      FIM                                 │
└─────────────────────────────────────────────────────────┘
```

### 2. Fluxo de Autenticação

```
Login → Validação → Sessão → Dashboard
  ↓         ↓          ↓         ↓
Email    Password   Cookie   Permissões
```

### 3. Fluxo de Gerenciamento de Usuários (Caixa)

```
Caixa acessa "Gerenciar Usuários"
         ↓
Pode criar novo usuário (Cliente ou Atendente)
         ↓
Pode editar dados de usuários existentes
         ↓
Pode ativar/desativar usuários
         ↓
Pode remover permanentemente
```

---

## 🌐 Endpoints da Aplicação

### Autenticação (`auth_controller.py`)

| Rota                          | Método      | Descrição                          | Permissão    |
|-------------------------------|-------------|------------------------------------|--------------|
| `/`                           | GET         | Redireciona para login             | Pública      |
| `/login`                      | GET, POST   | Página de login                    | Pública      |
| `/register`                   | GET, POST   | Cadastro de novos clientes         | Pública      |
| `/dashboard`                  | GET         | Painel principal                   | Autenticado  |
| `/logout`                     | GET         | Encerrar sessão                    | Autenticado  |
| `/gerenciar-usuarios`         | GET         | Gerenciamento de usuários          | Caixa        |
| `/cadastrar-usuario`          | POST        | Criar novo usuário                 | Caixa        |
| `/editar-usuario`             | POST        | Editar usuário                     | Caixa        |
| `/desativar-usuario/<id>`     | POST        | Desativar usuário                  | Caixa        |
| `/ativar-usuario/<id>`        | POST        | Ativar usuário                     | Caixa        |
| `/remover-usuario/<id>`       | POST        | Remover usuário                    | Caixa        |

### Comandas e Cardápio (`sensor_controller.py`)

| Rota                              | Método | Descrição                      | Permissão          |
|-----------------------------------|--------|--------------------------------|--------------------|
| `/cardapio`                       | GET    | Ver cardápio                   | Autenticado        |
| `/cardapio/abrir_comanda`         | POST   | Abrir nova comanda             | Autenticado        |
| `/cardapio/adicionar_item`        | POST   | Adicionar item à comanda       | Autenticado        |
| `/cardapio/fechar_comanda/<id>`   | POST   | Fechar comanda                 | Atendente/Caixa    |
| `/cardapio/editar_item/<id>`      | POST   | Editar quantidade              | Atendente/Caixa    |
| `/cardapio/remover_item/<id>`     | POST   | Remover item                   | Atendente/Caixa    |
| `/cardapio/processar_pagamento/<id>` | POST | Processar pagamento         | Caixa              |

---

## 💻 Uso do Sistema

### Usuários Padrão

Após inicialização, o sistema cria 3 usuários padrão:

```
┌──────────┬─────────────────────────────┬───────────────┐
│ Tipo     │ Email                       │ Senha         │
├──────────┼─────────────────────────────┼───────────────┤
│ Caixa    │ caixa@restaurante.com       │ caixa123      │
│ Atendente│ atendente@restaurante.com   │ atendente123  │
│ Cliente  │ cliente@email.com           │ cliente123    │
└──────────┴─────────────────────────────┴───────────────┘
```

### Cenário de Uso Típico

#### 1. Cliente chega ao restaurante

```
1. Acessa o sistema pelo navegador
2. Faz login ou cria uma conta
3. Visualiza o cardápio
4. Abre uma comanda para sua mesa
5. Adiciona itens que deseja consumir
```

#### 2. Atendente gerencia pedidos

```
1. Faz login como atendente
2. Abre comandas para clientes
3. Adiciona itens solicitados pelos clientes
4. Edita quantidades se necessário
5. Fecha comandas quando clientes solicitam conta
```

#### 3. Caixa processa pagamentos

```
1. Faz login como caixa
2. Visualiza comandas fechadas
3. Verifica itens e valor total
4. Processa pagamento com forma escolhida
5. Confirma pagamento e finaliza comanda
```

### Exemplo Prático

**Passo a Passo Completo:**

```
1. Login como Atendente
   ↓
2. Cliente pede para abrir comanda na mesa 5
   ↓
3. Atendente seleciona o cliente e mesa 5
   ↓
4. Cliente pede:
   - 2x X-Burger (R$ 25,00 cada)
   - 1x Refrigerante (R$ 5,00)
   - 1x Batata Frita (R$ 18,00)
   ↓
5. Atendente adiciona itens
   Sistema calcula: R$ 73,00
   ↓
6. Cliente pede a conta
   Atendente fecha a comanda
   ↓
7. Caixa recebe notificação de comanda fechada
   ↓
8. Caixa processa pagamento via PIX
   ↓
9. Comanda marcada como PAGA
   Cliente pode sair
```

---

## 🔧 Troubleshooting

### Problemas Comuns

#### 1. Erro de Conexão com Banco de Dados

**Sintoma:**
```
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) 
(2003, "Can't connect to MySQL server")
```

**Solução:**
- Verifique se o MySQL está rodando
- Confirme usuário e senha no `.env` ou `main.py`
- Teste a conexão: `mysql -u root -p`

#### 2. Erro ao Criar Tabelas

**Sintoma:**
```
Table 'restaurante.usuarios' doesn't exist
```

**Solução:**
```bash
# Execute o script SQL manualmente
mysql -u root -p < app/database.sql

# Ou deixe o Flask criar
python main.py  # A função init_db() cria automaticamente
```

#### 3. Senha de Usuário Padrão não Funciona

**Problema:** As senhas padrão no SQL estão com hash incorreto.

**Solução:**
```python
# Delete os usuários do banco
# Rode o app novamente - ele cria usuários com senhas corretas
python main.py
```

#### 4. Erro 404 nas Rotas

**Problema:** Blueprint não registrado corretamente.

**Solução:**
Verifique em `main.py`:
```python
app.register_blueprint(auth_bp)
app.register_blueprint(sensor_bp, url_prefix='/cardapio')
```

#### 5. Session Cookie não Funciona

**Problema:** SECRET_KEY não configurada.

**Solução:**
```python
# Em main.py ou .env
app.config['SECRET_KEY'] = 'sua-chave-secreta-forte-aqui'
```

#### 6. Usuário não Consegue Adicionar Item

**Verificar:**
- Status da comanda (aberta?)
- Permissão do usuário
- Item está disponível no cardápio?
- Comanda pertence ao usuário (se cliente)?

#### 7. Total da Comanda não Atualiza

**Causa:** Função `calcular_total()` não chamada.

**Solução:** É chamada automaticamente em:
- `add_item_to_comanda()`
- `update_item_comanda()`
- `delete_item_comanda()`
- `fechar_comanda()`

Se não atualizar, verifique se há exceções sendo capturadas silenciosamente.

---

## 📝 Notas de Desenvolvimento

### Padrões de Código

1. **Retorno de Métodos de Modelo:**
   ```python
   return (success: bool, result: object|str)
   ```

2. **Flash Messages:**
   - `success`: Operação bem-sucedida
   - `error`: Erro na operação
   - `warning`: Aviso ao usuário

3. **Validações:**
   - Sempre validar permissões
   - Verificar status antes de modificar
   - Confirmar existência de registros relacionados

### Melhorias Futuras

- [ ] Sistema de relatórios e estatísticas
- [ ] Impressão de comandas
- [ ] Suporte a cupom fiscal
- [ ] App mobile para clientes
- [ ] Integração com sistema de estoque
- [ ] Notificações em tempo real (WebSocket)
- [ ] Suporte a gorjetas
- [ ] Divisão de conta entre clientes
- [ ] QR Code para acesso rápido
- [ ] Dashboard com gráficos

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.

---

## 👨‍💻 Autor

**Pedro Lucas**
- GitHub: [@pedrolucasgb](https://github.com/pedrolucasgb)

---

## 🙏 Agradecimentos

Desenvolvido como projeto de recuperação para a disciplina de Experiência Criativa.

---

**Versão:** 1.0.0  
**Última Atualização:** Novembro 2025
