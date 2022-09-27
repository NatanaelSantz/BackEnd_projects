from validate_docbr import CPF,CNPJ   

class Document:
  @staticmethod
  def create_document(document):
    if len(document)  == 11:
      return DocCpf(document)
    elif len(document) == 14:
      return DocCnpj(document)
    else:
      raise ValueError("Invalid document, missing digits!")

class DocCpf:
  def __init__(self, document):
    if self.validate(document):
        self.cpf = document
    else:
      raise ValueError("Invalid document: %s" % document)
  
  def __str__(self):
    return self.format()

  def validate(self, document):
    validate = CPF()
    return validate.validate(document)
  
  def format(self):
    mask = CPF()
    return mask.mask(self.cpf)
  
class DocCnpj:
  def __init__(self,document):
    if self.validate(document):
      self.cnpj = document
    else:
      raise ValueError("Document invalid: %s" % document)
        
  def __str__(self):
    return self.format()
    
    
  def validate(self,document):
    validateCNPJ = CNPJ()
    return validateCNPJ.validate(document)
  
  def format(self):
    masks = CNPJ() 
    return masks.mask(self.cnpj)
  
