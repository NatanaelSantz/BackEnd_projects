from cpf_cnpj import Document
cpf= 50440192838
cpf = str(cpf)
cnpj_t = 45021766000191
cnpj = str(cnpj_t)

document = Document.create_document(cnpj)
print(document)
