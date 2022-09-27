from cpf_cnpj import Document
cpf= input("digite seu CPF:")
cpf = str(cpf)
cnpj_t = input("digite seu CNPJ: ")
cnpj = str(cnpj_t)

document = Document.create_document(cpf)
document = Document.create_document(cnpj)
print(document)
# 10630743000107
# 50440192838
