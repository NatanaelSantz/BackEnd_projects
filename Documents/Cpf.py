from validate_docbr import CPF

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
  
