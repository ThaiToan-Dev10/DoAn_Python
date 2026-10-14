import tkinter as tk
from tkinter import messagebox

from views.giao_dien_admin import GiaoDienAdmin
from views.giao_dien_nguoi_dung import GiaoDienNguoiDung
from views.giao_dien_quen_mat_khau import (
    GiaoDienQuenMatKhau
)
from views.giao_dien_dang_ky import (
    GiaoDienDangKy
)


class GiaoDienDangNhap:
    def __init__(
        self,
        cua_so,
        quan_ly_tai_khoan
    ):
        self.__cua_so = cua_so
        self.__quan_ly_tai_khoan = (
            quan_ly_tai_khoan
        )

        self.__tao_giao_dien()

    def __tao_giao_dien(self):
        self.__khung_dang_nhap = tk.Frame(
            self.__cua_so,
            padx=30,
            pady=30
        )

        self.__khung_dang_nhap.pack(
            expand=True
        )

        tieu_de = tk.Label(
            self.__khung_dang_nhap,
            text="ĐĂNG NHẬP HỆ THỐNG",
            font=("Arial", 20, "bold"),
            fg="blue"
        )

        tieu_de.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

        nhan_ten_dang_nhap = tk.Label(
            self.__khung_dang_nhap,
            text="Tên đăng nhập:",
            font=("Arial", 12)
        )

        nhan_ten_dang_nhap.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.__o_ten_dang_nhap = tk.Entry(
            self.__khung_dang_nhap,
            font=("Arial", 12),
            width=25
        )

        self.__o_ten_dang_nhap.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        nhan_mat_khau = tk.Label(
            self.__khung_dang_nhap,
            text="Mật khẩu:",
            font=("Arial", 12)
        )

        nhan_mat_khau.grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.__o_mat_khau = tk.Entry(
            self.__khung_dang_nhap,
            font=("Arial", 12),
            width=25,
            show="*"
        )

        self.__o_mat_khau.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        nut_dang_nhap = tk.Button(
            self.__khung_dang_nhap,
            text="Đăng nhập",
            font=("Arial", 12, "bold"),
            bg="blue",
            fg="white",
            width=15,
            command=self.__xu_ly_dang_nhap
        )

        nut_dang_nhap.grid(
            row=3,
            column=0,
            columnspan=2,
            pady=20
        )

        nut_quen_mat_khau = tk.Button(
            self.__khung_dang_nhap,
            text="Quên mật khẩu?",
            font=("Arial", 10, "underline"),
            fg="blue",
            bd=0,
            cursor="hand2",
            command=(
                self.__mo_giao_dien_quen_mat_khau
            )
        )

        nut_quen_mat_khau.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=(0, 10)
        )

        nut_dang_ky = tk.Button(
            self.__khung_dang_nhap,
            text="Chưa có tài khoản? Đăng ký",
            font=("Arial", 10, "underline"),
            fg="green",
            bd=0,
            cursor="hand2",
            command=self.__mo_giao_dien_dang_ky
        )

        nut_dang_ky.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=(0, 10)
        )

        self.__o_ten_dang_nhap.focus()

    def __mo_giao_dien_quen_mat_khau(self):
        self.__giao_dien_quen_mat_khau = (
            GiaoDienQuenMatKhau(
                self.__cua_so,
                self.__quan_ly_tai_khoan
            )
        )

    def __mo_giao_dien_dang_ky(self):
        self.__giao_dien_dang_ky = (
            GiaoDienDangKy(
                self.__cua_so,
                self.__quan_ly_tai_khoan
            )
        )

    def __xu_ly_dang_nhap(self):
        ten_dang_nhap = (
            self.__o_ten_dang_nhap
            .get()
            .strip()
        )

        mat_khau = (
            self.__o_mat_khau
            .get()
            .strip()
        )

        tai_khoan, thong_bao = (
            self.__quan_ly_tai_khoan
            .dang_nhap(
                ten_dang_nhap,
                mat_khau
            )
        )

        if tai_khoan is None:
            messagebox.showerror(
                "Đăng nhập thất bại",
                thong_bao,
                parent=self.__cua_so
            )
            return

        messagebox.showinfo(
            "Đăng nhập thành công",
            thong_bao
            + "\nXin chào: "
            + tai_khoan.ho_ten,
            parent=self.__cua_so
        )

        self.__khung_dang_nhap.destroy()

        if tai_khoan.vai_tro == "admin":
            self.__giao_dien_admin = (
                GiaoDienAdmin(
                    self.__cua_so,
                    tai_khoan,
                    self.__quan_ly_tai_khoan,
                    self.__hien_thi_lai_dang_nhap
                )
            )
        else:
            self.__giao_dien_nguoi_dung = (
                GiaoDienNguoiDung(
                    self.__cua_so,
                    tai_khoan,
                    self.__hien_thi_lai_dang_nhap
                )
            )

    def __hien_thi_lai_dang_nhap(self):
        self.__tao_giao_dien()