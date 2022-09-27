from Cpf import DocCpf
from Cnpj import DocCnpj
from Cnh import DocCnh

type_doc = input("Digite o tipo de documento: ").upper()

class Document:
  @staticmethod
  def create_document(document):
    if type_doc  == "CPF":
      return DocCpf(document)
    elif type_doc == "CNPJ":
      return DocCnpj(document)
    elif type_doc == "CNH":
      return DocCnh(document)
    else:
      raise ValueError("Invalid document, missing digits!")


