from tkinter import *
from tkinter import messagebox
import sqlite3
# import smtplib
import matplotlib.pyplot as plt
import datetime

table = datetime.datetime.now()
print(table)
table_name=table.strftime("%x")
window = Tk()
login = Tk()
window.configure(bg='black')
window.title("Store app ")
window.geometry("1000x1000")
total_price = []
item_list = []
price_list = []
quantity_list=[]
num_bill= [1]
items = []
sold = []
def db_():
    global table_name
    db_name= str(table_name)+".db"
    conn = sqlite3.connect('orders.db')
    # conn = sqlite3.connect(str(table_name)+'.db')

    c = conn.cursor()
    sql_query = "CREATE TABLE IF NOT EXISTS '{}' (item TEXT, Price TEXT, Quantity TEXT, total TEXT)".format(table_name)
    c.execute(sql_query)
    conn.commit()
    conn.close()



def click(*args):
    item_ = item.get()
    price_ = price.get()
    quantity_ = quantity.get()
    bill.insert(END,item_)
    bill.insert(END,"\tRs.")
    bill.insert(END,price_)
    bill.insert(END,"\tQuantity: "+quantity_)
    bill.insert(END,"\t\tPrice: "+str(float(price_) * float(quantity_)))
    total_price.append(float(price_) * float(quantity_))
    item_list.append(item_)
    price_list.append(price_)
    quantity_list.append(quantity_)
    # adding to database
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    # query = """SELECT * from sales"""
    # c.execute(query)
    # records = c.fetchall()
    # print("total rows", len(records))
    c.execute('INSERT INTO "{}" (item, Price, Quantity, total) VALUES (?,? ,?, ?)'.format(table_name), (str(item_), str(price_), str(quantity_), str(total_price[-1])))
    conn.commit()
    # --------------------------------------------------
    bill.insert(END,"\n")
    item.delete(0, "end")
    price.delete(0, "end")
    quantity.delete(0,"end")


def generate_bill(*args):
    total_bill = 0

    f = open("bill"+str(num_bill[-1])+".txt", "w+")
    num_bill.append(num_bill[0]+num_bill[-1])
    for c in range(len(item_list)):
        f.write(str(item_list[c])+"\t\t"+str(price_list[c])+"\t\t"+str(quantity_list[c])+"\t\t" +str(total_price[c]))
        f.write("\n")

    for i in total_price:
        total_bill += i


    total_price.clear()
    item_list.clear()
    price_list.clear()
    quantity_list.clear()
    messagebox.showinfo("Overall Bill", "TOTAL BILL IS "+str(total_bill))
    bill.delete('1.0', END)

def visual():
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    query = """SELECT * from '{}'""".format(table_name)
    c.execute(query)
    records = c.fetchall()
    print("total rows", len(records))

    # ================================================
    for k in range(0,len(records)):
        if records[k][0] == "coco coffe na":
            item = str(records[k][0])
            sale = int(records[k][2])

            items.append(item)
            sold.append(sale)
    total_sold = 0
    for x in sold:
        total_sold += x
    print(total_sold)
    plt.bar(items,sold)
    plt.legend()

    plt.xlabel('Items')
    plt.ylabel("Quantity Sold")

    plt.title("Sale graph")

    plt.show()



    # =====================================================
    c.close()

def history():
    from tkinter import simpledialog
    date_ =simpledialog.askstring("Date", "Enter Date in this format (02/24/20) please?",
                           parent=window)
    print(date_)
    if date_ == '':
        messagebox.showinfo("wrong", "please enter something ")
    else:
        if date_[2] == '/':
            print("correct")
            conn = sqlite3.connect('orders.db')
            c = conn.cursor()
            query = """SELECT * from '{}'""".format(date_)
            c.execute(query)
            records = c.fetchall()
            print("total rows", len(records))

        # ================================================
            for k in range(0, len(records)):
                if records[k][0] == "coco coffe na":
                    item = str(records[k][0])
                    sale = int(records[k][2])

                    items.append(item)
                    sold.append(sale)
            total_sold = 0
            for x in sold:
                total_sold += x
            print(total_sold)
            plt.bar(items, sold)
            plt.legend()

            plt.xlabel('Items')
            plt.ylabel("Quantity Sold")

            plt.title("Sale graph")

            plt.show()

        # =====================================================
            c.close()
        else:
            messagebox.showerror("Error", "correct the format please")
def signin(*args):
    code = p.get()
    if code =="00":
        return True
    else:
        messagebox.showerror("Error","Incorrect password")
        quit()

# signin()
db_()
# authorization

login.configure(bg='black')
login.title("Store app ")
login.geometry("1000x1000")

Label(login, text="Password", bg="black",fg="white",font="times 12 bold").grid(row=10,column=100)
# messagebox.askquestion("password","Enter Code: ")
p = Entry(login,width=20,bg="black", fg="white")
p.grid(row=10, column=200,sticky=W)
Button(login, text= "ENTER", width=20, command= signin , bg="blue", fg = "white").grid(row=15, column=100, sticky= W)
# signin()
# Label
Label(window, text= "POINT OF SALE", bg="red",fg="black", font="times 24 bold").grid(row=0,column=100)
Label(window, text="Item", bg = "black",fg="white", font="none 12 bold").grid(row= 5 , column=15, sticky= W)
Label(window, text="Price", bg = "black",fg="white", font="none 12 bold").grid(row= 7 , column=15, sticky= W)
Label(window, text="Quantity", bg = "black",fg="white", font="none 12 bold").grid(row= 9 , column=15, sticky= W)
Label(window, text="Total Bill", bg = "black",fg="white", font="none 12 bold").grid(row= 10 , column=100, sticky= W)

# entry
item = Entry(window, width=20, bg="black", fg="white")
item.grid(row=5, column=20,sticky=W)

price = Entry(window, width=20, bg="black", fg="white")
price.grid(row=7, column=20,sticky=W)

quantity = Entry(window, width=20, bg="black", fg="white")
quantity.grid(row=9, column=20,sticky=W)

bill = Text(window, width=50,height=5, wrap=WORD, bg="white", fg="black")
bill.grid(row=11, column=100,sticky=E)

Button(window, text= "POST", width=20, command= click , bg="blue", fg = "white").grid(row=5, column=100, sticky= W)
Button(window, text="DONE", width= 50, command= generate_bill, bg="black", fg = "white").grid(row = 0, column=400, sticky=W)
Button(window, text="VISUAL", width=50, command= visual , bg="red", fg = "white").grid(row = 1, column=400, sticky=W)
Button(window, text="PREVIOUS SALES", width=50, command= history , bg="lightblue", fg = "black").grid(row = 2, column=400, sticky=W)
window.mainloop()