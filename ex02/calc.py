import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    button = event.widget
    num = button["text"]
    if num == "=":
        eqn = entry.get()
        res = eval(eqn)
        entry.delate(0, tk.END)
        entry.insert(tk.END, res)
    else:    
        #tkm.showinfo("", f"{num}のボタンがクリックされました")
        entry.insert(tk.END, num)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("calc")
    #root.geometry("300x500")

    entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
    entry.grid(row=0, column=0, columnspan=3)

    r, c = 0, 0    #r:行番号 c:列番号
    for i,num in enumerate([i for i in range(9, -1, -1)]+["+"]+["="]):
        button = tk.Button(root,
                          text=f"{num}",
                          width=4,
                          height=2,
                          font=("Times New Roman", 30)
                        )
        button.bind("<1>", button_click)
        button.grid(row=r, column=c)
        c += 1
        if (i+1)%3 == 0:
            r += 1
            c = 0

root.mainloop()
