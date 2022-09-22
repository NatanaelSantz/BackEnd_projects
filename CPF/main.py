from cpf import Cpf
cpf = 50440192839
cpf = str(cpf)
# tamanho_do_cpf = len(str(cpf))
# print(f"O tamanho do cpf {tamanho_do_cpf}")

# cpf_Formatado = f'{cpf[:3]}.({cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
objeto_cpf = Cpf(cpf)
print(objeto_cpf)

