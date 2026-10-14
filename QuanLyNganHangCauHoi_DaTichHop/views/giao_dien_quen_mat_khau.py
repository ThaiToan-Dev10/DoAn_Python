import tkinter as tk
from tkinter import messagebox


class GiaoDienQuenMatKhau:
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
            "Quên mật khẩu"
        )

        self.__cua_so.geometry(
            "520x400"
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
            text="ĐẶT LẠI MẬT KHẨU",
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
            width=27
        )

        self.__o_ten_dang_nhap.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            khung_chinh,
            text="Email đã đăng ký:",
            font=("Arial", 11)
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.__o_email = tk.Entry(
            khung_chinh,
            font=("Arial", 11),
            width=27
        )

        self.__o_email.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            khung_chinh,
            text="Mật khẩu mới:",
            font=("Arial", 11)
        ).grid(
            row=3,
            column=0,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.__o_mat_khau_moi = tk.Entry(
            khung_chinh,
            font=("Arial", 11),
            width=27,
            show="*"
        )

        self.__o_mat_khau_moi.grid(
            row=3,
            column=1,
            padx=10,
            pady=10
        )

        tk.Label(
            khung_chinh,
            text="Xác nhận mật khẩu:",
            font=("Arial", 11)
        ).grid(
            row=4,
            column=0,
            padx=10,
            pady=10,
            sticky="e"
        )

        self.__o_xac_nhan_mat_khau = (
            tk.Entry(
                khung_chinh,
                font=("Arial", 11),
                width=27,
                show="*"
            )
        )

        self.__o_xac_nhan_mat_khau.grid(
            row=4,
            column=1,
            padx=10,
            pady=10
        )

        khung_nut = tk.Frame(
            khung_chinh
        )

        khung_nut.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=20
        )

        nut_dat_lai = tk.Button(
            khung_nut,
            text="Đặt lại mật khẩu",
            font=("Arial", 11, "bold"),
            bg="green",
            fg="white",
            width=17,
            command=(
                self.__xu_ly_dat_lai_mat_khau
            )
        )

        nut_dat_lai.grid(
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

    def __xu_ly_dat_lai_mat_khau(self):
        ten_dang_nhap = (
            self.__o_ten_dang_nhap
            .get()
            .strip()
        )

        email = (
            self.__o_email
            .get()
            .strip()
        )

        mat_khau_moi = (
            self.__o_mat_khau_moi
            .get()
            .strip()
        )

        xac_nhan_mat_khau = (
            self.__o_xac_nhan_mat_khau
            .get()
            .strip()
        )

        if mat_khau_moi != xac_nhan_mat_khau:
            messagebox.showerror(
                "Không hợp lệ",
                "Mật khẩu xác nhận không khớp",
                parent=self.__cua_so
            )
            return

        thanh_cong, thong_bao = (
            self.__quan_ly_tai_khoan
            .dat_lai_mat_khau(
                ten_dang_nhap,
                email,
                mat_khau_moi
            )
        )

        if not thanh_cong:
            messagebox.showerror(
                "Không thể đặt lại mật khẩu",
                thong_bao,
                parent=self.__cua_so
            )
            return

        messagebox.showinfo(
            "Thành công",
            thong_bao,
            parent=self.__cua_so
        )

        self.__cua_so.destroy()