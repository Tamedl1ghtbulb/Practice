from fpdf import FPDF
import fpdf
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.image(r"shirtificate.png", x=0, y=60)
pdf.set_font(family= 'Arial',style='B')
pdf.set_font_size(18)
pdf.set_text_color( r=255, g=255, b=255)
pdf.cell(0,230, 'Ognjen Radojevic took CS50',align='C')
pdf.set_text_color( r=0, g=0, b=0)
pdf.set_font_size(30)
pdf.cell(-198)
pdf.cell(0,0,'CS50 Shirtificate',align='C')

pdf.set_text_color( r=0, g=0, b=0)
pdf.set_font("helvetica", "B", 16)

#pdf.multi_cell(txt='Ognjen Radojevic took CS50',w=0,align='C')

pdf.output("shirtificate.pdf")
