from documents import *
# tratativa dos dados, e encaminhando os documentos para validações certas.
if type_doc == "CPF":
  cpf= input("digite seu CPF: ")
  cpf = str(cpf)
  document1 = Document.create_document(cpf)'  '
  print(f"CPF: %s" % document1)
elif type_doc == "CNPJ":
  cnpj_s = input("digite seu CNPJ: ")
  cnpj = str(cnpj_s)
  document2 = Document.create_document(cnpj)
  print(f"CNPJ: %s" % document2)
elif type_doc == "CNH":
  cnh_s = input("digite seu CNH: ")
  cnh = str(cnh_s)
  document3 = Document.create_document(cnh)
  print(f"CNH: %s" % document3)
elif type_doc == "PIS/PASEP" or "PIS":
  pis_s = input("Digite seu PIS/PASEP: ")
  pis = str(pis_s)
  document4 = Document.create_document(pis)
  print(f"PIS/PASEP: %s" % document4)
else:
  raise ValueError("Unknown type doc: %s" % type_doc)




# 10630743000107
# 50440192838
