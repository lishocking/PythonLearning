import wx
import pdb
import numpy as np
from chess_rule import *
class MyChessButton(wx.BitmapButton):
     def __init__(self,parent, id=wx.ID_ANY,label="",pos=wx.DefaultPosition,
             size=wx.DefaultSize, 
             style=wx.BORDER_NONE,
             #style=wx.BORDER_NONE|wx.TRANSPARENT_WINDOW,
             validator=wx.DefaultValidator,
             name="MyChessButton",bitmap=wx.NullBitmap,bitmapSelect=wx.NullBitmap):
        wx.BitmapButton.__init__(self, parent, id,bitmap,pos, size, style, validator, name)
        self.oldpos=pos+(1,1)
        self.pos=pos
        self.bitmapNotSelect=bitmap
        self.bitmapSelect=bitmapSelect
        self.bitmapNotSelectTmp=wx.Bitmap()
        self.bitmapSelectTmp=wx.Bitmap()
        self.clicked=False
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.selectable=False

     def OnPaint(self,event):
        """ Handles the wx.EVT_PAINT event for MyChessButton. """
        dc = wx.BufferedPaintDC(self)
        self.Draw(dc)
     def Draw(self, dc):
        # Get the actual client size of ourselves
        width, height = self.GetClientSize()
        if not width or not height:
            # Nothing to do, we still don't have dimensions!
            return
        bitmapXpos = 0
        bitmapYpos = 0
        parent=self.GetParent()
        if self.oldpos != self.pos :
            bitmapWidth, bitmapHeight = self.bitmapSelect.GetWidth(), self.bitmapSelect.GetHeight()
            size=wx.Size(bitmapWidth,bitmapHeight)
            rect=wx.Rect(self.pos,size)

            pbitmap=parent.GetBitmap()
            pbitmap=pbitmap.GetSubBitmap(rect)

            parray=np.zeros(bitmapWidth*bitmapHeight*3,np.uint8)
            parray=parray.reshape(bitmapWidth*bitmapHeight,3)
            pbitmap.CopyToBuffer(parray)

            array=np.zeros(bitmapWidth*bitmapHeight*3,np.uint8)
            array=array.reshape(bitmapWidth*bitmapHeight,3)
            self.bitmapNotSelect.CopyToBuffer(array)
            narray=np.zeros(bitmapWidth*bitmapHeight*3,np.uint8)
            narray=narray.reshape(bitmapWidth*bitmapHeight,3)

            for i in range(0,bitmapWidth*bitmapHeight):
                if (array[i][0] == 255 and array[i][1]==255 and array[i][2]==255):
                    narray[i]=parray[i]
                else:
                    narray[i]=array[i]
            self.bitmapNotSelectTmp=wx.Bitmap.FromBuffer(bitmapWidth,bitmapHeight,narray)

            array=np.zeros(bitmapWidth*bitmapHeight*3,np.uint8)
            array=array.reshape(bitmapWidth*bitmapHeight,3)
            self.bitmapSelect.CopyToBuffer(array)
            narray=np.zeros(bitmapWidth*bitmapHeight*3,np.uint8)
            narray=narray.reshape(bitmapWidth*bitmapHeight,3)

            for i in range(0,bitmapWidth*bitmapHeight):
                if (array[i][0] == 255 and array[i][1]==255 and array[i][2]==255):
                    narray[i]=parray[i]
                else:
                    narray[i]=array[i]
            self.bitmapSelectTmp=wx.Bitmap.FromBuffer(bitmapWidth,bitmapHeight,narray)
            self.oldpos = self.pos
        if self.clicked == False:
            dc.DrawBitmap(self.bitmapNotSelectTmp, bitmapXpos, bitmapYpos, True)
        else:
            dc.DrawBitmap(self.bitmapSelectTmp, bitmapXpos, bitmapYpos, True)
        
     def OnEraseBackground(self, event):
        """ Handles the wx.EVT_ERASE_BACKGROUND eventb for CustomCheckBox. """

        # This is intentionally empty, because we are using the combination
        # of wx.BufferedPaintDC + an empty OnEraseBackground event to
        # reduce flicker
        pass
     def Select(self,stat):
         self.clicked=stat
         
     def MoveButton(self,pos):
         self.SetPosition(pos)
         self.pos=pos
