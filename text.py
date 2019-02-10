#!/usr/bin/python
# -*- encoding: UTF-8 -*-

from tkinter import *

class Cell(Entry): 
	def __init__(self, parent):
		self.value = StringVar()
		Entry.__init__(self, parent, textvariable = self.value)

class Table(Frame):
	def __init__(self, parent, columns = 4, rows = 10):
		Frame.__init__(self, parent)
		self.cells = [[Cell(self) for i in range(columns)] for j in range(rows)]
		[self.cells[i][j].grid(row = i, column = j) for i in range(rows) for j in range(columns)]

if __name__ == '__main__':
	root = Tk()
	tab = Table(root)
	tab.pack()
	tab.cells[1][1].value.set('test')
	tab.cells[2][2].value.set( tab.cells[1][1].value.get() )
	
	root.mainloop()