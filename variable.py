class student:
      college_name="NSAK college of Engineering and Technology"# this is a static variable
      def __init__(self,name,roll_no):
         self.name=name   #this is a instance variable when ever we are using reference variable that is nothing but instance variable
         self.roll_no=roll_no
      def view(self):
         print("the name of the student is ",self.name)
         print("the roll number of the student is ",self.roll_no)
       @classmethod
       def view_clas():
        """this is class variable accessing in object method when ever we wnts to use then we have to use  @classmethod delimeter"""
          print("the name of college is: ",self.college_name)
       @staticmethod
       def avgmarks(H,T,E,M,s,so):
          """this is a static method it is not concerned with class or object method with  @staticmethod delimeter we can create
          in this self method we wont use if you wont want to declare delimeter then you can access with class name
           print((H+T+E+M+s+so)/6)
           
s=student()
s.view()
s.view_clas()
s.avgmarks(40,50,60,80,90,50)
