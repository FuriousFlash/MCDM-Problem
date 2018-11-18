import wx
 
def onButton(event):
    print("Button pressed.")
 
def openfile(string):
	app = wx.App()
 
	frame = wx.Frame(None, -1, 'win.py')
	frame.SetDimensions(0,0,200,50)
 
	# Create open file dialog
	openFileDialog = wx.FileDialog(frame, string, "", "", 
    	                                  "CSV Files (*.csv)|*.csv", 
        	                               wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
 
	openFileDialog.ShowModal()
	print("")
	print("")
	print("Chosen", string, "location :", openFileDialog.GetPath())
	print("")
	print("")
	s = openFileDialog.GetPath()
	openFileDialog.Destroy()
	return s