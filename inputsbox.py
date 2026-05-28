import tkinter as tk

global rets 

rets=""

class myapps:
    def __init__(self,root:tk.Tk,title:str,text:str,backgrounds:str,foregrounds:str):
        self.root=root
        self.root.title(title)
        self.root.configure(background=backgrounds)
        self.label=tk.Label(background=backgrounds,foreground=foregrounds,text=text)
        self.label.pack(padx=10,pady=10)
        self.text=tk.Entry(background=backgrounds,foreground=foregrounds)
        self.text.pack(padx=10,pady=10)
        self.button=tk.Button(background=backgrounds,foreground=foregrounds,command=self.oks,text="ok")
        self.button.pack(padx=10,pady=10)

    def oks(self):
        global rets
        a=self.text.get()
        rets=a
        self.root.quit()


def inputs(title:str="input?",text:str="wask?",backgrounds:str="black",foregrounds:str="white"):
    root=tk.Tk()
    apps=myapps(root,title,text,backgrounds,foregrounds)
    root.mainloop()
    return rets




a=inputs(title="input",text="get me x?")
print(a)