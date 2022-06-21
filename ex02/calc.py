import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("calc")
    root.geometry("300x500")

r, c = 0, 0    #r:行番号 c:列番号
for num in range(9, -1, -1):
    button = tk.Button(root,
                      text=f"{num}",
                      width=4,
                      height=2,
                      font=("Times New Roman", 30)
                  )
    button.grid(row=r, column=c)
    c += 1
    if (num-1)%3 == 0:
        r += 1
        c = 0


root.mainloop()
