import tkinter as tk
from tkinter import messagebox

from managers.quan_ly_cau_hoi import QuanLyCauHoi
from managers.quan_ly_de_thi import QuanLyDeThi
from managers.quan_ly_ket_qua import QuanLyKetQua

from views.giao_dien_chon_de_thi import (
    GiaoDienChonDeThi
)
from views.giao_dien_xem_ket_qua import (
    GiaoDienXemKetQua
)


class GiaoDienNguoiDung:
    def __init__(
        self,
        cua_so,
        tai_khoan,
        ham_dang_xuat
    ):
        self.__cua_so = cua_so
        self.__tai_khoan = tai_khoan
        self.__ham_dang_xuat = ham_dang_xuat

        # Dùng chung một ngân hàng câu hỏi
        self.__quan_ly_cau_hoi = QuanLyCauHoi()

        # Quản lý đề thi sử dụng ngân hàng câu hỏi trên
        self.__quan_ly_de_thi = QuanLyDeThi(
            self.__quan_ly_cau_hoi
        )

        # Quản lý kết quả dùng chung câu hỏi và đề thi
        self.__quan_ly_ket_qua = QuanLyKetQua(
            self.__quan_ly_cau_hoi,
            self.__quan_ly_de_thi
        )

        self.__tao_giao_dien()

    def __tao_giao_dien(self):
        self.__khung_chinh = tk.Frame(
            self.__cua_so,
            padx=30,
            pady=30
        )

        self.__khung_chinh.pack(
            fill="both",
            expand=True
        )

        tieu_de = tk.Label(
            self.__khung_chinh,
            text="TRANG NGƯỜI DÙNG",
            font=("Arial", 22, "bold"),
            fg="blue"
        )

        tieu_de.pack(pady=20)

        loi_chao = tk.Label(
            self.__khung_chinh,
            text=(
                "Xin chào: "
                + self.__tai_khoan.ho_ten
            ),
            font=("Arial", 14)
        )

        loi_chao.pack(pady=10)

        thong_tin_tai_khoan = tk.Label(
            self.__khung_chinh,
            text=(
                "Tên đăng nhập: "
                + self.__tai_khoan.ten_dang_nhap
            ),
            font=("Arial", 11)
        )

        thong_tin_tai_khoan.pack(
            pady=5
        )

        nut_lam_bai = tk.Button(
            self.__khung_chinh,
            text="Làm bài thi",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=25,
            height=2,
            command=self.__mo_chuc_nang_lam_bai
        )

        nut_lam_bai.pack(pady=10)

        nut_xem_ket_qua = tk.Button(
            self.__khung_chinh,
            text="Xem kết quả của tôi",
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            width=25,
            height=2,
            command=self.__mo_chuc_nang_xem_ket_qua
        )

        nut_xem_ket_qua.pack(pady=10)

        nut_dang_xuat = tk.Button(
            self.__khung_chinh,
            text="Đăng xuất",
            font=("Arial", 11, "bold"),
            bg="red",
            fg="white",
            width=15,
            command=self.__dang_xuat
        )

        nut_dang_xuat.pack(pady=20)

    def __mo_chuc_nang_lam_bai(self):
        self.__giao_dien_chon_de_thi = (
            GiaoDienChonDeThi(
                self.__cua_so,
                self.__tai_khoan.ten_dang_nhap,
                self.__quan_ly_de_thi,
                self.__quan_ly_cau_hoi,
                self.__quan_ly_ket_qua
            )
        )

    def __mo_chuc_nang_xem_ket_qua(self):
        self.__giao_dien_xem_ket_qua = (
            GiaoDienXemKetQua(
                self.__cua_so,
                self.__quan_ly_ket_qua,
                self.__quan_ly_de_thi,
                self.__tai_khoan.ten_dang_nhap
            )
        )

    def __dang_xuat(self):
        dong_y = messagebox.askyesno(
            "Xác nhận đăng xuất",
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