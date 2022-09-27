from Cpf import DocCpf
from Cnpj import DocCnpj
from Cnh import DocCnh
from pis import DocPis
type_doc = input("Digite o tipo de documento: ").upper()
## Cria a validação e o factore que gerencia qual validação de qual documento será feito
class Document:
  @staticmethod
  def create_document(document):
    if type_doc  == "CPF":
      return DocCpf(document)
    elif type_doc == "CNPJ":
      return DocCnpj(document)
    elif type_doc == "CNH":
      return DocCnh(document)
    elif type_doc == "PIS":
      return DocPis(document)
    else:
      raise ValueError("Invalid document, missing digits!")


