from tkinter import *
import random
import time;
import os

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management system")

text_Input = StringVar()
operator = ""

Tops= Frame(root,width=1600,height=50,bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1= Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2= Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

global date

localtime=time.asctime(time.localtime(time.time()))

b= localtime.replace(" ", "")

date= b[0:8]

lb1Info = Label(Tops,font=('arial',50,'bold'),text="Restaurant management systems",fg="Steel Blue",bd=10,anchor='w')
lb1Info.grid(row=0,column=0)
lb1Info2 = Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lb1Info2.grid(row=1,column=0)
#calculator
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqual():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def Ref():
    global costoffries
    global costofdrinks
    global costoffilet
    global costofburger
    global costofchicken
    global costofcheese
    global costofMeal
    global PayTax
    global TotalCost
    global Ser_charge
    global Service
    global overallCost
    global PaidTax
    global randomRef
    
    Cof =float(fries.get())
    cofilet=float(filet.get())
    coburger=float(burger.get())
    cochiburger=float(chickenburger.get())
    cocheese=float(cheeseburger.get())
    codrinks=float(drinks.get())

    costoffries = Cof * 0.99
    costofdrinks = codrinks * 1.00
    costoffilet = cofilet * 2.99
    costofburger = coburger * 2.87
    costofchicken = cochiburger * 2.89
    costofcheese = cocheese * 2.69

    costofMeal = "£", str('%.2f' % (costoffries + costofburger + costofcheese + costofchicken + costofdrinks + costoffilet))
    PayTax = ((costoffries + costofburger + costofcheese + costofchicken + costofdrinks + costoffilet) * 0.2 )
    TotalCost = (costoffries + costofburger + costofcheese + costofchicken + costofdrinks + costoffilet)
    Ser_charge =((costoffries + costofburger + costofcheese + costofchicken + costofdrinks + costoffilet)/99)
    Service = "£", str('%.2f' % Ser_charge)
    overallCost = "£",str('%.2f' % (PayTax + TotalCost + Ser_charge))
    PaidTax = "£", str('%.2f' % PayTax)
    service.set(Service)
    cost.set(costofMeal)
    tax.set(PaidTax)
    subtotal.set(costofMeal)
    total.set(overallCost)
    
    
def convertTuple(tup): 
    str =  ''.join(tup) 
    return str

def submit():
	global MYDIR
	MYDIR = (date)
	CHECK_FOLDER = os.path.isdir(MYDIR)
	global d
	d=os.getcwd()
	if not CHECK_FOLDER:
		os.makedirs(MYDIR)
		file()
	else:
		file()

def file():
	global ref
	ref=1000
	nof= str(fries.get())
	noc= str(filet.get())
	nob= str(burger.get())
	nocb= str(chickenburger.get())
	noccb= str(cheeseburger.get())
	nod= str(drinks.get())
	cof= str(costoffries)
	coc= str(costoffilet)
	cob= str(costofburger)
	cocb= str(costofchicken) 
	coccb= str(costofcheese)
	cod= str(costofdrinks)
	com= convertTuple(costofMeal)
	ser= convertTuple(Service)
	oc= convertTuple(overallCost)
	ptax= convertTuple(PaidTax)
	sub=convertTuple(costofMeal)
	i=0
	while i==0:
		d1=os.path.join(d,MYDIR)
		name= str(date+" "+str(ref))
		filename= os.path.join(d1, name+".txt")
		file_exists = os.path.isfile(filename)
		if file_exists:
			ref=ref+1
		else:
			i=1

	d1=os.path.join(d,MYDIR)
	fname= os.path.join(d1, name+".txt")
	file= open(fname,"w")
	file.write("------------Restaurant-----------------"+"\n")
	file.write("Reference No"+str(ref)+"\n")
	file.write("Items         Quantity\t Price\n")
	file.write("Fires"+"             "+nof+"\t  £"+cof+"\n")
	file.write("Burger"+"            "+nob+"\t  £"+cob+"\n")
	file.write("Filet"+"             "+noc+"\t  £"+coc+"\n")
	file.write("Cheese Burger"+"     "+nocb+"\t  £"+coccb+"\n")
	file.write("Chiken Burger"+"     "+noccb+"\t  £"+cocb+"\n")
	file.write("Drinks"+"            "+nod+"\t  £"+cod+"\n")
	file.write("-------------Tax------------------------\n")
	file.write("Cost of Meal"+"              "+com+"\n")
	file.write("Service Tax"+"               "+ser+"\n")
	file.write("Paid Tax"+"                  "+ptax+"\n")
	file.write("Subtotal"+"                  "+sub+"\n")
	file.write("---------------------------------------"+"\n")
	file.write("Total"+"                     "+oc+"\n")    
	file.close()
	ref_no.set(ref)

	popup = Tk()
	popup.wm_title("Paid")
	popup.geometry("350x50")
	label = Label(popup, text="Bill Paid Successfully with Reference no:"+str(ref), font=("Arial",10,"bold")).grid(column=0, row=0,columnspan=3)
	B1 = Button(popup, font=("Arial",10,"bold"),text="Okay", command = popup.destroy).grid(column=1, row=3)
	popup.mainloop()

def qExit():
    root.destroy()

def Reset():
    ref_no.set(0)
    fries.set(0)
    burger.set(0)
    filet.set(0)
    subtotal.set(0)
    total.set(0)
    service.set(0)
    drinks.set(0)
    tax.set(0)
    cost.set(0)
    chickenburger.set(0)
    cheeseburger.set(0)





txtD=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",justify='right')
txtD.grid(columnspan=4)

btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="powder blue",command=lambda:btnClick(1)).grid(row=2,column=0)
btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="powder blue",command=lambda:btnClick(2)).grid(row=2,column=1)
btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="powder blue",command=lambda:btnClick(3)).grid(row=2,column=2)
sub=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="powder blue",command=lambda:btnClick("-")).grid(row=2,column=3)
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="powder blue",command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="powder blue",command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="powder blue",command=lambda:btnClick(6)).grid(row=3,column=2)
Add=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="powder blue",command=lambda:btnClick("+")).grid(row=3,column=3)
btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=4,column=0)
btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=4,column=1)
btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="powder blue",command=lambda:btnClick(9)).grid(row=4,column=2)
mul=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="powder blue",command=lambda:btnClick("*")).grid(row=4,column=3)
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="powder blue",command=lambda:btnClick(0)).grid(row=5,column=0)
clear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="c",bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)
Equal=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",bg="powder blue",command=btnEqual).grid(row=5,column=2)
div=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="powder blue",command=lambda:btnClick("/")).grid(row=5,column=3)
dot=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text=".",bg="powder blue",command=lambda:btnClick(".")).grid(row=6,column=2)
#----------------------------------------------------------------------------

