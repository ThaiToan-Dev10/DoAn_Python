class KetQua:
    def __init__(
        self,
        ma_ket_qua,
        ten_dang_nhap,
        ma_de_thi,
        so_cau_dung,
        tong_so_cau,
        diem,
        cau_tra_loi,
        thoi_gian_nop_bai
    ):
        self.__ma_ket_qua = ma_ket_qua
        self.__ten_dang_nhap = ten_dang_nhap
        self.__ma_de_thi = ma_de_thi
        self.__so_cau_dung = so_cau_dung
        self.__tong_so_cau = tong_so_cau
        self.__diem = diem

        if isinstance(cau_tra_loi, dict):
            self.__cau_tra_loi = cau_tra_loi.copy()
        else:
            self.__cau_tra_loi = {}

        self.__thoi_gian_nop_bai = (
            thoi_gian_nop_bai
        )

    @property
    def ma_ket_qua(self):
        return self.__ma_ket_qua

    @ma_ket_qua.setter
    def ma_ket_qua(self, value):
        self.__ma_ket_qua = value

    @property
    def ten_dang_nhap(self):
        return self.__ten_dang_nhap

    @ten_dang_nhap.setter
    def ten_dang_nhap(self, value):
        self.__ten_dang_nhap = value

    @property
    def ma_de_thi(self):
        return self.__ma_de_thi

    @ma_de_thi.setter
    def ma_de_thi(self, value):
        self.__ma_de_thi = value

    @property
    def so_cau_dung(self):
        return self.__so_cau_dung

    @so_cau_dung.setter
    def so_cau_dung(self, value):
        self.__so_cau_dung = value

    @property
    def tong_so_cau(self):
        return self.__tong_so_cau

    @tong_so_cau.setter
    def tong_so_cau(self, value):
        self.__tong_so_cau = value

    @property
    def diem(self):
        return self.__diem

    @diem.setter
    def diem(self, value):
        self.__diem = value

    @property
    def cau_tra_loi(self):
        return self.__cau_tra_loi.copy()

    @cau_tra_loi.setter
    def cau_tra_loi(self, value):
        if isinstance(value, dict):
            self.__cau_tra_loi = value.copy()
        else:
            self.__cau_tra_loi = {}

    @property
    def thoi_gian_nop_bai(self):
        return self.__thoi_gian_nop_bai

    @thoi_gian_nop_bai.setter
    def thoi_gian_nop_bai(self, value):
        self.__thoi_gian_nop_bai = value

    @property
    def xep_loai(self):
        if self.__diem >= 8:
            return "Giỏi"

        if self.__diem >= 6.5:
            return "Khá"

        if self.__diem >= 5:
            return "Đạt"

        return "Chưa đạt"

    def chuyen_thanh_dict(self):
        return {
            "ma_ket_qua": self.__ma_ket_qua,
            "ten_dang_nhap": self.__ten_dang_nhap,
            "ma_de_thi": self.__ma_de_thi,
            "so_cau_dung": self.__so_cau_dung,
            "tong_so_cau": self.__tong_so_cau,
            "diem": self.__diem,
            "cau_tra_loi": self.__cau_tra_loi.copy(),
            "thoi_gian_nop_bai": (
                self.__thoi_gian_nop_bai
            )
        }

    @classmethod
    def tao_tu_dict(cls, du_lieu):
        return cls(
            du_lieu.get("ma_ket_qua", ""),
            du_lieu.get("ten_dang_nhap", ""),
            du_lieu.get("ma_de_thi", ""),
            du_lieu.get("so_cau_dung", 0),
            du_lieu.get("tong_so_cau", 0),
            du_lieu.get("diem", 0),
            du_lieu.get("cau_tra_loi", {}),
            du_lieu.get(
                "thoi_gian_nop_bai",
                ""
            )
        )