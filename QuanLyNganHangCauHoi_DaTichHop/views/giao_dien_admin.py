import tkinter as tk
from tkinter import messagebox

from managers.quan_ly_thong_ke import QuanLyThongKe
from managers.quan_ly_cau_hoi import QuanLyCauHoi
from managers.quan_ly_de_thi import QuanLyDeThi
from managers.quan_ly_ket_qua import QuanLyKetQua

from views.giao_dien_thong_ke import (
    GiaoDienThongKe
)
from views.giao_dien_quan_ly_tai_khoan import (
    GiaoDienQuanLyTaiKhoan
)
from views.giao_dien_quan_ly_cau_hoi import (
    GiaoDienQuanLyCauHoi
)
from views.giao_dien_quan_ly_de_thi import (
    GiaoDienQuanLyDeThi
)
from views.giao_dien_xem_ket_qua import (
    GiaoDienXemKetQua
)


class GiaoDienAdmin:
    def __init__(
        self,
        cua_so,
        tai_khoan,
        quan_ly_tai_khoan,
        ham_dang_xuat
    ):
        self.__cua_so = cua_so
        self.__tai_khoan = tai_khoan

        self.__quan_ly_tai_khoan = (
            quan_ly_tai_khoan
        )

        self.__ham_dang_xuat = (
            ham_dang_xuat
        )

        self.__quan_ly_cau_hoi = (
            QuanLyCauHoi()
        )

        self.__quan_ly_de_thi = (
            QuanLyDeThi(
                self.__quan_ly_cau_hoi
            )
        )

        self.__quan_ly_ket_qua = (
            QuanLyKetQua(
                self.__quan_ly_cau_hoi,
                self.__quan_ly_de_thi
            )
        )

        self.__tao_giao_dien()

    def __mo_quan_ly_tai_khoan(self):
        self.__giao_dien_quan_ly_tai_khoan = (
            GiaoDienQuanLyTaiKhoan(
                self.__cua_so,
                self.__quan_ly_tai_khoan,
                self.__hien_thi_lai_admin
            )
        )

        self.__cua_so.withdraw()

    def __hien_thi_lai_admin(self):
        self.__cua_so.deiconify()
        self.__cua_so.lift()
        self.__cua_so.focus_force()

    def __mo_quan_ly_cau_hoi(self):
        self.__giao_dien_quan_ly_cau_hoi = (
            GiaoDienQuanLyCauHoi(
                self.__cua_so,
                self.__quan_ly_cau_hoi,
                self.__hien_thi_lai_admin
            )
        )

        self.__cua_so.withdraw()

    def __mo_quan_ly_de_thi(self):
        self.__giao_dien_quan_ly_de_thi = (
            GiaoDienQuanLyDeThi(
                self.__cua_so,
                self.__quan_ly_de_thi,
                self.__hien_thi_lai_admin
            )
        )
    
        self.__cua_so.withdraw()

    def __mo_xem_ket_qua(self):
        self.__giao_dien_xem_ket_qua = (
            GiaoDienXemKetQua(
                self.__cua_so,
                self.__quan_ly_ket_qua,
                self.__quan_ly_de_thi,
                None,
                self.__hien_thi_lai_admin
            )
        )
    
        self.__cua_so.withdraw()

    def __mo_giao_dien_thong_ke(self):
        self.__quan_ly_thong_ke = QuanLyThongKe()
    
        self.__giao_dien_thong_ke = (
            GiaoDienThongKe(
                self.__cua_so,
                self.__quan_ly_thong_ke,
                self.__hien_thi_lai_admin
            )
        )

        self.__cua_so.withdraw()

    def __tao_giao_dien(self):
        self.__khung_chinh = tk.Frame(
            self.__cua_so,
            bg="#f2f2f2"
        )

        self.__khung_chinh.pack(
            fill="both",
            expand=True
        )

        tieu_de = tk.Label(
            self.__khung_chinh,
            text=(
                "HỆ THỐNG QUẢN LÝ "
                "NGÂN HÀNG CÂU HỎI"
            ),
            font=("Arial", 22, "bold"),
            fg="blue",
            bg="#f2f2f2"
        )

        tieu_de.pack(
            pady=40
        )

        loi_chao = tk.Label(
            self.__khung_chinh,
            text=(
                "Xin chào: "
                + self.__tai_khoan.ho_ten
                + " - Vai trò: "
                + self.__tai_khoan.vai_tro
            ),
            font=("Arial", 13),
            bg="#f2f2f2"
        )

        loi_chao.pack(
            pady=10
        )

        khung_chuc_nang = tk.Frame(
            self.__khung_chinh,
            bg="#f2f2f2"
        )

        khung_chuc_nang.pack(
            pady=30
        )

        nut_quan_ly_tai_khoan = tk.Button(
            khung_chuc_nang,
            text="Quản lý tài khoản",
            font=("Arial", 12, "bold"),
            width=22,
            height=2,
            command=self.__mo_quan_ly_tai_khoan
        )

        nut_quan_ly_tai_khoan.grid(
            row=0,
            column=0,
            padx=15,
            pady=15
        )

        nut_quan_ly_cau_hoi = tk.Button(
            khung_chuc_nang,
            text="Quản lý câu hỏi",
            font=("Arial", 12, "bold"),
            width=22,
            height=2,
            command=self.__mo_quan_ly_cau_hoi
        )

        nut_quan_ly_cau_hoi.grid(
            row=0,
            column=1,
            padx=15,
            pady=15
        )

        nut_quan_ly_de_thi = tk.Button(
            khung_chuc_nang,
            text="Quản lý đề thi",
            font=("Arial", 12, "bold"),
            width=22,
            height=2,
            command=self.__mo_quan_ly_de_thi
        )

        nut_quan_ly_de_thi.grid(
            row=1,
            column=0,
            padx=15,
            pady=15
        )

        nut_xem_ket_qua = tk.Button(
            khung_chuc_nang,
            text="Xem kết quả",
            font=("Arial", 12, "bold"),
            width=22,
            height=2,
            command=self.__mo_xem_ket_qua
        )

        nut_xem_ket_qua.grid(
            row=1,
            column=1,
            padx=15,
            pady=15
        )

        nut_thong_ke = tk.Button(
            self.__khung_chinh,
            text="Thống kê tổng quan",
            font=("Arial", 12, "bold"),
            width=25,
            height=2,
            command=self.__mo_giao_dien_thong_ke
        )

        nut_thong_ke.pack(
            pady=10
        )

        nut_dang_xuat = tk.Button(
            self.__khung_chinh,
            text="Đăng xuất",
            font=("Arial", 11, "bold"),
            bg="red",
            fg="white",
            width=15,
            command=self.__dang_xuat
        )

        nut_dang_xuat.pack(
            pady=20
        )

    def __dang_xuat(self):
        dong_y = messagebox.askyesno(
            "Xác nhận đăng xuất!",
            "Bạn có chắc muốn đăng xuất không?",
            parent=self.__cua_so
        )

        if not dong_y:
            return

        cac_thanh_phan = (
            self.__cua_so.winfo_children()
        )

        for thanh_phan in cac_thanh_phan:
            if isinstance(
                thanh_phan,
                tk.Toplevel
            ):
                thanh_phan.destroy()

        self.__khung_chinh.destroy()
        self.__ham_dang_xuat()