from validate_docbr import CNPJ 
# validação e mascara do CNPJ
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
  
