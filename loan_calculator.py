"""
Projetc: Tkinter Loan Calculator (Place Manager Layout)
Purpose: Demonstrates building a fully functional  calculator interface to compute loan interset and monthly payments.
Key Concepts:Objects-oriented GUI Design ,Tkinter Grid Layout, StringvVar Data Binding,and Financial Calculations.
Usage: Serves as a desktop utility projects for financial calculations and user input forms.
"""

from tkinter import*

class LoanCalculator:
    def __init__(self):
        window=Tk()#create a window
        window.title("Loan Calculator")
        window.geometry("350x220")
                        
        Label(window,text="Annual Interest rate").grid(row=1,column=1,sticky=W,padx=10,pady=5)
        Label(window,text="Number of years").grid(row=2,column=1,sticky=W,padx=10,pady=5)
        Label(window,text="Loan Amount").grid(row=3,column=1,sticky=W,padx=10,pady=5)
        Label(window,text="Monthly Payment").grid(row=4,column=1,sticky=W,padx=10,pady=5)
        Label(window,text="Total Payment").grid(row=5,column=1,sticky=W,padx=10,pady=5)

        self.annualInterestRateVar=StringVar()
        self.numberOfYearsVar=StringVar()
        self.loanAmountVar=StringVar()
        self.monthlyPaymentVar=StringVar()
        self.totalPaymentVar=StringVar()

        Entry(window,textvariable=self.annualInterestRateVar,justify=RIGHT).grid(row=1,column=2,padx=10)
        Entry(window,textvariable=self.numberOfYearsVar,justify=RIGHT).grid(row=2,column=2,padx=10)
        Entry(window,textvariable=self.loanAmountVar,justify=RIGHT).grid(row=3,column=2,padx=10)

        Label(window,textvariable=self.monthlyPaymentVar,font="Helvetica 10 bold").grid(row=4,column=2,sticky=E,padx=10)
        Label(window,textvariable=self.totalPaymentVar,font="Helvetica 10 bold").grid(row=5,column=2,sticky=E,padx=10)
        Button(window,text="Compute Payment",command=self.computePayment).grid(row=6,column=2,sticky=E,padx=10,pady=10)
        window.mainloop() 
    def computePayment(self):
        try:
            monthlyInterestRate=float(self.annualInterestRateVar.get())/1200
            loanAmount=float(self.loanAmountVar.get())
            numberOfYears=int(self.numberOfYearsVar.get())

            monthlyPayment=loanAmount*monthlyInterestRate/(1-(1/(1+monthlyInterestRate))**(numberOfYears*12))
        
            totalPayment=monthlyPayment*numberOfYears*12
        
            self.monthlyPaymentVar.set(f"${monthlyPayment:,.2f}")
            self.totalPaymentVar.set(f"${totalPayment:,.2f}")
        
    
        except ValueError:
    
             self.monthlyPaymentVar.set("Invalid Input")
             self.totalPaymentVar.set("Invalid Input")
LoanCalculator()



        
            



