import class1
#zhaofangguo=people('zhaofangguo',18)
#zhaofangguo.print_name()
#zhaofangguo.print_age()

class_name=input("名字:")
class_age=input("age:")
class_sex_def=input("sex:")
zhaofangguo=male(class_name,class_age,class_sex_def)
zhaofangguo.print_info()
zhaofangguo.study.print_study()
zhaofangguo.study.set_school("primera")
zhaofangguo.study.print_study()