from cpf_cnpj import Document
type_doc = input("Digite o tipo de documento: ").upper()
if type_doc == "CPF":
  cpf= input("digite seu CPF:")
  cpf = str(cpf)
  document1 = Document.create_document(cpf)
  print(f"CPF: %s" % document1)
elif type_doc == "CNPJ":
  cnpj_t = input("digite seu CNPJ:")
  cnpj = str(cnpj_t)
  document2 = Document.create_document(cnpj)
  print(f"CNPJ: %s" % document2)
else:
  print("Unknown type doc: %s" % type_doc)





# 10630743000107
# 50440192838
