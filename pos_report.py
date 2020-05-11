from tkinter import *
from tkinter import messagebox
import sqlite3
# import smtplib
import matplotlib.pyplot as plt
import datetime
from tkinter import simpledialog
from tkinter import ttk

table = datetime.datetime.now()
print(table)
table_name=table.strftime("%x")
window = Tk()

window.configure(bg='black')
window.title("Store app ")
window.geometry("1000x1000")
total_price = []
item_list = []
price_list = []
quantity_list=[]
total_sales = []
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
    global table_name
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

                # if records[k][0] == "coco coffe na":
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

def net_sales():
    # monthly_report = Tk()
    report_list=[]
    overall_report = {}

    month_ = simpledialog.askstring("Date", "Enter Month in this format (02/2020) please?",parent=window)
    # print(month_[0:2] + "/" + '0' + '2' + month_[2:7])

    # (02 / 24 / 20)
    conn = sqlite3.connect('orders.db')
    c = conn.cursor()
    for q in range(1,31):

        try:
            # if q == 1 - 9 then add 0
            month = """SELECT * from '{}'""".format(month_[0:3]+str(0) +str(q)+ month_[2:5])
            c.execute(month)
            report_list.append(month)
            # print(month[3:5])
        except:
            pass

        finally:
            pass
        continue
    # print(set(report_list))
    report_list = list(set(report_list))
    print(report_list)
    for day in report_list:


        price_of_product = []
        product = []
        quantity_sold = []
        total_cost = []


        conn = sqlite3.connect('orders.db')
        c = conn.cursor()
        query = """{}""".format(day)
        c.execute(query)
        records = c.fetchall()
        print("total rows", len(records))

        # price_of_product = []
        # product = []
        # quantity_sold = []
        # total_cost = []
        # ================================================
        for k in range(0, len(records)):
            item = str(records[k][0])
            price_ = int(records[k][1])
            quantity_=int(records[k][2])
            total_= float(records[k][3])

            product.append(item)
            price_of_product.append(price_)
            quantity_sold.append(quantity_)
            total_cost.append(total_)
        overall_report[str(quantity_sold)] = sum(total_cost)

        # print(day[15:-1] , "  =  ", product,price_of_product,quantity_sold,total_cost)

        # monthly_report.configure(bg='black')
        # monthly_report.title("Store app ")
        # monthly_report.geometry("1000x1000")
        #
        # for i in report_list:
        #     Label(monthly_report, text=day[15:-1], bg="black", fg="white", font="times 12 bold").grid(row=10, column=100)
        #     Label(monthly_report,)
        #
        # monthly_report.mainloop()
        # monthly_report = Tk()
        q = 0
        print(day[15:-1])
        for t in product:
            # print(day[15:-1])
            # for g in range(len(product)):
            print("\n"+ str(product[q]) +"\t"+str(price_of_product[q])+'\t'+ str(quantity_sold[q])+ "\t"+ str(total_cost[q])+"\n")
            q += 1
        print("sfawfadfaf")
        keys = overall_report.keys()
        overall_revenue = overall_report.values()


        print("keys", keys)
        print("Revenue", overall_revenue)
        products_sum = 0
        for k in quantity_sold:
            products_sum += float(k)
        print(products_sum)

        revenue = 0
        for v in overall_revenue:
            revenue += float(v)

        print(revenue)

    messagebox.showinfo("Revenue", "TOTAL ITEM SOLD: " + str(products_sum)+" and revenue: "+ str(revenue))




        # for k,v in overall_report.items():
        #     print(k, v)

        # total_sold = 0
        # for x in sold:
        #     total_sold += x
        # print(total_sold)

    # query = """SELECT * from '{}'""".format(date_)
    # c.execute(query)
    # records = c.fetchall()
    # print("total rows", len(records))
    #
    # # ================================================
    # for k in range(0, len(records)):
    #     if records[k][0] == "coco coffe na":
    #         item = str(records[k][0])
    #         sale = int(records[k][2])
    #
    #         items.append(item)
    #         sold.append(sale)
    # total_sold = 0
    # for x in sold:
    #     total_sold += x
    # print(total_sold)

# signin()
db_()
# authorization




# messagebox.askquestion("password","Enter Code: ")
# p = Entry(login,width=20,bg="black", fg="white")
# p.grid(row=10, column=200,sticky=W)
# Button(login, text= "ENTER", width=20, command= signin , bg="blue", fg = "white").grid(row=15, column=100, sticky= W)
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
Button(window, text="Today's VISUAL", width=50, command= visual , bg="red", fg = "white").grid(row = 1, column=400, sticky=W)
Button(window, text="Net Sales Of The Month", width=50, command= net_sales , bg="skyblue", fg = "black").grid(row = 3, column=400, sticky=W)
Button(window, text="PREVIOUS SALES", width=50, command= history , bg="lightblue", fg = "black").grid(row = 2, column=400, sticky=W)
window.mainloop()