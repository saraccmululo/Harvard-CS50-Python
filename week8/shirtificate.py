from fpdf import FPDF

class PDF():
    def __init__(self, user_name):
        self._pdf=FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255,255,255)
        self._pdf.text(x=47.5, y=140, text=f"{user_name} took CS50")


    def save(self,pdf_name):
        self._pdf.output(pdf_name)


user_name = input("Name: ")
pdf = PDF(user_name)
pdf.save("shirtificate.pdf")