global fries
global burger
global filet
global drinks
global chickenburger
global cheeseburger

ref_no= IntVar()
fries=IntVar()
burger=IntVar()
filet=IntVar()
subtotal=IntVar()
total=IntVar()
service=IntVar()
drinks=IntVar()
tax=IntVar()
cost=IntVar()
chickenburger=IntVar()
cheeseburger=IntVar()


lblReference = Label(f1,font=('arial',16,'bold'),text="Reference",bd=16 , anchor= 'w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=ref_no,bd=10 ,insertwidth=4,bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblfries = Label(f1,font=('arial',16,'bold'),text="Fries",bd=16 , anchor= 'w')
lblfries.grid(row=1,column=0)
txtfries=Entry(f1,font=('arial',16,'bold'),textvariable=fries,bd=10 ,insertwidth=4,bg="powder blue",justify='right')
txtfries.grid(row=1,column=1)

lblburger = Label(f1,font=('arial',16,'bold'),text="Burger",bd=16 , anchor= 'w')
lblburger.grid(row=2,column=0)
txtburger=Entry(f1,font=('arial',16,'bold'),textvariable=burger,bd=10 ,insertwidth=4,bg="powder blue",justify='right')
txtburger.grid(row=2,column=1)

lblfilet = Label(f1,font=('arial',16,'bold'),text="Filet",bd=16 , anchor= 'w')
lblfilet.grid(row=3,column=0)
txtfilet=Entry(f1,font=('arial',16,'bold'),textvariable=filet,bd=10 ,insertwidth=4,bg="powder blue",justify='right')
txtfilet.grid(row=3,column=1)

lblchicken = Label(f1,font=('arial',16,'bold'),text="Chicken Burger",bd=16 , anchor= 'w')
lblchicken.grid(row=4,column=0)
txtchicken=Entry(f1,font=('arial',16,'bold'),textvariable=chickenburger,bd=10 ,insertwidth=4,bg="powder blue",justify='right')
txtchicken.grid(row=4,column=1)

lblcheese = Label(f1,font=('arial',16,'bold'),text="Cheese Burger",bd=16 , anchor= 'w')
lblcheese.grid(row=5,column=0)
txtcheese=Entry(f1,font=('arial',16,'bold'),textvariable=cheeseburger,bd=10 ,insertwidth=4,bg="powder blue",justify='right')
txtcheese.grid(row=5,column=1)
#-------------------------2side------------------------------
lblDrinks = Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16 , anchor= 'w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=drinks,bd=10 ,insertwidth=4,bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblservice = Label(f1,font=('arial',16,'bold'),text="Service",bd=16 , anchor= 'w')
lblservice.grid(row=1,column=2)
txtservice=Entry(f1,font=('arial',16,'bold'),textvariable=service,bd=10 ,insertwidth=4,bg="powder blue",justify='right')
txtservice.grid(row=1,column=3)

lblcost = Label(f1,font=('arial',16,'bold'),text="cost",bd=16 , anchor= 'w')
lblcost.grid(row=2,column=2)
txtcost=Entry(f1,font=('arial',16,'bold'),textvariable=cost,bd=10 ,insertwidth=4,bg="powder blue",justify='right')
txtcost.grid(row=2,column=3)

lbltax = Label(f1,font=('arial',16,'bold'),text="Tax",bd=16 , anchor= 'w')
lbltax.grid(row=3,column=2)
txttax=Entry(f1,font=('arial',16,'bold'),textvariable=tax,bd=10 ,insertwidth=4,bg="powder blue",justify='right')
txttax.grid(row=3,column=3)

lblsubtotal = Label(f1,font=('arial',16,'bold'),text="Subtotal",bd=16 , anchor= 'w')
lblsubtotal.grid(row=4,column=2)
txtsubtotal=Entry(f1,font=('arial',16,'bold'),textvariable=subtotal,bd=10 ,insertwidth=4,bg="powder blue",justify='right')
txtsubtotal.grid(row=4,column=3)

lbltotal = Label(f1,font=('arial',16,'bold'),text="Total Amount",bd=16 , anchor= 'w')
lbltotal.grid(row=5,column=2)
txttotal=Entry(f1,font=('arial',16,'bold'),textvariable=total,bd=10 ,insertwidth=4,bg="powder blue",justify='right')
txttotal.grid(row=5,column=3)
#-------------------------------BUttons--------------------------------------------------------

btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="powder blue",command= Ref).grid(row=7,column=1)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="powder blue",command= Reset).grid(row=7,column=2)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command= qExit).grid(row=7,column=3)
btnSubmit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Submit",bg="powder blue",command= submit).grid(row=7,column=4)

root.mainloop()