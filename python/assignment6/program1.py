class Password_manager:
    def __init__(self,pas):
        self.list=[]
        self.list.append(pas)
        self.__password=self.list[len(self.list)-1]

    def get_password(self):
        print("current password is:",self.__password)

    def is_correct(self,check):
        if(check==self.__password):
            return True
        else: return False

    def set_password(self,a):
        if(a not in self.list):
            self.list.append(input("enter new password:"))
            self.__password=self.list[len(self.list)-1]
        
    
s=Password_manager("1275")
s.get_password()
print(s.is_correct("1275"))
s.set_password("65")
s.get_password()
