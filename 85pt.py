#########################################
#
#         85pt - Boundary detection
#
#########################################

# Add a button to move to the right and make them work as you'd expect (repeating lab12)
# This time - make sure that pressing left or right does nothing if you are going
# to hit a "boundary" - i.e. the edge of the screen.

from Tkinter import *
root = Tk()
drawpadwidth = 480
drawpadheight = 320
drawpad = Canvas(root, width=drawpadwidth, height=drawpadheight, background='white')
x1 = 160
x2 = 160
y1 = 320
y2 = 320
oval = drawpad.create_oval(x1,x2,y1,y2, fill="red")
class MyApp:
	def __init__(self, parent):
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Left", background= "green")
		self.button1.grid(row=0,column=0)												
		self.button1.bind("<Button-1>", self.button1Click)
		
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Right", background= "yellow")
		self.button2.grid(row=0,column=1)												
		self.button2.bind("<Button-1>", self.button2Click)
		 
		drawpad.pack()
			
	def button1Click(self, event):   
		global oval
		global drawpad
		global drawpadwidth
		global drawpadheight
	        drawpad.move(oval,-50,0)
	        #if :
	           #drawpad.move(oval,0,0)    
	
	def button2Click(self, event):   
		global oval
		global drawpad
		global drawpadwidth
		global drawpadheight
		drawpad.move(oval,50,0)	
		#if :
	           #drawpad.move(oval,0,0)
	       
myapp = MyApp(root)

root.mainloop()