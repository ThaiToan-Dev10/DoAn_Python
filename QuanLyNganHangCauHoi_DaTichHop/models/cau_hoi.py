class CauHoi:
    def __init__(
        self,
        ma_cau_hoi,
        mon_hoc,
        chu_de,
        muc_do,
        noi_dung,
        phuong_an_a,
        phuong_an_b,
        phuong_an_c,
        phuong_an_d,
        dap_an_dung,
        nguon_cau_hoi
    ):
        self.__ma_cau_hoi = ma_cau_hoi
        self.__mon_hoc = mon_hoc
        self.__chu_de = chu_de
        self.__muc_do = muc_do
        self.__noi_dung = noi_dung
        self.__phuong_an_a = phuong_an_a
        self.__phuong_an_b = phuong_an_b
        self.__phuong_an_c = phuong_an_c
        self.__phuong_an_d = phuong_an_d
        self.__dap_an_dung = dap_an_dung
        self.__nguon_cau_hoi = nguon_cau_hoi

    @property
    def ma_cau_hoi(self):
        return self.__ma_cau_hoi

    @ma_cau_hoi.setter
    def ma_cau_hoi(self, value):
        self.__ma_cau_hoi = value

    @property
    def mon_hoc(self):
        return self.__mon_hoc

    @mon_hoc.setter
    def mon_hoc(self, value):
        self.__mon_hoc = value

    @property
    def chu_de(self):
        return self.__chu_de

    @chu_de.setter
    def chu_de(self, value):
        self.__chu_de = value

    @property
    def muc_do(self):
        return self.__muc_do

    @muc_do.setter
    def muc_do(self, value):
        self.__muc_do = value

    @property
    def noi_dung(self):
        return self.__noi_dung

    @noi_dung.setter
    def noi_dung(self, value):
        self.__noi_dung = value

    @property
    def phuong_an_a(self):
        return self.__phuong_an_a

    @phuong_an_a.setter
    def phuong_an_a(self, value):
        self.__phuong_an_a = value

    @property
    def phuong_an_b(self):
        return self.__phuong_an_b

    @phuong_an_b.setter
    def phuong_an_b(self, value):
        self.__phuong_an_b = value

    @property
    def phuong_an_c(self):
        return self.__phuong_an_c

    @phuong_an_c.setter
    def phuong_an_c(self, value):
        self.__phuong_an_c = value

    @property
    def phuong_an_d(self):
        return self.__phuong_an_d

    @phuong_an_d.setter
    def phuong_an_d(self, value):
        self.__phuong_an_d = value

    @property
    def dap_an_dung(self):
        return self.__dap_an_dung

    @dap_an_dung.setter
    def dap_an_dung(self, value):
        self.__dap_an_dung = value

    @property
    def nguon_cau_hoi(self):
        return self.__nguon_cau_hoi

    @nguon_cau_hoi.setter
    def nguon_cau_hoi(self, value):
        self.__nguon_cau_hoi = value

    def chuyen_thanh_dict(self):
        return {
            "ma_cau_hoi": self.__ma_cau_hoi,
            "mon_hoc": self.__mon_hoc,
            "chu_de": self.__chu_de,
            "muc_do": self.__muc_do,
            "noi_dung": self.__noi_dung,
            "phuong_an_a": self.__phuong_an_a,
            "phuong_an_b": self.__phuong_an_b,
            "phuong_an_c": self.__phuong_an_c,
            "phuong_an_d": self.__phuong_an_d,
            "dap_an_dung": self.__dap_an_dung,
            "nguon_cau_hoi": self.__nguon_cau_hoi
        }


class CauHoiTracNghiem(CauHoi):
    @classmethod
    def tao_tu_dict(cls, du_lieu):
        return cls(
            du_lieu.get("ma_cau_hoi", ""),
            du_lieu.get("mon_hoc", ""),
            du_lieu.get("chu_de", ""),
            du_lieu.get("muc_do", ""),
            du_lieu.get("noi_dung", ""),
            du_lieu.get("phuong_an_a", ""),
            du_lieu.get("phuong_an_b", ""),
            du_lieu.get("phuong_an_c", ""),
            du_lieu.get("phuong_an_d", ""),
            du_lieu.get("dap_an_dung", ""),
            du_lieu.get("nguon_cau_hoi", "")
        )
