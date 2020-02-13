import tkinter as tk           
from tkinter import font  as tkfont
from tkinter import messagebox
import backend
import re
from tkinter.filedialog import askdirectory
import photo_from_folder as pff
import identify_face_image as ifi
import identify_face_video as ifv
import photo_from_webcam as pfw
import train_main as tm
        
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        
        container = tk.Frame(self)        
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    Id = []
    def view_command(self):
       self.list1.delete(0,tk.END)
       for row in backend.View():
           self.list1.insert(tk.END,row)
    
    def View_command(self):
       self.list1.delete(0,tk.END)
       final_list = [] 
       for num in self.Id: 
           if num not in final_list: 
               final_list.append(num)
       if len(final_list) == 0:
           self.list1.insert(tk.END,"No Face Found")
       else:
           for i in final_list:
               row = backend.Search(int(i))
               self.list1.insert(tk.END,row)            
                

    def train_model(self):
        self.list1.delete(0,tk.END)
        temp = tm.train_model()           
        if temp == 0:
            self.list1.insert(tk.END,"No Face Found")
        
    def identify_image(self):
        folder = tk.filedialog.askopenfilename()
        self.Id = ifi.Image_Recognition(folder)        
        
    def identify_video(self):
        self.Id = ifv.Video_Recognition()
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        controller.title("Face Recognition System")
        message = tk.Label(self, text="Face Recognition System", bg = "black", fg= "white",font=controller.title_font)
        message.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Take Picture",command=lambda: controller.show_frame("PageOne") )
        button1.pack(pady = 10)
        
        button2 = tk.Button(self, text="Train Model" , command = lambda: self.train_model())
        button2.pack(pady = 10)
        
        button3 = tk.Button(self, text="Face Recognize Using Photo", command = lambda : self.identify_image())
        button3.pack(pady = 10)    
        
        button4 = tk.Button(self, text="Face Recognize Using Video", command = lambda : self.identify_video())
        button4.pack(pady = 10)
        
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack( side = tk.RIGHT, fill = tk.Y )
        
        self.list1 = tk.Listbox(self, yscrollcommand = scrollbar.set)
        self.list1.yview()
        self.list1.pack(pady = 10)
        self.list1.configure(height = 10,  width = 50)
        scrollbar.config( command = self.list1.yview )
        
        button5 = tk.Button(self, text="View All Data", command = lambda : self.View_command())
        button5.pack(pady = 10)
    
    
class PageOne(tk.Frame):
    
    def insert_command(self):
        if re.match(r'[a-zA-Z\s]+$',self.e1.get()) == None:
            messagebox.showerror("Error", "Entered Name is Wrong")
            self.e1.delete(0, 'end')
            
        elif re.match(r'(\d{2})[/.-](\d{2})[/.-](\d{4})$',self.e2.get()) == None:
            messagebox.showerror("Error", "Entered DOB is Wrong")
            self.e2.delete(0, 'end')
            
        elif re.match(r'^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$', self.e3.get()) == None:
            messagebox.showerror("Error", "Entered Email is Wrong")
            self.e3.delete(0, 'end')
            
        elif (re.match(r'[789]\d{9}$',self.e4.get()) == None):
            messagebox.showerror("Error", "Entered Phone Number is Wrong")
            self.e4.delete(0, 'end')
            
        else :
            msg = messagebox.askyesno("python","Are you sure to save the data?")    
            if msg == True:
                backend.Insert(self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get())
                self.e1.delete(0, 'end')
                self.e2.delete(0, 'end')
                self.e3.delete(0, 'end')
                self.e4.delete(0, 'end')
                self.controller.show_frame("PageTwo")

    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Insert Data", bg = "black", fg= "white", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        name = tk.Label(self, text='Name : ')
        name.pack(pady = 10)
        self.e1 = tk.Entry(self)
        self.e1.pack()

        DOB = tk.Label(self, text='DOB (DD-MM-YYYY) : ')
        DOB.pack(pady = 10)
        self.e2 = tk.Entry(self)
        self.e2.pack()

        email = tk.Label(self,text='Email : ')
        email.pack(pady = 10)
        self.e3 =tk.Entry(self)
        self.e3.pack()

        phone = tk.Label(self,text='Phone : ')
        phone.pack(pady = 10)
        self.e4 = tk.Entry(self)
        self.e4.pack()
        
        button1 = tk.Button(self, text="Submit", command= lambda :  self.insert_command())
        button1.pack(pady = 10)

#        back1 = tk.Button(self, text="Go next", command=lambda: self.controller.show_frame("PageTwo"))
#        back1.pack(pady = 10)
#        
        back = tk.Button(self, text="Go Back", command=lambda: controller.show_frame("StartPage"))
        back.pack(pady = 10)
        

class PageTwo(tk.Frame):
    F_name = 0
    
    def view_last_record(self):
       self.list1.delete(0,tk.END)
       rows = backend.Last_Record()
       self.F_name = rows[0][0]
#       print(type(self.F_name))
       for row in rows:
           self.list1.insert(tk.END,row)

           
    def Select_folder(self):
        folder = askdirectory()
        pff.Preprocess_by_photo(folder, self.F_name)
    
    def Clear_list(self):
        self.list1.delete(0,tk.END)
        self.controller.show_frame("StartPage")
        
    def Open_webcam(self):
        webcam = pfw.Photo_webcam()
        webcam.run()
        pff.Preprocess_by_photo('./unknownfaces', self.F_name)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text="Insert Image",bg = "black", fg= "white", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        self.list1 = tk.Listbox(self)
        self.list1.pack(pady = 10)
        self.list1.configure(height = 10,  width = 50)
        
        but1 = tk.Button(self, text="Get Details" ,  command = lambda :self.view_last_record())
        but1.pack(pady = 10) 
#        go to page photo_from_folder.py
        button1 = tk.Button(self, text="Upload Image (max 10)" , command = lambda : self.Select_folder())
        button1.pack(pady = 10)
        
        label = tk.Label(self, text="Or", font=controller.title_font)
        label.pack()
#        go to image photo_from_webcam.py
        button2 = tk.Button(self, text="Take Photos using webcam", command = lambda : self.Open_webcam())
        button2.pack(pady = 10)

        back = tk.Button(self, text="Done", command=lambda: self.Clear_list())
        back.pack(pady = 10)
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()