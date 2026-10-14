class TaiKhoan:
    def __init__(self,ten_dang_nhap,mat_khau,ho_ten,email,vai_tro ="user"):
        self.__ten_dang_nhap = ten_dang_nhap
        self.__mat_khau = mat_khau
        self.__ho_ten = ho_ten
        self.__email = email
        self.__vai_tro = vai_tro
        
    @property
    def ten_dang_nhap(self):
        return self.__ten_dang_nhap
    @ten_dang_nhap.setter
    def ten_dang_nhap(self,value):
        self.__ten_dang_nhap = value
        
    @property
    def mat_khau(self):
        return self.__mat_khau
    @mat_khau.setter
    def mat_khau(self,value):
        self.__mat_khau = value
    
    @property
    def ho_ten(self):
        return self.__ho_ten
    @ho_ten.setter
    def ho_ten(self,value):
       self.__ho_ten = value
       
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,value):
        self.__email = value
    
    @property
    def vai_tro(self):
        return self.__vai_tro
    @vai_tro.setter
    def vai_tro(self,value):
        self.__vai_tro = value
        
    def chuyen_thanh_dict(self):
        return {
            "ten_dang_nhap": self.__ten_dang_nhap,
            "mat_khau": self.__mat_khau,
            "ho_ten": self.__ho_ten,
            "email": self.__email,
            "vai_tro": self.__vai_tro
            }
