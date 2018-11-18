from tkinter import *
from tkinter.messagebox import showwarning
import webbrowser

class App:

    def __init__(self, parent):
        self.p = parent
        self.p.configure(background="white")
        self.p.columnconfigure(1, weight=3)
        self.create_widgets()


    def create_widgets(self):
        self.l1 = Label(self.p, text="Rule (0-255) : ", font="Sans-serif 14", bg="#B0C4DE", bd=1, relief=RAISED)         #Main Window
        self.l1.grid(row=0, column=0, sticky = W+E)
        self.entry1 = Entry(self.p, font="Sans-serif 14", bd=1, relief=GROOVE, bg="#F5FFFA")
        self.entry1.grid(row=0, column=1, sticky = W+E)
        self.entry1.insert(END, '90')

        self.l2 = Label(self.p, text="Width : ", font="Sans-serif 14", bg="#B0C4DE", bd=1, relief=RAISED)                #Width
        self.l2.grid(row=1, column=0, sticky = W+E)
        self.entry2 = Entry(self.p, font="Sans-serif 14", bd=1, relief=GROOVE, bg="#F5FFFA")
        self.entry2.grid(row=1, column=1, sticky = W+E)
        self.entry2.insert(END, '720')

        self.l3 = Label(self.p, text="Height : ", font="Sans-serif 14", bg="#B0C4DE", bd=1, relief=RAISED)               #Height
        self.l3.grid(row=2, column=0, sticky = W+E)
        self.entry3 = Entry(self.p, font="Sans-serif 14", bd=1, relief=GROOVE, bg="#F5FFFA")
        self.entry3.grid(row=2, column=1, sticky = W+E)
        self.entry3.insert(END, '405')

        self.l4 = Label(self.p, text="Generations : ", font="Sans-serif 14", bg="#B0C4DE", bd=1, relief=RAISED)          #Generations
        self.l4.grid(row=3, column=0, sticky=W + E)
        self.entry4 = Entry(self.p, font="Sans-serif 14", bd=1, relief=GROOVE, bg="#F5FFFA")
        self.entry4.grid(row=3, column=1, sticky=W + E)
        self.entry4.insert(END, '20')

        self.l5 = Label(self.p, text="Size of cell : ", font="Sans-serif 14", bg="#B0C4DE", bd=1, relief=RAISED)         #Size of cell
        self.l5.grid(row=4, column=0, sticky=W + E)
        self.entry5 = Entry(self.p, font="Sans-serif 14", bd=1, relief=GROOVE, bg="#F5FFFA")
        self.entry5.grid(row=4, column=1, sticky=W + E)
        self.entry5.insert(END, '15')

        self.btn = Button(self.p, text=" OK ", font="Sans-serif 10", bg="#3CB371"                                        #OK Button
                          , command=self.button_push, pady=0)
        self.btn.grid(row=5, column=0, sticky = W+E, columnspan=2)


    def button_push(self):
        try:
            self.r_value = int(self.entry1.get())                           #Checking for the correct entry
            self.x_value = int(self.entry2.get())
            self.y_value = int(self.entry3.get())
            self.generations = int(self.entry4.get())
            self.size = int(self.entry5.get())
        except ValueError:
            showwarning("Wrong Input", "Please only input NUMBERS")
        else:
            if int(self.r_value) not in range(0,256):
                showwarning("Error", "No such Rule\nPick a Rule between 0 and 255")
            elif int(self.generations) <= 0 or int(self.generations) > 450:
                showwarning("Error", "Can't have that number of generations")
            elif int(self.x_value) <=0 or int(self.y_value) <= 0:
                showwarning('Error', "Bad Geometry\nChange Width and/or Height")
            elif int(self.size) <= 0 or int(self.size) > int(self.x_value/2):               #be positive and less than half the screen size
                showwarning("Error", "Choose a different size for the cells")
            else:
                if self.r_value == None or self.x_value == None or self.y_value == None:
                    pass
                else:
                    self.create_window()


    def create_window(self):
        self.child = Toplevel(self.p)                                       #New Window
        self.child.title("Plotting Window")
        self.child.geometry("{}x{}".format(self.x_value, self.y_value))
        self.child.resizable(False, False)                                  #makes the window NOT resizable

        self.cf1 = Frame(self.child)
        self.cf1.pack(side=TOP, fill = X)
        self.clabel = Label(self.cf1, text="Rule #{}".format(self.r_value), font="Sans-serif 20", bg="#B0C4DE")
        self.clabel.pack(fill=BOTH, expand=1)
        self.cf2 = Frame(self.child)

        self.create_canvas()


    def create_canvas(self):
        self.cf2.pack(side=BOTTOM, fill=BOTH, expand=1)
        self.canvas = Canvas(self.cf2, bg = "#F5FFFA")
        self.canvas.pack(fill=BOTH, expand=1)
        self.top_left_x, self.top_left_y = 0, 0

        self.create_info()
        self.CA()


    def create_info(self):

        self.clabel2 = Label(self.cf2, text="Additinal Info: ", font="Sans=serif 20", fg="black", bg="#8677AF")
        self.clabel2.pack(fill=BOTH, expand=0)

        self.wiki_link = Label(self.cf2, text="Wiki", font="Sans=serif 14", fg="blue", cursor="hand2")               #HYPERLINKS 
        self.wiki_link.pack(side=LEFT)
        self.wiki_link.bind("<Button-1>", self.callback)

        self.mathworld_link = Label(self.cf2, text="        Math World", font="Sans=serif 14", fg="blue", cursor="hand2")
        self.mathworld_link.pack(side=LEFT)
        self.mathworld_link.bind("<Button-1>", self.callback2)

        self.publication_link = Label(self.cf2, text="      Steven Wolfram's Publication", font="Sans=serif 14", fg="blue", cursor="hand2")
        self.publication_link.pack(side=LEFT)
        self.publication_link.bind("<Button-1>", self.callback3)

        self.NatureOfCode_link = Label(self.cf2, text="         The Nature of Code", font="Sans=serif 14", fg="blue", cursor="hand2")
        self.NatureOfCode_link.pack(side=LEFT)
        self.NatureOfCode_link.bind("<Button-1>", self.callback4)


    def callback(self, event):
        webbrowser.open_new("https://en.wikipedia.org/wiki/Elementary_cellular_automaton")
    def callback2(self, event):
        webbrowser.open_new("http://mathworld.wolfram.com/ElementaryCellularAutomaton.html")
    def callback3(self, event):
        webbrowser.open_new("http://www.stephenwolfram.com/publications/academic/cellular-automaton-properties.pdf")
    def callback4(self, event):
        webbrowser.open_new("http://natureofcode.com/book/chapter-7-cellular-automata/#chapter07_section2")


    def CA(self):
        self.gen = 0
        self.ruleset = [0, 0, 0, 0, 0, 0, 0, 0]
        self.cells = []

        self.cell_number = int(self.x_value / self.size)

        for i in range(self.cell_number):          #create empty cells
            self.cells.append(0)
        self.cells[int(self.cell_number/2)] = 1    #The middle cell is set to value of 1

        self.bin_rule =  bin(self.r_value)[2:]     #Change the rule from int to bin
        length = 8 - len(self.bin_rule)
        for i in range( len(self.bin_rule) ):
            self.ruleset[i+length] = self.bin_rule[i]

        self.loop()


    def loop(self):
        self.Plot()
        self.generate()


    def Plot(self):
        for i in range(len(self.cells)):
            if self.cells[i] == 1 or self.cells[i] == '1':  # Fill in the cells of the table that have a "1" in cells[]
                self.bot_right_x = self.top_left_x + self.size
                self.bot_right_y = self.top_left_y + self.size
                self.canvas.create_rectangle(self.top_left_x, self.top_left_y, self.bot_right_x, self.bot_right_y,
                                             fill="black", outline="white")
            else:
                self.bot_right_x = self.top_left_x + self.size  # This is in order to create an outline for the rest of the table
                self.bot_right_y = self.top_left_y + self.size
                self.canvas.create_rectangle(self.top_left_x, self.top_left_y, self.bot_right_x, self.bot_right_y,
                                             outline="black")
            self.top_left_x += self.size

        self.bot_right_y = 0  # reset
        self.bot_right_x = 0
        self.top_left_x = 0
        self.top_left_y += self.size


    def generate(self):
        self.nextgen = []

        for i in range(self.cell_number):
            self.nextgen.append(0)                 # Create the next gen of cells

        for i in range(1, self.cell_number - 1):
            self.left = self.cells[i - 1]
            self.center = self.cells[i]
            self.right = self.cells[i + 1]
            self.nextgen[i] = self.check(self.left, self.center, self.right)

        self.cells = list(self.nextgen)
        self.gen += 1

        if self.gen <= (self.generations - 1) :  #int((self.y_value / self.size)/1.5)
            self.loop()


    def check(self, a, b, c):
        self.abc = [a, b, c]
        self.fin = ''.join(map(str, self.abc))
        return self.ruleset[-1-int(self.fin, 2)]


#--------------------------------------------------------------------------------
root = Tk()
root.title("Control Panel")
root.resizable(False, False)        #makes the window NOT resizable
app = App(root)
root.mainloop()
