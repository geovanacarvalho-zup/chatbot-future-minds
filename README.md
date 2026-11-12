# 🤖 Chatbot com StackSpot AI e SQLite

Assistente virtual integrado com a API da StackSpot AI para tirar dúvidas sobre o Future Minds, gravando o histórico de conversas em um banco de dados local SQLite.

---

## 🛠️ 1. Dependências Necessárias

Para rodar este projeto, é necessário ter o **Python 3.10+** instalado.

No terminal, instale as bibliotecas necessárias com o comando:

```bash
pip install requests python-dotenv


⚙️ 2.COMO CONFIGURAR E EXECUTAR

Passo 1: Criar o arquivo .env
Por questões de segurança, as credenciais não são enviadas ao repositório.
Crie um arquivo chamado .env na raiz do projeto e preencha com as suas credenciais da StackSpot:

Snippet de código
STACKSPOT_REALM=zup
STACKSPOT_CLIENT_ID=<SEU_CLIENT_ID_AQUI>
STACKSPOT_CLIENT_KEY=<SEU_CLIENT_KEY_AQUI>
STACKSPOT_AGENT_SLUG=01M72MJJHR201Q51FK9PHBHZYF

ATENÇÃO: A aplicação gerencia a renovação de tokens automaticamente via OAuth2 a cada execução.

Passo 2: Iniciar a aplicação
Com o arquivo .env configurado, execute:

Bash
python main.py


O banco local historico_chat.db será criado automaticamente na primeira execução

