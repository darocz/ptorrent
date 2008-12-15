import wx

class PTorrent(wx.Frame):
	def __init__(self):
		super(PTorrent, self).__init__(None, wx.ID_ANY, 'PTorrent v0.01', size=(600, 600))
		
		self.Centre()

if __name__ == '__main__':
	app = wx.App()
	frame = PTorrent()
	frame.Show(True)
	app.MainLoop()