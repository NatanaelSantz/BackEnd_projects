class Cpf:
  def __init__(self, documento):
    documento = str(documento)
    if self.cpf_eh_valido(documento):
      self.cpf = documento
    else:
      raise ValueError("CPF INVALID" )  
  def cpf_eh_valido(self, documento):
    if len(documento) == 11:
      return True
    else:
      return False
    #### Fatiamento de str ######
  def __str__(self):
      return self.format_cpf()
  def format_cpf(self):
    cpf_Formatado = f'CPF:{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}' + u'\u2713'
    return cpf_Formatado
 
    
  
     