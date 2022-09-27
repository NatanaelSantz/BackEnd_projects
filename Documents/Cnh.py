from validate_docbr import CNH


class DocCnh:
  def __init__(self, document):
    if self.validate(document):
      self.cnh = document
    else:
       raise ValueError("Document invalid: %s" % document)
     
  def __str__(self):
    return self.format()
  
  def validate(self,document):
    validateCNH = CNH()
    return validateCNH.validate(document)
  
  def format(self):
    mask = CNH()
    return mask.mask(self.cnh)
  
     
