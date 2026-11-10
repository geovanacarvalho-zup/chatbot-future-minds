import sys
from database import inicializar_banco, salvar_mensagem, listar_historico, limpar_historico
from client import enviar_mensagem_stackspot


def main():
    inicializar_banco()

    print("=" * 55)
    print("🤖 Chatbot Future Minds - Conectado à StackSpot AI")
    print("Comandos disponíveis:")
    print(" - Digite 'sair' para encerrar")
    print(" - Digite 'historico' para ver conversas anteriores")
    print(" - Digite 'limpar' para iniciar uma conversa do zero")
    print("=" * 55)

    while True:
        try:
            mensagem = input("\nVocê: ").strip()

            if not mensagem:
                continue

            if mensagem.lower() == "sair":
                print("\nEncerrando o chat. Até logo!")
                break

            if mensagem.lower() == "historico":
                registros = listar_historico()
                print("\n--- Histórico Salvo no Banco ---")
                if not registros:
                    print("Nenhuma conversa gravada ainda.")
                else:
                    for papel, texto, data_hora in registros:
                        print(f"[{data_hora}] {papel.upper()}: {texto}")
                print("--------------------------------")
                continue

            if mensagem.lower() == "limpar":
                limpar_historico()
                print("\n🧹 Histórico limpo com sucesso! Você pode iniciar uma nova conversa.")
                continue

            # 1. Salva a fala do usuário no banco local
            salvar_mensagem(papel="usuario", mensagem=mensagem)

            # 2. Envia para a StackSpot AI responder
            print("Robô pensando...")
            resposta_ia = enviar_mensagem_stackspot(mensagem)

            # 3. Salva a resposta da IA no banco local
            salvar_mensagem(papel="bot", mensagem=resposta_ia)

            # 4. Exibe na tela
            print(f"\nAssistente: {resposta_ia}")

        except KeyboardInterrupt:
            print("\n\nOperação cancelada. Saindo...")
            sys.exit(0)
        except Exception as erro:
            print(f"\n❌ Ocorreu um erro: {erro}")


if __name__ == "__main__":
    main()