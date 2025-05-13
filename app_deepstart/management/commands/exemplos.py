
import spacy       

nlp = spacy.load("pt_core_news_sm")        

doc = nlp("Ulisses foi ao bar Overflow no centro da cidade de São Paulo.")   
for token in doc:
    print(f"TOKEN: {token.text}\tLEMMA: {token.lemma_}\tPOS: {token.pos_}\tTAG: {token.tag_}\tDEP: {token.dep_}")

doc = nlp("O presidente Lula visitou Brasília em janeiro de 2023.")

for ent in doc.ents:
    print(f"ENTIDADE: {ent.text} \t| TIPO: {ent.label_}")    