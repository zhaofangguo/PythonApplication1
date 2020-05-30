class People():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_info(self):
        print(self.name+'is'+self.age)
class StudySta():
    def __init__(self,school="college"):
        self.school=school
    def print_study(self ):
        print(self.school)
    def set_school(self,school):
        self.school=school
class Male(People):
    def __init__(self,name,age,sex_def):
        super().__init__( name,age)
        self.sex_def=sex_def
        self.study=Study_sta()
    def print_info(self):
        super().print_info() 
        print(self.sex_def)