from django.core.management.base import BaseCommand
import spacy

class Command(BaseCommand):
    help = 'Executa 7 exemplos com spaCy usando o modelo pt_core_news_sm'

    def handle(self, *args, **kwargs):
        nlp = spacy.load("pt_core_news_sm")

        # EXEMPLO 1 - Tokenização, lematização e análise morfossintática
        self.stdout.write("\n🧪 Exemplo 1 - Análise de Tokens")
        doc = nlp("Ulisses foi ao bar Overflow no centro da cidade de São Paulo.")
        for token in doc:
            self.stdout.write(f"TOKEN: {token.text}\tLEMMA: {token.lemma_}\tPOS: {token.pos_}\tTAG: {token.tag_}\tDEP: {token.dep_}")

        # EXEMPLO 2 - Reconhecimento de entidades nomeadas
        self.stdout.write("\n🧪 Exemplo 2 - Entidades nomeadas")
        doc = nlp("O presidente Lula visitou Brasília em janeiro de 2023.")
        for ent in doc.ents:
            self.stdout.write(f"ENTIDADE: {ent.text} \t| TIPO: {ent.label_}")

        # EXEMPLO 3 - Frase com múltiplas entidades
        self.stdout.write("\n🧪 Exemplo 3 - Frase com várias entidades")
        doc = nlp("A Apple lançou o iPhone 17 nos Estados Unidos em setembro de 2023.")
        for ent in doc.ents:
            self.stdout.write(f"ENTIDADE: {ent.text} \t| TIPO: {ent.label_}")

        # EXEMPLO 4 - Detecção de datas e eventos
        self.stdout.write("\n🧪 Exemplo 4 - Datas e eventos")
        doc = nlp("O Natal é comemorado em 25 de dezembro no Brasil.")
        for ent in doc.ents:
            self.stdout.write(f"ENTIDADE: {ent.text} \t| TIPO: {ent.label_}")

        # EXEMPLO 5 - Nomes próprios e localizações
        self.stdout.write("\n🧪 Exemplo 5 - Nomes e lugares")
        doc = nlp("Maria viajou de avião para Lisboa e depois seguiu para Paris.")
        for ent in doc.ents:
            self.stdout.write(f"ENTIDADE: {ent.text} \t| TIPO: {ent.label_}")

        # EXEMPLO 6 - Análise de dependência sintática
        self.stdout.write("\n🧪 Exemplo 6 - Dependência sintática")
        doc = nlp("O cachorro correu atrás do carro que estava passando.")
        for token in doc:
            self.stdout.write(f"TOKEN: {token.text}\tDEP: {token.dep_}\tCABEÇA: {token.head.text}")

        # EXEMPLO 7 - Frase com dinheiro e valores
        self.stdout.write("\n🧪 Exemplo 7 - Dinheiro e quantidades")
        doc = nlp("Ela comprou um carro por R$ 45.000,00 em São Paulo.")
        for ent in doc.ents:
            self.stdout.write(f"ENTIDADE: {ent.text} \t| TIPO: {ent.label_}")
