import pdb
class a:
   x=0 
   def set_x(self,i):
       x=i
   def set_y(self,i):
       self.x=(i)
   def get_x(self):
       return x
   def get_y(self):
       return self.x

if __name__ == '__main__':
        import pdb
        #str_filename="c:/stockdata/000001.ss.csv"
        #DrawHistogram(str_filename,1000)
        #str_filename="c:/stockdata/000100.sz.csv"
        #DrawHistogram(str_filename,1000)
        c=a()
        d=a()
        c.set_x(1)
        d.set_x(2)
        print c.get_x()
        c.set_y(1)
        d.set_y(2)
        print c.get_y()
        pdb.set_trace()