class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,style=wx.TRANSPARENT_WINDOW)
        bitmap_chessboard=wx.Bitmap("./IMAGES_S/GREEN.GIF")

        self.board=ChessBoard()
        self.board.PutDefault()
        self.board.Print()

        self.chessboard_x=np.array(range(28-20,349-20,40))
        self.chessboard_y=np.array(range(27-20,417-20,40))
        self.chessboard_y=self.chessboard_y+np.array([0,0,0,0,0,1,1,1,1,1])
        self.turn=True

        self.bitmap_chessboard=wx.StaticBitmap(self,bitmap=bitmap_chessboard)
        #黑士
        self.ba=wx.Bitmap("./IMAGES_S/WOOD/BA.BMP")
        self.bas=wx.Bitmap("./IMAGES_S/WOOD/BAS.BMP")
        #黑象
        self.bb=wx.Bitmap("./IMAGES_S/WOOD/BB.BMP")
        self.bbs=wx.Bitmap("./IMAGES_S/WOOD/BBS.BMP")
        #黑炮
        self.bc=wx.Bitmap("./IMAGES_S/WOOD/BC.BMP")
        self.bcs=wx.Bitmap("./IMAGES_S/WOOD/BCS.BMP")
        #黑将
        self.bk=wx.Bitmap("./IMAGES_S/WOOD/BK.BMP")
        self.bks=wx.Bitmap("./IMAGES_S/WOOD/BKS.BMP")
        #黑马
        self.bn=wx.Bitmap("./IMAGES_S/WOOD/BN.BMP")
        self.bns=wx.Bitmap("./IMAGES_S/WOOD/BNS.BMP")
        #黑车
        self.br=wx.Bitmap("./IMAGES_S/WOOD/BR.BMP")
        self.brs=wx.Bitmap("./IMAGES_S/WOOD/BRS.BMP")
        #黑兵
        self.bp=wx.Bitmap("./IMAGES_S/WOOD/BP.BMP")
        self.bps=wx.Bitmap("./IMAGES_S/WOOD/BPS.BMP")
        #红士
        self.ra=wx.Bitmap("./IMAGES_S/WOOD/RA.BMP")
        self.ras=wx.Bitmap("./IMAGES_S/WOOD/RAS.BMP")
        #红相
        self.rb=wx.Bitmap("./IMAGES_S/WOOD/RB.BMP")
        self.rbs=wx.Bitmap("./IMAGES_S/WOOD/RBS.BMP")
        #红炮
        self.rc=wx.Bitmap("./IMAGES_S/WOOD/RC.BMP")
        self.rcs=wx.Bitmap("./IMAGES_S/WOOD/RCS.BMP")
        #红将
        self.rk=wx.Bitmap("./IMAGES_S/WOOD/RK.BMP")
        self.rks=wx.Bitmap("./IMAGES_S/WOOD/RKS.BMP")
        #红马
        self.rn=wx.Bitmap("./IMAGES_S/WOOD/RN.BMP")
        self.rns=wx.Bitmap("./IMAGES_S/WOOD/RNS.BMP")
        #红车
        self.rr=wx.Bitmap("./IMAGES_S/WOOD/RR.BMP")
        self.rrs=wx.Bitmap("./IMAGES_S/WOOD/RRS.BMP")
        #红兵
        self.rp=wx.Bitmap("./IMAGES_S/WOOD/RP.BMP")
        self.rps=wx.Bitmap("./IMAGES_S/WOOD/RPS.BMP")

        self.button_ba2=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.ba,bitmapSelect=self.bas,pos=(self.chessboard_x[3],self.chessboard_y[0]))
        self.button_ba1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.ba,bitmapSelect=self.bas,pos=(self.chessboard_x[5],self.chessboard_y[0]))

        self.button_bb2=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.bb,bitmapSelect=self.bbs,pos=(self.chessboard_x[2],self.chessboard_y[0]))
        self.button_bb1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.bb,bitmapSelect=self.bbs,pos=(self.chessboard_x[6],self.chessboard_y[0]))

        self.button_bc2=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.bc,bitmapSelect=self.bcs,pos=(self.chessboard_x[1],self.chessboard_y[2]))
        self.button_bc1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.bc,bitmapSelect=self.bcs,pos=(self.chessboard_x[7],self.chessboard_y[2]))

        self.button_bk1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.bk,bitmapSelect=self.bks,pos=(self.chessboard_x[4],self.chessboard_y[0]))

        self.button_bn1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.bn,bitmapSelect=self.bns,pos=(self.chessboard_x[1],self.chessboard_y[0]))
        self.button_bn2=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.bn,bitmapSelect=self.bns,pos=(self.chessboard_x[7],self.chessboard_y[0]))
        
        self.button_br1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.br,bitmapSelect=self.brs,pos=(self.chessboard_x[0],self.chessboard_y[0]))
        self.button_br2=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.br,bitmapSelect=self.brs,pos=(self.chessboard_x[8],self.chessboard_y[0]))
        
        self.button_bp1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.bp,bitmapSelect=self.bps,pos=(self.chessboard_x[0],self.chessboard_y[3]))
        self.button_bp2=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.bp,bitmapSelect=self.bps,pos=(self.chessboard_x[2],self.chessboard_y[3]))
        self.button_bp3=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.bp,bitmapSelect=self.bps,pos=(self.chessboard_x[4],self.chessboard_y[3]))
        self.button_bp4=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.bp,bitmapSelect=self.bps,pos=(self.chessboard_x[6],self.chessboard_y[3]))
        self.button_bp5=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.bp,bitmapSelect=self.bps,pos=(self.chessboard_x[8],self.chessboard_y[3]))

        self.buttonb=[self.button_ba1,self.button_ba2,
                      self.button_bb1,self.button_bb2,
                      self.button_bk1,
                      self.button_bn1,self.button_bn2,
                      self.button_br1,self.button_br2,
                      self.button_bc1,self.button_bc2,
                      self.button_bp1,self.button_bp2,self.button_bp3,self.button_bp4,self.button_bp5]


        self.button_ra2=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.ra,bitmapSelect=self.ras,pos=(self.chessboard_x[3],self.chessboard_y[9]))
        self.button_ra1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.ra,bitmapSelect=self.ras,pos=(self.chessboard_x[5],self.chessboard_y[9]))

        self.button_rb2=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rb,bitmapSelect=self.rbs,pos=(self.chessboard_x[2],self.chessboard_y[9]))
        self.button_rb1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rb,bitmapSelect=self.rbs,pos=(self.chessboard_x[6],self.chessboard_y[9]))

        self.button_rc2=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rc,bitmapSelect=self.rcs,pos=(self.chessboard_x[1],self.chessboard_y[7]))
        self.button_rc1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rc,bitmapSelect=self.rcs,pos=(self.chessboard_x[7],self.chessboard_y[7]))

        self.button_rk1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rk,bitmapSelect=self.rks,pos=(self.chessboard_x[4],self.chessboard_y[9]))

        self.button_rn1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rn,bitmapSelect=self.rns,pos=(self.chessboard_x[1],self.chessboard_y[9]))
        self.button_rn2=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rn,bitmapSelect=self.rns,pos=(self.chessboard_x[7],self.chessboard_y[9]))
        
        self.button_rr1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rr,bitmapSelect=self.rrs,pos=(self.chessboard_x[0],self.chessboard_y[9]))
        self.button_rr2=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rr,bitmapSelect=self.rrs,pos=(self.chessboard_x[8],self.chessboard_y[9]))
        
        self.button_rp1=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rp,bitmapSelect=self.rps,pos=(self.chessboard_x[0],self.chessboard_y[6]))
        self.button_rp2=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rp,bitmapSelect=self.rps,pos=(self.chessboard_x[2],self.chessboard_y[6]))
        self.button_rp3=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rp,bitmapSelect=self.rps,pos=(self.chessboard_x[4],self.chessboard_y[6]))
        self.button_rp4=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rp,bitmapSelect=self.rps,pos=(self.chessboard_x[6],self.chessboard_y[6]))
        self.button_rp5=MyChessButton(parent=self.bitmap_chessboard,bitmap=self.rp,bitmapSelect=self.rps,pos=(self.chessboard_x[8],self.chessboard_y[6]))

        self.buttonr=[self.button_ra1,self.button_ra2,
                      self.button_rb1,self.button_rb2,
                      self.button_rk1,
                      self.button_rn1,self.button_rn2,
                      self.button_rr1,self.button_rr2,
                      self.button_rc1,self.button_rc2,
                      self.button_rp1,self.button_rp2,self.button_rp3,self.button_rp4,self.button_rp5]
        self.bitmap_chessboard.Bind(wx.EVT_LEFT_UP,self.OnButtonClicked)
        self.OnTurn()

        for i in self.buttonb:
            i.Bind(wx.EVT_BUTTON,self.OnChessSelect)
        for i in self.buttonr:
            i.Bind(wx.EVT_BUTTON,self.OnChessSelect)
    def OnTurn(self):
        if self.turn:
            for i in range(0,len(self.buttonb)):
                self.buttonb[i].selectable=False
            for i in range(0,len(self.buttonr)):
                self.buttonr[i].selectable=True
        else:
            for i in range(0,len(self.buttonb)):
                self.buttonb[i].selectable=True
            for i in range(0,len(self.buttonr)):
                self.buttonr[i].selectable=False


        self.turn = not self.turn
    def OnButtonClicked(self,event):
        pos=event.GetPosition()
        x=pos.x
        y=pos.y
        x_index=int(round((x-28)/40))
        y_index=int(round((y-27)/40))
    
        x=self.chessboard_x[x_index]
        y=self.chessboard_y[y_index]

        selectedbutton=False
        for i in range(0,len(self.buttonb)):
            if(self.buttonb[i].clicked==True):
                selectedbutton=self.buttonb[i]
                
        for i in range(0,len(self.buttonr)):
            if(self.buttonr[i].clicked==True):
                selectedbutton=self.buttonr[i]
        if selectedbutton == False:
            return
        old_x_index=int(round((selectedbutton.oldpos[0]-8)/40))
        old_y_index=int(round((selectedbutton.oldpos[1]-8)/40))
       # print(old_x_index,old_y_index)
       # print(x_index,y_index)
        if self.board.Mov(Postion(old_x_index,old_y_index),Postion(x_index,y_index)):
                selectedbutton.MoveButton((x,y))
                self.OnTurn()
                selectedbutton.Select(False)
                selectedbutton.Refresh()
            

        return
    def OnChessSelect(self,event):
        if event.GetEventObject().selectable == True:
            for i in range(0,len(self.buttonb)):
                if(self.buttonb[i].clicked):
                    self.buttonb[i].Select(False)
                    self.buttonb[i].Refresh()
            for i in range(0,len(self.buttonr)):
                if(self.buttonr[i].clicked):
                    self.buttonr[i].Select(False)
                    self.buttonr[i].Refresh()
            event.GetEventObject().Select(True)
        else:
            removebutton=event.GetEventObject()
            pos=removebutton.pos
            x=pos[0]
            y=pos[1]
            x_index=int(round((x-8)/40))
            y_index=int(round((y-7)/40))
    
            x=self.chessboard_x[x_index]
            y=self.chessboard_y[y_index]

            selectedbutton=False
            for i in range(0,len(self.buttonb)):
                if(self.buttonb[i].clicked==True):
                    selectedbutton=self.buttonb[i]
                    
            for i in range(0,len(self.buttonr)):
                if(self.buttonr[i].clicked==True):
                    selectedbutton=self.buttonr[i]
            if selectedbutton == False:
                return
            old_x_index=int(round((selectedbutton.oldpos[0]-8)/40))
            old_y_index=int(round((selectedbutton.oldpos[1]-8)/40))
       #     print(old_x_index,old_y_index)
       #     print(x_index,y_index)
            if self.board.Mov(Postion(old_x_index,old_y_index),Postion(x_index,y_index)):
                    if removebutton in self.buttonb:
                        self.buttonb.remove(removebutton)
                    if removebutton in self.buttonr:
                        self.buttonr.remove(removebutton)
                    removebutton.Destroy()
                    selectedbutton.MoveButton((x,y))
                    self.OnTurn()
                    selectedbutton.Select(False)
                    selectedbutton.Refresh()
                    
            
    
    

app = wx.App(False)
frame = wx.Frame(None,-1,"Chess",size=(394,452),style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()
