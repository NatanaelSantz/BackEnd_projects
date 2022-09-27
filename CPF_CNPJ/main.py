from cpf_cnpj import Document
cpf= input("digite seu CPF:")
cpf = str(cpf)
cnpj_t = input("digite seu CNPJ:")
cnpj = str(cnpj_t)

document1 = Document.create_document(cpf)
document2 = Document.create_document(cnpj)
print(f"""CPF:{document1} 
CNPJ:{document2}""")

# 10630743000107
# 50440192838
