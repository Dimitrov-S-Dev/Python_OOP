from fpdf import FPDF
class Bill:
    """
    Object that contains data about a bill, such as
    total amount and period of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Person who leaves in the flat
    and pays a share of the bill.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house/(self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Generate a Pdf that contains data about
    the flatmates such as their names, amount and
    period of the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        pdf = FPDF()
        pdf.add_page()

        # Insert title
        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=20, txt="Flatmates Bill", border=1, align="C", ln=1)

        # Insert period label and value
        pdf.cell(w=100, h=20, txt="Period:", border=1)
        pdf.cell(w=100, h=20, txt=bill.period, border=1, ln=1)

        # Insert name and due amount
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=1)
        pdf.cell(w=100, h=20, txt=flatmate1_pay, border=1, ln=1)

        pdf.output(self.filename)


the_bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print("John pays: ", john.pays(bill=the_bill, flatmate2=marry))
print("Marry pays: ", marry.pays(bill=the_bill, flatmate2=john))

pdf_report = PdfReport(filename="Report.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)