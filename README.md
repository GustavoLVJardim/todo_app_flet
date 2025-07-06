# ✅ Todo App com Flet + Firebase

Aplicativo de Lista de Tarefas desenvolvido com [Flet](https://flet.dev/) e Python. Ele permite adicionar, excluir, completar tarefas, além de manter um histórico. Os dados são persistidos localmente em `.json` e remotamente no **Firebase Firestore**.

🚀 Compatível com execução **desktop**, **web** e **build para Android/iOS**.

---

## 🧠 Visão Geral

Este projeto foi desenvolvido para explorar:

- Interface gráfica com Flet (modo desktop e web)
- Persistência local com `.json`
- Integração com Firebase Firestore
- Organização em camadas (MVC simplificado)
- Navegação entre páginas (tarefas e histórico)

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12
- [Flet](https://flet.dev/) — UI multiplataforma com Python
- Firebase Firestore — Banco NoSQL na nuvem
- uv ou Poetry — Gerenciadores de dependências

---

## 📦 Instalação e Execução

### Usando **uv**

```bash
uv run flet               # Executa em modo desktop
uv run flet run --web     # Executa em modo web


Usando Poetry

poetry install            # Instala dependências
poetry run flet           # Executa em modo desktop
poetry run flet --web     # Executa em modo web


📦 raiz
├── main.py                      # Script de teste inicial
├── pyproject.toml              # Dependências e config do projeto
├── .python-version             # Versão do Python usada
├── .gitignore                  # Arquivos a ignorar no Git
└── fonte/
    ├── tarefas.json            # Armazenamento local das tarefas
    ├── test_firestore.py       # Teste rápido de conexão Firebase
    └── todo_app/
        ├── main.py             # Ponto de entrada da aplicação
        ├── rotas.py            # Gerenciador de navegação entre páginas
        ├── modelos/
        │   └── modelos.py      # Classe Tarefa e modelos de dados
        ├── controladores/
        │   ├── armazenamento.py        # Persistência local (.json)
        │   ├── firebase_controller.py  # Integração com Firebase
        │   └── task_controllers.py     # Lógica de manipulação das tarefas
        ├── visualizações/
        │   ├── visualizações.py           # Interface principal
        │   ├── views_config.py            # Layout e configurações
        │   └── visualizações_história.py  # Tela de histórico com filtros
        └── firebase/
            └── config.py       # Configurações do Firebase (vazio ou WIP)


🧩 Descrição dos Arquivos
main.py (raiz)
Script simples de teste ou fallback. Pode ser ignorado.

pyproject.toml
Arquivo central do projeto com dependências e configuração do Flet.

tarefas.json
Base de dados local onde as tarefas são salvas offline.

📁 todo_app/
main.py
Inicializa o app Flet, define a rota inicial e inicia a UI.

rotas.py
Define as rotas (/, /historico, etc.) e navegação entre views.

modelos/modelos.py
Contém a classe Tarefa, com métodos auxiliares como to_dict() e from_dict().

controladores/armazenamento.py
Responsável por salvar e carregar tarefas do arquivo tarefas.json.

controladores/firebase_controller.py
Gerencia conexão e sincronização de tarefas com o Firebase Firestore.

controladores/task_controllers.py
Funções para adicionar, remover, alternar status das tarefas e atualizar a lista.

visualizações/visualizações.py
Componente visual da lista de tarefas: campo de entrada, botões e listagem.

visualizações/views_config.py
Configurações de layout e definição visual da estrutura da aplicação.

visualizações/visualizações_história.py
Tela de histórico de tarefas concluídas, com filtros dinâmicos por data/rota.

firebase/config.py
Configurações do Firebase (atualmente vazio ou para uso futuro).

🧪 test_firestore.py
Script de teste simples para validar a conexão com o Firebase.

📲 Build Multiplataforma
Você pode empacotar o app para Android, iOS ou desktop:

Android
bash
Copiar
Editar
flet build apk -v
iOS
bash
Copiar
Editar
flet build ipa -v
Windows, Linux e macOS
bash
Copiar
Editar
flet build windows -v
flet build linux -v
flet build macos -v
Documentação completa em: flet.dev/docs/publish

✨ Funcionalidades Futuras (ideias)
Autenticação com Firebase Auth

Modo offline com sincronização posterior

Suporte a múltiplos usuários

Notificações por push

Tema escuro/claro

Compartilhamento de tarefas

🧑‍💻 Autor
Desenvolvido por Gustavo Jardim