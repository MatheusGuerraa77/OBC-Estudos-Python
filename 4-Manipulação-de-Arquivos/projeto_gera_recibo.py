from fpdf import FPDF
from num2words import num2words
from datetime import date

# 1 - Variáveis

cliente = input("Informe o nome do cliente:\n")
consulta = input("Informe o tipo da consulta:\n")
valor = input("Informe o valor da consulta:\n")
valor_msg = f"{valor} reais"
valor_extenso = num2words(float(valor), lang="pt-br")
valor_extenso_msg = f"{valor_extenso} reais"
data = date.today()
dia = data.day
mes = data.month
ano = data.year

# 2 - Layout do recibo

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "", 20)
pdf.image("dados/rec.jpg", x=0, y=0)
pdf.text(162, 45, valor_msg)
pdf.text(80, 86, cliente)
pdf.text(80, 108, valor_extenso_msg)
pdf.text(80, 135, consulta)
pdf.set_text_color(255, 255, 255)
pdf.text(30, 193, str(dia))
pdf.text(50, 193, str(mes))
pdf.text(70, 193, str(ano))
nome_arquivo = f"{cliente.strip()}_{dia}_{mes}_{ano}"
pdf.output(f"{nome_arquivo}.pdf")
print("Recibo gerado com sucesso!")
