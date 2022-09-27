from validate_docbr import PIS 
# Class de validação e mascara do PIS/PASEP
class DocPis:
  def __init__(self,document):
    if self.validate(document):
      self.pis = document
    else:
      raise ValueError("Document invalid: %s" % document)
        
  def __str__(self):
    return self.format()
  
  def validate(self, document):
    validate = PIS()
    return validate.validate(document)
  
  def format(self):
    mask = PIS()
    return mask.mask(self.pis)
  
