import tkinter as tk
from tkinter import ttk, messagebox

from views.giao_dien_them_tai_khoan import (
    GiaoDienThemTaiKhoan
)

from views.giao_dien_sua_tai_khoan import (
    GiaoDienSuaTaiKhoan
)


class GiaoDienQuanLyTaiKhoan:
    def __init__(
        self,
        cua_so_cha,
        quan_ly_tai_khoan,
        ham_quay_lai
    ):
        self.__cua_so_cha = cua_so_cha
        self.__quan_ly_tai_khoan = (
            quan_ly_tai_khoan
        )
        self.__ham_quay_lai = ham_quay_lai

        self.__cua_so = tk.Toplevel(
            self.__cua_so_cha
        )

        self.__cua_so.title(
            "Quản lý tài khoản"
        )

        self.__cua_so.geometry(
            "900x500"
        )

        self.__cua_so.protocol(
            "WM_DELETE_WINDOW",
            self.__dong_cua_so
        )

        self.__tao_giao_dien()
        self.__hien_thi_danh_sach()

    def __tao_giao_dien(self):
        tieu_de = tk.Label(
            self.__cua_so,
            text="DANH SÁCH TÀI KHOẢN",
            font=("Arial", 20, "bold"),
            fg="blue"
        )

        tieu_de.pack(
            pady=20
        )

        khung_nut = tk.Frame(
            self.__cua_so
        )

        khung_nut.pack(
            fill="x",
            padx=20,
            pady=5
        )

        nut_them = tk.Button(
            khung_nut,
            text="Thêm tài khoản",
            font=("Arial", 11, "bold"),
            bg="green",
            fg="white",
            width=16,
            command=self.__mo_giao_dien_them
        )

        nut_them.pack(
            side="left"
        )

        nut_sua = tk.Button(
            khung_nut,
            text="Sửa tài khoản",
            font=("Arial", 11, "bold"),
            bg="orange",
            fg="black",
            width=16,
            command=self.__mo_giao_dien_sua
        )

        nut_sua.pack(
            side="left",
            padx=10
        )

        nut_xoa = tk.Button(
            khung_nut,
            text="Xóa tài khoản",
            font=("Arial", 11, "bold"),
            bg="red",
            fg="white",
            width=16,
            command=self.__xoa_tai_khoan_da_chon
        )

        nut_xoa.pack(
            side="left",
            padx=10
        )

        nut_quay_lai = tk.Button(
            khung_nut,
            text="Quay lại",
            font=("Arial", 11, "bold"),
            bg="blue",
            fg="white",
            width=12,
            command=self.__dong_cua_so
        )

        nut_quay_lai.pack(
            side="right"
        )

        khung_bang = tk.Frame(
            self.__cua_so
        )

        khung_bang.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        ten_cot = (
            "ten_dang_nhap",
            "ho_ten",
            "email",
            "vai_tro"
        )

        self.__bang_tai_khoan = ttk.Treeview(
            khung_bang,
            columns=ten_cot,
            show="headings"
        )

        self.__bang_tai_khoan.heading(
            "ten_dang_nhap",
            text="Tên đăng nhập"
        )

        self.__bang_tai_khoan.heading(
            "ho_ten",
            text="Họ tên"
        )

        self.__bang_tai_khoan.heading(
            "email",
            text="Email"
        )

        self.__bang_tai_khoan.heading(
            "vai_tro",
            text="Vai trò"
        )

        self.__bang_tai_khoan.column(
            "ten_dang_nhap",
            width=150
        )

        self.__bang_tai_khoan.column(
            "ho_ten",
            width=200
        )

        self.__bang_tai_khoan.column(
            "email",
            width=250
        )

        self.__bang_tai_khoan.column(
            "vai_tro",
            width=100
        )

        thanh_cuon = ttk.Scrollbar(
            khung_bang,
            orient="vertical",
            command=self.__bang_tai_khoan.yview
        )

        self.__bang_tai_khoan.configure(
            yscrollcommand=thanh_cuon.set
        )

        self.__bang_tai_khoan.pack(
            side="left",
            fill="both",
            expand=True
        )

        thanh_cuon.pack(
            side="right",
            fill="y"
        )

    def __hien_thi_danh_sach(self):
        cac_dong = (
            self.__bang_tai_khoan
            .get_children()
        )

        for dong in cac_dong:
            self.__bang_tai_khoan.delete(
                dong
            )

        danh_sach = (
            self.__quan_ly_tai_khoan
            .lay_danh_sach_tai_khoan()
        )

        for tai_khoan in danh_sach:
            self.__bang_tai_khoan.insert(
                "",
                "end",
                values=(
                    tai_khoan.ten_dang_nhap,
                    tai_khoan.ho_ten,
                    tai_khoan.email,
                    tai_khoan.vai_tro
                )
            )

    def __mo_giao_dien_them(self):
        self.__giao_dien_them = (
            GiaoDienThemTaiKhoan(
                self.__cua_so,
                self.__quan_ly_tai_khoan,
                self.__hien_thi_danh_sach
            )
        )

    def __mo_giao_dien_sua(self):
        cac_dong_da_chon = (
            self.__bang_tai_khoan.selection()
        )

        if len(cac_dong_da_chon) == 0:
            messagebox.showwarning(
                "Chưa chọn tài khoản",
                "Bạn phải chọn tài khoản cần sửa",
                parent=self.__cua_so
            )
            return

        dong_da_chon = (
            cac_dong_da_chon[0]
        )

        du_lieu = (
            self.__bang_tai_khoan.item(
                dong_da_chon,
                "values"
            )
        )

        ten_dang_nhap = du_lieu[0]
        ho_ten = du_lieu[1]
        email = du_lieu[2]

        self.__giao_dien_sua = (
            GiaoDienSuaTaiKhoan(
                self.__cua_so,
                self.__quan_ly_tai_khoan,
                ten_dang_nhap,
                ho_ten,
                email,
                self.__hien_thi_danh_sach
            )
        )

    def __xoa_tai_khoan_da_chon(self):
        cac_dong_da_chon = (
            self.__bang_tai_khoan.selection()
        )

        if len(cac_dong_da_chon) == 0:
            messagebox.showwarning(
                "Chưa chọn tài khoản",
                "Bạn phải chọn tài khoản cần xóa",
                parent=self.__cua_so
            )
            return

        dong_da_chon = (
            cac_dong_da_chon[0]
        )

        du_lieu = (
            self.__bang_tai_khoan.item(
                dong_da_chon,
                "values"
            )
        )

        ten_dang_nhap = du_lieu[0]

        dong_y = messagebox.askyesno(
            "Xác nhận xóa",
            (
                "Bạn có chắc muốn xóa tài khoản "
                + ten_dang_nhap
                + " không?"
            ),
            parent=self.__cua_so
        )

        if not dong_y:
            return

        ket_qua, thong_bao = (
            self.__quan_ly_tai_khoan
            .xoa_tai_khoan(
                ten_dang_nhap
            )
        )

        if not ket_qua:
            messagebox.showerror(
                "Xóa thất bại",
                thong_bao,
                parent=self.__cua_so
            )
            return

        messagebox.showinfo(
            "Thành công",
            thong_bao,
            parent=self.__cua_so
        )

        self.__hien_thi_danh_sach()

    def __dong_cua_so(self):
        self.__cua_so.destroy()
        self.__ham_quay_lai()