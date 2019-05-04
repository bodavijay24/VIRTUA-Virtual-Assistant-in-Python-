import wx
import wikipedia
import wolframalpha
from espeak import espeak as es

es.synth("Welcome")
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(650, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="VIRTUA")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello! I am VIRTUA,Python Digital Assistant.How Can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(500,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input1 = self.txt.GetValue()
        input1 = input1.lower()
        try:
            #wolframalpha
            app_id = "APP ID"
            client = wolframalpha.Client(app_id)
            res = client.query(input1)
            answer = next(res.results).text
            print (answer)
            es.synth("The answer is "+answer)
        except:
            #wikipedia
            input1=input1.split(' ')
            input1=" ".join(input1[2:])
            es.synth("Searched for "+input1)
            print (wikipedia.summary(input1))


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
