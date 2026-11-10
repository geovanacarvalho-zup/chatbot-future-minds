import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("STACKSPOT_CLIENT_ID")
CLIENT_KEY = os.getenv("STACKSPOT_CLIENT_KEY")
REALM = os.getenv("STACKSPOT_REALM", "zup")
AGENT_SLUG = os.getenv("STACKSPOT_AGENT_SLUG", "01M72MJJHR201Q51FK9PHBHZYF")

AUTH_URL = f"https://idm.stackspot.com/{REALM}/oidc/oauth/token"
API_URL = f"https://genai-inference-app.stackspot.com/v1/agent/{AGENT_SLUG}/chat"


def obter_token_acesso() -> str:
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_KEY,
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "ProjetoFutureMinds/1.0",
    }
    resposta = requests.post(AUTH_URL, data=payload, headers=headers, timeout=15)
    if not resposta.ok:
        raise Exception(
            f"Falha na autenticação: {resposta.status_code} - {resposta.text}"
        )
    return resposta.json()["access_token"]


def enviar_mensagem_stackspot(mensagem_usuario: str) -> str:
    token = obter_token_acesso()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "ProjetoFutureMinds/1.0",
    }
    payload = {
        "streaming": False,
        "user_prompt": mensagem_usuario,
        "stackspot_knowledge": False,
        "return_ks_in_response": True,
        "deep_search_ks": False,
    }

    resposta = requests.post(API_URL, json=payload, headers=headers, timeout=30)
    if not resposta.ok:
        raise Exception(
            f"Erro {resposta.status_code} ({resposta.reason}) na URL {API_URL}:\n{resposta.text}"
        )

    dados = resposta.json()
    if isinstance(dados, dict):
        # Extrai exclusivamente o texto da mensagem limpa devolvida pela StackSpot
        if "message" in dados:
            return dados["message"]
        return dados.get(
            "result", dados.get("answer", dados.get("content", str(dados)))
        )
    return str(dados)