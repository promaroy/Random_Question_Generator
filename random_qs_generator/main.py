from fpdf import FPDF
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user=<your username>,
  passwd=<your password>,
  database=<database name>
)

mycursor = mydb.cursor()

subject = input('''Enter one of the following subjects...
                1. OOPS
                2. DSA
                3. COA\n''')
number = int(input("Enter the number of questions\n"))
if subject == "OOPS":
    #sql=" SELECT * FROM OOPS ORDER BY RAND() LIMIT %s "
    val = (number)
    mycursor.execute("""SELECT * FROM OOPS ORDER BY RAND() LIMIT %s """ %(val))
    myres=mycursor.fetchall()
    pdf = FPDF()

    # Add a page
    pdf.add_page()

# set style and size of font
# that you want in the pdf
    pdf.set_font("Arial", size = 15)
    pdf.cell(200,10,txt="Questions on OOPS",align='C')
    pdf.ln(11)

# create a cell
    CN=0
    for x in myres:
        CN=CN+1
        pdf.cell(1,10,txt=str(CN),align='L')
        pdf.cell(20)
        for c in x:
            pdf.cell(200, 10, txt=c,
            align = 'L')
        pdf.ln(10)



    pdf.output("QUESTIONS.pdf")

elif subject == "DSA":
    sql="SELECT * FROM DSA ORDER BY RAND() LIMIT (%s)"

    val=number
    mycursor.execute("""SELECT * FROM DSA ORDER BY RAND() LIMIT %s """ %(val))
    myres=mycursor.fetchall()
    #for x in myres:
    #    print(x)
    pdf = FPDF()

    # Add a page
    pdf.add_page()

# set style and size of font
# that you want in the pdf
    pdf.set_font("Arial", size = 15)
    pdf.cell(200,10,txt="Questions on DSA",align='C')
    pdf.ln(11)
# create a cell
    CN=0
    for x in myres:
        CN=CN+1
        pdf.cell(1,10,txt=str(CN),align='L')
        pdf.cell(20)
        for c in x:
            pdf.cell(200, 10, txt=c,
            align = 'L')
        pdf.ln(10)





    pdf.output("QUESTIONS.pdf")

elif subject == "COA":
    #sql="SELECT * FROM COA ORDER BY RAND() LIMIT (%s)"
    val = number
    mycursor.execute("""SELECT * FROM COA ORDER BY RAND() LIMIT %s """ %(val))
    myres=mycursor.fetchall()
    #for x in myres:
    #    print(x)
    pdf = FPDF()

    # Add a page
    pdf.add_page()

# set style and size of font
# that you want in the pdf
    pdf.set_font("Arial", size = 15)
    pdf.cell(200,10,txt="Questions on COA",align='C')
    pdf.ln(11)
# create a cell
    CN=0
    for x in myres:
        #x=[1,]+x
        CN=CN+1
        pdf.cell(1,10,txt=str(CN),align='L')
        pdf.cell(20)
        for c in x:

            pdf.cell(200, 10, txt=c,
            align = 'L')
        pdf.ln(10)


    pdf.output("QUESTIONS.pdf")

else:
    print("Subject Questions not present\n")
