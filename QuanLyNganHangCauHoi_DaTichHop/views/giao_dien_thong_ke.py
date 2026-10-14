import tkinter as tk


class GiaoDienThongKe:
    def __init__(
        self,
        cua_so,
        quan_ly_thong_ke,
        ham_quay_lai
    ):
        self.__cua_so_cha = cua_so
        self.__quan_ly_thong_ke = quan_ly_thong_ke
        self.__ham_quay_lai = ham_quay_lai

        self.__tao_giao_dien()

    def __tao_giao_dien(self):
        self.__cua_so_thong_ke = tk.Toplevel(
            self.__cua_so_cha
        )

        self.__cua_so_thong_ke.title(
            "Thống kê tổng quan"
        )

        self.__cua_so_thong_ke.geometry(
            "650x450"
        )

        self.__cua_so_thong_ke.resizable(
            False,
            False
        )

        self.__cua_so_thong_ke.protocol(
            "WM_DELETE_WINDOW",
            self.__dong_cua_so
        )

        tieu_de = tk.Label(
            self.__cua_so_thong_ke,
            text="THỐNG KÊ TỔNG QUAN",
            font=("Arial", 20, "bold"),
            fg="blue"
        )

        tieu_de.pack(pady=20)

        thong_ke = (
            self.__quan_ly_thong_ke
            .lay_thong_ke_tong_quan()
        )

        khung_cac_o = tk.Frame(
            self.__cua_so_thong_ke
        )

        khung_cac_o.pack(pady=10)

        self.__tao_o_thong_ke(
            khung_cac_o,
            "Tài khoản",
            thong_ke["so_tai_khoan"],
            0,
            0,
            "#1976D2"
        )

        self.__tao_o_thong_ke(
            khung_cac_o,
            "Câu hỏi",
            thong_ke["so_cau_hoi"],
            0,
            1,
            "#388E3C"
        )

        self.__tao_o_thong_ke(
            khung_cac_o,
            "Đề thi",
            thong_ke["so_de_thi"],
            1,
            0,
            "#F57C00"
        )

        self.__tao_o_thong_ke(
            khung_cac_o,
            "Kết quả thi",
            thong_ke["so_ket_qua"],
            1,
            1,
            "#7B1FA2"
        )

        nut_quay_lai = tk.Button(
            self.__cua_so_thong_ke,
            text="Quay lại",
            font=("Arial", 11, "bold"),
            bg="#607D8B",
            fg="white",
            width=12,
            command=self.__dong_cua_so
        )

        nut_quay_lai.pack(pady=20)

    def __dong_cua_so(self):
        self.__cua_so_thong_ke.destroy()
        self.__ham_quay_lai()

    def __tao_o_thong_ke(
        self,
        khung_cha,
        ten_thong_ke,
        so_luong,
        hang,
        cot,
        mau_nen
    ):
        khung = tk.Frame(
            khung_cha,
            width=250,
            height=120,
            bg=mau_nen,
            relief="ridge",
            bd=2
        )

        khung.grid(
            row=hang,
            column=cot,
            padx=15,
            pady=15
        )

        khung.grid_propagate(False)

        nhan_ten = tk.Label(
            khung,
            text=ten_thong_ke,
            font=("Arial", 13, "bold"),
            bg=mau_nen,
            fg="white"
        )

        nhan_ten.pack(pady=(20, 5))

        nhan_so_luong = tk.Label(
            khung,
            text=str(so_luong),
            font=("Arial", 24, "bold"),
            bg=mau_nen,
            fg="white"
        )

        nhan_so_luong.pack()
