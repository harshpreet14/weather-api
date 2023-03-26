from fpdf import FPDF
import pandas as pd

# Read the employee CSV file
df = pd.read_csv('employee_data.csv')

# Define the font styles
font_bold = ('Times', 'B', 28)
font_normal = ('Times', 'I', 12)

# Define the colors
color_primary = (20, 130, 255)
color_secondary = (0, 0, 0)

# Loop through each employee in the DataFrame
for index, row in df.iterrows():

    # Create a new PDF document for the offer letter
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()
    pdf.set_margins(left=15.4, top=25.4, right=15.4)

    # Set the fill color to blue
    pdf.set_fill_color(212, 241, 249)
    pdf.rect(0, 0, pdf.w, pdf.h, 'F')

    #Add the image
    pdf.image('cognify-logo.png', x=pdf.w/2-75, y=None, w=150, h=45, type='png')

    # Set the border style to 1 (solid)
    pdf.set_draw_color(0, 102, 204)
    pdf.set_line_width(1)
    pdf.rect(5.0, 5.0, pdf.w - 10.0, pdf.h - 10.0)

    # Add the header
    pdf.set_font(*font_bold)
    pdf.set_text_color(*color_primary)
    pdf.cell(w=0, h=20, txt='Offer Letter', align='C')

    pdf.ln(30)

    # Add the employee name
    pdf.set_font('Times', 'B', 20)
    pdf.set_text_color(*color_secondary)
    pdf.cell(w=0, h=10, txt=f"Dear {row['Name']},", align='L', ln=1)
    pdf.ln()

    # Add the body text
    pdf.set_font(*font_normal)
    pdf.set_text_color(*color_secondary)
    pdf.cell(0, 10, f'We are pleased to offer you the position of {row["Position"]} at Cognify.', ln=1)
    pdf.multi_cell(0, 10, f'Your starting salary will be {row["Salary"]}, with benefits including Health insurance, Performance Benfits, Paid Time Off, Flexible work hours or work-from-home options, Professional development, Employee assistance, Performance bonuses or profit sharing, Employee discounts on products, Gym memberships, and Equity in the company')
    pdf.cell(0, 10, f'Your start date will be {row["Joining_Date"]}.', ln=1)

    # Add the footer
    pdf.set_font(*font_normal)
    pdf.set_text_color(*color_secondary)
    pdf.cell(0, 10, 'Please sign and return this offer letter to indicate your acceptance of this position.', align='L')
    pdf.ln()
    pdf.cell(0, 10, 'Sincerely,', align='L')
    pdf.ln()
    pdf.cell(0, 10, 'Jack Williams', align='L')

    # Save the PDF with the employee name as the filename
    filename = f"{row['Name']} - Offer Letter.pdf"
    pdf.output(filename, 'F')

    print(f"Offer letter for {row['Name']} generated as {filename}")


