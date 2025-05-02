import sys
sys.path.append("C:\Users\lbule\OneDrive\Documentos\Source\deepstart\OpenManus")  # ajuste conforme sua pasta
from django.core.management.base import BaseCommand
from openmanus.agents import ManusAgent  # Certifique-se de que OpenManus está instalado

class Command(BaseCommand):
    help = 'Executa o agente Manus do OpenManus'

    def handle(self, *args, **kwargs):
        agent = ManusAgent()
        print("Agente iniciado! Digite sua entrada:")
        while True:
            try:
                prompt = input(">> ")
                if prompt.lower() in {"exit", "quit"}:
                    print("Encerrando agente.")
                    break
                response = agent.run(prompt)
                print(f"\nResposta:\n{response}\n")
            except KeyboardInterrupt:
                print("\nAgente encerrado por interrupção.")
                break
