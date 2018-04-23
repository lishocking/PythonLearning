import numpy
class ChessValue():
    def __init__(self):
        self.jiang_value=65535
        self.che1_value=1000
        self.che2_value=1000
        self.ma1_value=500
        self.ma2_value=500
        self.pa1_value=500
        self.pa2_value=500
        self.xiang1_value=200
        self.xiang2_value=200
        self.shi1_value=220
        self.shi2_value=220
        self.bing1_value=150
        self.bing2_value=150
        self.bing3_value=150
        self.bing4_value=150
        self.bing5_value=150


        self.anti_jiang_value=65535
        self.anti_che1_value=1000
        self.anti_che2_value=1000
        self.anti_ma1_value=500
        self.anti_ma2_value=500
        self.anti_pa1_value=500
        self.anti_pa2_value=500
        self.anti_xiang1_value=200
        self.anti_xiang2_value=200
        self.anti_shi1_value=220
        self.anti_shi2_value=220
        self.anti_bing1_value=150
        self.anti_bing2_value=150
        self.anti_bing3_value=150
        self.anti_bing4_value=150
        self.anti_bing5_value=150

        self.mychess=[
            self.jiang_value ,
            self.che1_value  ,
            self.che2_value  ,
            self.ma1_value   ,
            self.ma2_value   ,
            self.pa1_value   ,
            self.pa2_value   ,
            self.xiang1_value,
            self.xiang2_value,
            self.shi1_value  ,
            self.shi2_value  ,
            self.bing1_value ,
            self.bing2_value ,
            self.bing3_value ,
            self.bing4_value ,
            self.bing5_value 
            ]

        self.antichess=[
            self.anti_jiang_value ,
            self.anti_che1_value  ,
            self.anti_che2_value  ,
            self.anti_ma1_value   ,
            self.anti_ma2_value   ,
            self.anti_pa1_value   ,
            self.anti_pa2_value   ,
            self.anti_xiang1_value,
            self.anti_xiang2_value,
            self.anti_shi1_value  ,
            self.anti_shi2_value  ,
            self.anti_bing1_value ,
            self.anti_bing2_value ,
            self.anti_bing3_value ,
            self.anti_bing4_value ,
            self.anti_bing5_value 
            ]
    def value(self):
        value=sum(self.mychess)
        anti_value=sum(self.antichess)
        return [value,anti_value]



if __name__ == '__main__':
    a=ChessValue()
    b=a.value()
    print(b)
