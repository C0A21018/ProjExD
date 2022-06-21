import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    button = event.widget
    num = button["text"]
    if num == "=":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    elif num == 'C':
        entry.delete(0, tk.END)
    elif num == 'B':
        pos_end_prev = len(entry.get())-1
        entry.delete(pos_end_prev, tk.END)
    else:    
        #tkm.showinfo("", f"{num}のボタンがクリックされました")
        entry.insert(tk.END, num)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    #root.geometry("300x500")

    entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
    entry.grid(row=0, column=0, columnspan=4, sticky=tk.EW)

    r, c = 1, 0    #r:行番号 c:列番号
    for i,num in enumerate(['', 'B', 'C', '/', 7, 8, 9, '*', 4, 5, 6,
                          "-", 1, 2, 3, "+", '00', 0, '.', '=']):
        button = tk.Button(root,
                          text=f"{num}",
                          width=3,
                          height=1,
                          font=("Times New Roman", 30)
                        )
        button.bind("<1>", button_click)
        button.grid(row=r, column=c)
        c += 1
        if (i+1)%4 == 0:
            r += 1
            c = 0

root.mainloop()
