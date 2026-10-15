import tkinter as tk
from tkinter import messagebox, ttk


class GiaoDienDoiMatKhau(tk.Toplevel):
    def __init__(
        self,
        cua_so_cha,
        quan_ly_tai_khoan,
        tai_khoan
    ):
        super().__init__(cua_so_cha)

        self.__cua_so_cha = cua_so_cha

        self.__quan_ly_tai_khoan = (
            quan_ly_tai_khoan
        )

        self.__tai_khoan = tai_khoan

        self.__tao_cua_so()
        self.__tao_giao_dien()

    def __tao_cua_so(self):
        self.title("Đổi mật khẩu")
        self.geometry("520x430")
        self.resizable(False, False)

        self.transient(self.__cua_so_cha)
        self.grab_set()

        self.protocol(
            "WM_DELETE_WINDOW",
            self.destroy
        )

        self.bind(
            "<Return>",
            lambda su_kien: (
                self.__xu_ly_doi_mat_khau()
            )
        )

        self.bind(
            "<Escape>",
            lambda su_kien: self.destroy()
        )

    def __tao_giao_dien(self):
        khung_chinh = ttk.Frame(
            self,
            padding=30
        )

        khung_chinh.pack(
            fill="both",
            expand=True
        )

        tieu_de = ttk.Label(
            khung_chinh,
            text="ĐỔI MẬT KHẨU",
            font=("Arial", 20, "bold"),
            foreground="blue"
        )

        tieu_de.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(0, 10)
        )

        ghi_chu = ttk.Label(
            khung_chinh,
            text=(
                "Mật khẩu mới phải có ít nhất "
                "6 ký tự"
            ),
            foreground="#555555"
        )

        ghi_chu.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(0, 15)
        )

        ttk.Separator(
            khung_chinh,
            orient="horizontal"
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(0, 15)
        )

        ttk.Label(
            khung_chinh,
            text="Tên đăng nhập:",
            font=("Arial", 11, "bold")
        ).grid(
            row=3,
            column=0,
            padx=8,
            pady=8,
            sticky="e"
        )

        ttk.Label(
            khung_chinh,
            text=self.__tai_khoan.ten_dang_nhap,
            font=("Arial", 11),
            foreground="blue"
        ).grid(
            row=3,
            column=1,
            padx=8,
            pady=8,
            sticky="w"
        )

        ttk.Label(
            khung_chinh,
            text="Mật khẩu hiện tại:"
        ).grid(
            row=4,
            column=0,
            padx=8,
            pady=8,
            sticky="e"
        )

        self.__mat_khau_hien_tai = (
            tk.StringVar()
        )

        self.__o_mat_khau_hien_tai = ttk.Entry(
            khung_chinh,
            textvariable=(
                self.__mat_khau_hien_tai
            ),
            width=30,
            show="*"
        )

        self.__o_mat_khau_hien_tai.grid(
            row=4,
            column=1,
            padx=8,
            pady=8,
            sticky="ew"
        )

        ttk.Label(
            khung_chinh,
            text="Mật khẩu mới:"
        ).grid(
            row=5,
            column=0,
            padx=8,
            pady=8,
            sticky="e"
        )

        self.__mat_khau_moi = tk.StringVar()

        self.__o_mat_khau_moi = ttk.Entry(
            khung_chinh,
            textvariable=self.__mat_khau_moi,
            width=30,
            show="*"
        )

        self.__o_mat_khau_moi.grid(
            row=5,
            column=1,
            padx=8,
            pady=8,
            sticky="ew"
        )

        ttk.Label(
            khung_chinh,
            text="Xác nhận mật khẩu:"
        ).grid(
            row=6,
            column=0,
            padx=8,
            pady=8,
            sticky="e"
        )

        self.__xac_nhan_mat_khau = (
            tk.StringVar()
        )

        self.__o_xac_nhan_mat_khau = ttk.Entry(
            khung_chinh,
            textvariable=(
                self.__xac_nhan_mat_khau
            ),
            width=30,
            show="*"
        )

        self.__o_xac_nhan_mat_khau.grid(
            row=6,
            column=1,
            padx=8,
            pady=8,
            sticky="ew"
        )

        self.__hien_mat_khau = tk.BooleanVar(
            value=False
        )

        ttk.Checkbutton(
            khung_chinh,
            text="Hiển thị mật khẩu",
            variable=self.__hien_mat_khau,
            command=self.__an_hien_mat_khau
        ).grid(
            row=7,
            column=1,
            padx=8,
            pady=(3, 12),
            sticky="w"
        )

        khung_nut = ttk.Frame(khung_chinh)

        khung_nut.grid(
            row=8,
            column=0,
            columnspan=2,
            pady=(10, 0)
        )

        nut_doi_mat_khau = tk.Button(
            khung_nut,
            text="Đổi mật khẩu",
            font=("Arial", 11, "bold"),
            bg="#1976D2",
            fg="white",
            width=15,
            command=self.__xu_ly_doi_mat_khau
        )

        nut_doi_mat_khau.pack(
            side="left",
            padx=6
        )

        nut_dong = tk.Button(
            khung_nut,
            text="Đóng",
            font=("Arial", 11, "bold"),
            bg="#757575",
            fg="white",
            width=10,
            command=self.destroy
        )

        nut_dong.pack(
            side="left",
            padx=6
        )

        khung_chinh.columnconfigure(
            1,
            weight=1
        )

        self.__o_mat_khau_hien_tai.focus()

    def __an_hien_mat_khau(self):
        if self.__hien_mat_khau.get():
            ky_tu_an = ""
        else:
            ky_tu_an = "*"

        self.__o_mat_khau_hien_tai.config(
            show=ky_tu_an
        )

        self.__o_mat_khau_moi.config(
            show=ky_tu_an
        )

        self.__o_xac_nhan_mat_khau.config(
            show=ky_tu_an
        )

    def __xu_ly_doi_mat_khau(self):
        thanh_cong, thong_bao = (
            self.__quan_ly_tai_khoan
            .doi_mat_khau(
                self.__tai_khoan.ten_dang_nhap,
                self.__mat_khau_hien_tai.get(),
                self.__mat_khau_moi.get(),
                self.__xac_nhan_mat_khau.get()
            )
        )

        if not thanh_cong:
            messagebox.showerror(
                "Đổi mật khẩu thất bại",
                thong_bao,
                parent=self
            )
            return

        messagebox.showinfo(
            "Đổi mật khẩu thành công",
            thong_bao,
            parent=self
        )

        self.destroy()
