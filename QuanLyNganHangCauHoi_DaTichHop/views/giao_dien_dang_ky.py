import tkinter as tk
from tkinter import messagebox


class GiaoDienDangKy:
    def __init__(
        self,
        cua_so_cha,
        quan_ly_tai_khoan
    ):
        self.__cua_so_cha = cua_so_cha
        self.__quan_ly_tai_khoan = (
            quan_ly_tai_khoan
        )

        self.__tao_cua_so()
        self.__tao_giao_dien()

    def __tao_cua_so(self):
        self.__cua_so = tk.Toplevel(
            self.__cua_so_cha
        )

        self.__cua_so.title(
            "Đăng ký tài khoản"
        )

        self.__cua_so.geometry(
            "540x500"
        )

        self.__cua_so.resizable(
            False,
            False
        )

        self.__cua_so.transient(
            self.__cua_so_cha
        )

        self.__cua_so.grab_set()

    def __tao_giao_dien(self):
        khung_chinh = tk.Frame(
            self.__cua_so,
            padx=30,
            pady=25
        )

        khung_chinh.pack(
            fill="both",
            expand=True
        )

        tieu_de = tk.Label(
            khung_chinh,
            text="ĐĂNG KÝ TÀI KHOẢN",
            font=("Arial", 18, "bold"),
            fg="blue"
        )

        tieu_de.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(0, 20)
        )

        tk.Label(
            khung_chinh,
            text="Tên đăng nhập:",
            font=("Arial", 11)
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.__o_ten_dang_nhap = tk.Entry(
            khung_chinh,
            font=("Arial", 11),
            width=28
        )

        self.__o_ten_dang_nhap.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            khung_chinh,
            text="Họ và tên:",
            font=("Arial", 11)
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.__o_ho_ten = tk.Entry(
            khung_chinh,
            font=("Arial", 11),
            width=28
        )

        self.__o_ho_ten.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            khung_chinh,
            text="Email:",
            font=("Arial", 11)
        ).grid(
            row=3,
            column=0,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.__o_email = tk.Entry(
            khung_chinh,
            font=("Arial", 11),
            width=28
        )

        self.__o_email.grid(
            row=3,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            khung_chinh,
            text="Mật khẩu:",
            font=("Arial", 11)
        ).grid(
            row=4,
            column=0,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.__o_mat_khau = tk.Entry(
            khung_chinh,
            font=("Arial", 11),
            width=28,
            show="*"
        )

        self.__o_mat_khau.grid(
            row=4,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            khung_chinh,
            text="Xác nhận mật khẩu:",
            font=("Arial", 11)
        ).grid(
            row=5,
            column=0,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.__o_xac_nhan_mat_khau = (
            tk.Entry(
                khung_chinh,
                font=("Arial", 11),
                width=28,
                show="*"
            )
        )

        self.__o_xac_nhan_mat_khau.grid(
            row=5,
            column=1,
            padx=10,
            pady=10
        )

        khung_nut = tk.Frame(
            khung_chinh
        )

        khung_nut.grid(
            row=6,
            column=0,
            columnspan=2,
            pady=25
        )

        nut_dang_ky = tk.Button(
            khung_nut,
            text="Đăng ký",
            font=("Arial", 11, "bold"),
            bg="green",
            fg="white",
            width=15,
            command=self.__xu_ly_dang_ky
        )

        nut_dang_ky.grid(
            row=0,
            column=0,
            padx=8
        )

        nut_dong = tk.Button(
            khung_nut,
            text="Đóng",
            font=("Arial", 11, "bold"),
            bg="gray",
            fg="white",
            width=10,
            command=self.__cua_so.destroy
        )

        nut_dong.grid(
            row=0,
            column=1,
            padx=8
        )

        self.__o_ten_dang_nhap.focus()

    def __xu_ly_dang_ky(self):
        ten_dang_nhap = (
            self.__o_ten_dang_nhap
            .get()
            .strip()
        )

        ho_ten = (
            self.__o_ho_ten
            .get()
            .strip()
        )

        email = (
            self.__o_email
            .get()
            .strip()
        )

        mat_khau = (
            self.__o_mat_khau
            .get()
            .strip()
        )

        xac_nhan_mat_khau = (
            self.__o_xac_nhan_mat_khau
            .get()
            .strip()
        )

        if (
            ten_dang_nhap == ""
            or ho_ten == ""
            or email == ""
            or mat_khau == ""
            or xac_nhan_mat_khau == ""
        ):
            messagebox.showerror(
                "Thông tin chưa đầy đủ",
                "Vui lòng nhập đầy đủ thông tin",
                parent=self.__cua_so
            )
            return

        if mat_khau != xac_nhan_mat_khau:
            messagebox.showerror(
                "Không hợp lệ",
                "Mật khẩu xác nhận không khớp",
                parent=self.__cua_so
            )
            return

        thanh_cong, thong_bao = (
            self.__quan_ly_tai_khoan
            .dang_ky_tai_khoan(
                ten_dang_nhap,
                mat_khau,
                ho_ten,
                email
            )
        )

        if not thanh_cong:
            messagebox.showerror(
                "Đăng ký thất bại",
                thong_bao,
                parent=self.__cua_so
            )
            return

        messagebox.showinfo(
            "Đăng ký thành công",
            thong_bao
            + "\nBạn có thể đăng nhập ngay bây giờ.",
            parent=self.__cua_so
        )

        self.__cua_so.destroy()