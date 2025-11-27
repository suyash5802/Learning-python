class Students:
    def __init__(self,name,roll_no,marks):
        self.__name=name
        self.__rollno=roll_no
        self.__marks=marks
    
    def get_name(self):
        print(self.__name)
    def set_marks(self,marks):
        self.__marks=marks
        print(self.__marks)

q=Students("Suyash",23,34)

q.get_name()
q.set_marks(100)
