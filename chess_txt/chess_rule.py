#!python3.6
# -*- coding: utf-8 -*-
#         y-----------------------------------------------------------++
#         ^+----------------------------------------------------------++
#         ||                                                          ||
#         ||                                                          ||
#      0   0     +-----+-----+-----+-----+-----+-----+-----+-----+    ||
#         ||     |     |     |     | *   |   * |     |     |     |    ||
#         ||     |     |     |     |   * | *   |     |     |     |    ||
#      1   1     +-----+-----+-----+-----*-----+-----+-----+-----+    ||
#         ||     |     |     |     |   * | *   |     |     |     |    ||
#         ||     |     |     |     | *   |   * |     |     |     |    ||
#      2   2     +-----#-----+-----+-----+-----+-----+-----#-----+    ||
#         ||     |     |     |     |     |     |     |     |     |    ||
#         ||     |     |     |     |     |     |     |     |     |    ||
#      3   3     #-----+-----#-----+-----#-----+-----#-----+-----#    ||
#         ||     |     |     |     |     |     |     |     |     |    ||
#         ||     |     |     |     |     |     |     |     |     |    ||
#      4   4     +-----+-----+-----+-----+-----+-----+-----+-----+    ||
#         ||     |                                               |    ||
#         ||     |                                               |    ||
#      5   5     +-----+-----+-----+-----+-----+-----+-----+-----+    ||
#         ||     |     |     |     |     |     |     |     |     |    ||
#         ||     |     |     |     |     |     |     |     |     |    ||
#      6   6     #-----+-----#-----+-----#-----+-----#-----+-----#    ||
#         ||     |     |     |     |     |     |     |     |     |    ||
#         ||     |     |     |     |     |     |     |     |     |    ||
#      7   7     +-----#-----+-----+-----+-----+-----+-----#-----+    ||
#         ||     |     |     |     | *   |   * |     |     |     |    ||
#         ||     |     |     |     |   * | *   |     |     |     |    ||
#      8   8     +-----+-----+-----+-----+-----+-----+-----+-----+    ||
#         ||     |     |     |     |   * | *   |     |     |     |    ||
#         ||     |     |     |     | *   |   * |     |     |     |    ++
#      9  |9     0-----1-----2-----3-----4-----5-----6-----7-----8----++
#         +------0-----------------------------------------------8----->x
import numpy as np
import pdb
class Postion:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class ChessBoard:
    chessboard=np.zeros((9,10),np.uint8)
    #定义棋子ID

    ID_red_che1  =  10
    ID_red_che2  =  11
    ID_red_ma1   =  20
    ID_red_ma2   =  21
    ID_red_pao1  =  30
    ID_red_pao2  =  31
    ID_red_xiang1=  40
    ID_red_xiang2=  41
    ID_red_shi1  =  50
    ID_red_shi2  =  51
    ID_red_bing1 =  60
    ID_red_bing2 =  61
    ID_red_bing3 =  62
    ID_red_bing4 =  63
    ID_red_bing5 =  64
    ID_red_jiang =  70

    ID_blue_che1  =  10+100 
    ID_blue_che2  =  11+100
    ID_blue_ma1   =  20+100
    ID_blue_ma2   =  21+100
    ID_blue_pao1  =  30+100
    ID_blue_pao2  =  31+100
    ID_blue_xiang1=  40+100
    ID_blue_xiang2=  41+100
    ID_blue_shi1  =  50+100
    ID_blue_shi2  =  51+100
    ID_blue_bing1 =  60+100
    ID_blue_bing2 =  61+100
    ID_blue_bing3 =  62+100
    ID_blue_bing4 =  63+100
    ID_blue_bing5 =  64+100
    ID_blue_jiang =  70+100
    def __init__(self):
        self.ID_red_jiang =  70
        self.ID_blue_jiang =  70+100
        self.NULL=0
        self.RED=1
        self.BLUE=2

        self.CHE=1
        self.MA=2
        self.PAO=3
        self.XIANG=4
        self.SHI=5
        self.BING=6
        self.JIANG=7

    def Print(self):
        print (np.transpose(self.chessboard))
    def PutDefault(self):
        self.chessboard[0][0]=self.ID_red_che1
        self.chessboard[1][0]=self.ID_red_ma1
        self.chessboard[2][0]=self.ID_red_xiang1
        self.chessboard[3][0]=self.ID_red_shi1
        self.chessboard[4][0]=self.ID_red_jiang
        self.chessboard[5][0]=self.ID_red_shi2
        self.chessboard[6][0]=self.ID_red_xiang2
        self.chessboard[7][0]=self.ID_red_ma2
        self.chessboard[8][0]=self.ID_red_che2
                          
        self.chessboard[0][3]=self.ID_red_bing1
        self.chessboard[2][3]=self.ID_red_bing2
        self.chessboard[4][3]=self.ID_red_bing3
        self.chessboard[6][3]=self.ID_red_bing4
        self.chessboard[8][3]=self.ID_red_bing5
                          
        self.chessboard[1][2]=self.ID_red_pao1
        self.chessboard[7][2]=self.ID_red_pao2

        self.chessboard[0][9-0]=self.ID_blue_che1
        self.chessboard[1][9-0]=self.ID_blue_ma1
        self.chessboard[2][9-0]=self.ID_blue_xiang1
        self.chessboard[3][9-0]=self.ID_blue_shi1
        self.chessboard[4][9-0]=self.ID_blue_jiang
        self.chessboard[5][9-0]=self.ID_blue_shi2
        self.chessboard[6][9-0]=self.ID_blue_xiang2
        self.chessboard[7][9-0]=self.ID_blue_ma2
        self.chessboard[8][9-0]=self.ID_blue_che2
                          
        self.chessboard[0][9-3]=self.ID_blue_bing1
        self.chessboard[2][9-3]=self.ID_blue_bing2
        self.chessboard[4][9-3]=self.ID_blue_bing3
        self.chessboard[6][9-3]=self.ID_blue_bing4
        self.chessboard[8][9-3]=self.ID_blue_bing5
                          
        self.chessboard[1][9-2]=self.ID_blue_pao1
        self.chessboard[7][9-2]=self.ID_blue_pao2
        return 
    def GetColor(self,id):
        if id == 0:
            return self.NULL
        elif int(id/100) == 0:
            return self.RED
        else:
            return self.BLUE
    def Rule_Jiang(self,oldpos,pos):
        if(pos.x<3 or pos.x >5 ):
            return False
        if(oldpos.y<4):
            if(pos.y>3 ):
                return False
        else:
            if(pos.y<7 ):
                return False
        if(self.GetColor(self.chessboard[oldpos.x][oldpos.y]) ==
            self.GetColor(self.chessboard[pos.x][pos.y]) ):
            return False
        if abs(pos.x-oldpos.x)+abs(pos.y-oldpos.y)!=1:
            return False
            
        return True
    def Rule_Che(self,oldpos,pos):
        if (pos.x-oldpos.x)*(pos.y-oldpos.y) != 0 :
            return False
        if(self.GetColor(self.chessboard[oldpos.x][oldpos.y]) ==
            self.GetColor(self.chessboard[pos.x][pos.y]) ):
            return False
        if (pos.x-oldpos.x) == 0:
            if abs(pos.y-oldpos.y)>1: 
                for i in range (min(oldpos.y,pos.y)+1,
                                    max(oldpos.y,pos.y)):
                    if(self.chessboard[pos.x][i] !=0 ):
                        return False
        else :
            if abs(pos.x-oldpos.x)>1: 
                for i in range (min(oldpos.x,pos.x)+1,
                                    max(oldpos.x,pos.x)):
                    if(self.chessboard[i][pos.y] !=0 ):
                        return False
        return True

    def Rule_Pao(self,oldpos,pos):
        if (pos.x-oldpos.x)*(pos.y-oldpos.y) != 0 :
            return False
        if(self.GetColor(self.chessboard[oldpos.x][oldpos.y]) ==
            self.GetColor(self.chessboard[pos.x][pos.y]) ):
            return False
        if (pos.x-oldpos.x) == 0:
            if abs(pos.y-oldpos.y) == 1:
                if(self.chessboard[pos.x][pos.y]!=0):
                    return False
            else:
                count=0
                for i in range (min(oldpos.y,pos.y)+1,
                                    max(oldpos.y,pos.y)):
                    if(self.chessboard[pos.x][i] !=0 ):
                        count+=1
                if count > 1:
                    return False
                if self.GetColor(self.chessboard[pos.x][pos.y]) == self.NULL:
                    if count == 1:
                        return False
        else:
            if abs(pos.x-oldpos.x) == 1:
                if(self.chessboard[pos.x][pos.y]!=0):
                    return False
            else:
                count=0
                for i in range (min(oldpos.x,pos.x)+1,
                                    max(oldpos.x,pos.x)):
                    if(self.chessboard[i][pos.y] !=0 ):
                        count+=1
                if count > 1:
                    return False
                if self.GetColor(self.chessboard[pos.x][pos.y]) == self.NULL:
                    if count == 1:
                        return False

        return True
    def Rule_Ma(self,oldpos,pos):
        if abs(pos.x-oldpos.x)*abs(pos.y-oldpos.y) != 2 :
            return False
        if(self.GetColor(self.chessboard[oldpos.x][oldpos.y]) ==
            self.GetColor(self.chessboard[pos.x][pos.y]) ):
            return False
        if abs(pos.x-oldpos.x) == 1:
            if(self.chessboard[oldpos.x][int((pos.y+oldpos.y)/2)]!=0):
                return False
        else:
            if(self.chessboard[int((pos.x+oldpos.x)/2)][oldpos.y]!=0):
                return False
        return True

    def Rule_Xiang(self,oldpos,pos):
        if abs(pos.x-oldpos.x)!=2:
            return False
        if abs(pos.y-oldpos.y)!=2:
            return False
        if(self.GetColor(self.chessboard[oldpos.x][oldpos.y]) ==
            self.GetColor(self.chessboard[pos.x][pos.y]) ):
            return False
        if (self.chessboard[int((pos.x+oldpos.x)/2)][int((pos.y+oldpos.y)/2)]!=0):
            return False
        if (pos.y-4.5)*(oldpos.y-4.5)<0:
            return False
        return True

    def Rule_Shi(self,oldpos,pos):
        if abs(pos.x-oldpos.x)!=1:
            return False
        if abs(pos.y-oldpos.y)!=1:
            return False
        if(self.GetColor(self.chessboard[oldpos.x][oldpos.y]) ==
            self.GetColor(self.chessboard[pos.x][pos.y]) ):
            return False
        if (pos.x > 5) or (pos.x<3):
            return False
        if (pos.y > 2) and (pos.y<7):
            return False
        return True

    def Rule_Bing(self,oldpos,pos):
        if abs(pos.x-oldpos.x)+abs(pos.y-oldpos.y) != 1 :
            return False
        if(self.GetColor(self.chessboard[oldpos.x][oldpos.y]) ==
            self.GetColor(self.chessboard[pos.x][pos.y]) ):
            return False
        for x in range(3,5):
            for y in range(0,2):
                if self.chessboard[x][y] == self.ID_blue_jiang:
                    if(self.GetColor(self.chessboard[oldpos.x][oldpos.y])==self.BLUE):
                        sourceposJiang=Postion(4,0)
                    else:
                        sourceposJiang=Postion(4,9)
                if self.chessboard[x][y] == self.ID_red_jiang:
                    if(self.GetColor(self.chessboard[oldpos.x][oldpos.y])==self.RED):
                        sourceposJiang=Postion(4,0)
                    else:
                        sourceposJiang=Postion(4,9)
        if abs(oldpos.y-sourceposJiang.y) > abs(pos.y-sourceposJiang.y):
            return False
        if abs(oldpos.y-sourceposJiang.y)<5:
            if abs(pos.y-oldpos.y) !=1:
                return False
        return True


    def CheckRule(self,oldpos,pos):
            id=self.chessboard[oldpos.x][oldpos.y]
            role=int((id%100)/10)
            if role == self.CHE:
                return self.Rule_Che(oldpos,pos)
            elif role == self.MA:
                return self.Rule_Ma(oldpos,pos)
            elif role == self.PAO:
                return self.Rule_Pao(oldpos,pos)
            elif role == self.XIANG:
                return self.Rule_Xiang(oldpos,pos)
            elif role == self.SHI:
                return self.Rule_Shi(oldpos,pos)
            elif role == self.BING:
                return self.Rule_Bing(oldpos,pos)
            elif role == self.JIANG:
                return self.Rule_Jiang(oldpos,pos)
            return False
    def Mov(self,oldpos,pos):
        if self.CheckRule(oldpos,pos):
            self.chessboard[pos.x][pos.y]=self.chessboard[oldpos.x][oldpos.y]
            self.chessboard[oldpos.x][oldpos.y]=0
            self.Print()
            return True
        else:
            print("check fail")
            return False



if __name__ == '__main__':
    import pdb
    board=ChessBoard()
    board.PutDefault()
    board.Print()
    board.Mov(Postion(0,9),Postion(0,8))
    board.Print()
    
    


