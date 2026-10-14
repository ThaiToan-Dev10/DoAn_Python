import tkinter as tk
from tkinter import messagebox


class GiaoDienSuaTaiKhoan:
    def __init__(
        self,cua_so_cha,quan_ly_tai_khoan,ten_dang_nhap,ho_ten,email,ham_lam_moi):
        self.__quan_ly_tai_khoan = quan_ly_tai_khoan
        self.__ten_dang_nhap = ten_dang_nhap
        self.__ho_ten = ho_ten
        self.__email = email
        self.__ham_lam_moi = ham_lam_moi

        self.__cua_so = tk.Toplevel(cua_so_cha)

        self.__cua_so.title("Sửa tài khoản")
        self.__cua_so.geometry("520x430")
        self.__cua_so.resizable(False, False)

        self.__tao_giao_dien()

    def __tao_giao_dien(self):
        khung_noi_dung = tk.Frame(
            self.__cua_so,
            padx=30,
            pady=20
        )

        khung_noi_dung.pack(
            fill="both",
            expand=True
        )

        tieu_de = tk.Label(
            khung_noi_dung,
            text="SỬA TÀI KHOẢN",
            font=("Arial", 20, "bold"),
            fg="blue"
        )

        tieu_de.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20
        )

        tk.Label(
            khung_noi_dung,
            text="Tên đăng nhập:",
            font=("Arial", 11)
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=8,
            sticky="e"
        )

        self.__o_ten_dang_nhap = tk.Entry(
            khung_noi_dung,
            font=("Arial", 11),
            width=25
        )

        self.__o_ten_dang_nhap.grid(
            row=1,
            column=1,
            padx=10,
            pady=8
        )

        self.__o_ten_dang_nhap.insert(
            0,
            self.__ten_dang_nhap
        )

        self.__o_ten_dang_nhap.config(
            state="readonly"
        )

        tk.Label(
            khung_noi_dung,
            text="Mật khẩu mới:",
            font=("Arial", 11)
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=8,
            sticky="e"
        )

        self.__o_mat_khau_moi = tk.Entry(
            khung_noi_dung,
            font=("Arial", 11),
            width=25,
            show="*"
        )

        self.__o_mat_khau_moi.grid(
            row=2,
            column=1,
            padx=10,
            pady=8
        )

        tk.Label(
            khung_noi_dung,
            text="Họ tên:",
            font=("Arial", 11)
        ).grid(
            row=3,
            column=0,
            padx=10,
            pady=8,
            sticky="e"
        )

        self.__o_ho_ten = tk.Entry(
            khung_noi_dung,
            font=("Arial", 11),
            width=25
        )

        self.__o_ho_ten.grid(
            row=3,
            column=1,
            padx=10,
            pady=8
        )

        self.__o_ho_ten.insert(
            0,
            self.__ho_ten
        )

        tk.Label(
            khung_noi_dung,
            text="Email:",
            font=("Arial", 11)
        ).grid(
            row=4,
            column=0,
            padx=10,
            pady=8,
            sticky="e"
        )

        self.__o_email = tk.Entry(
            khung_noi_dung,
            font=("Arial", 11),
            width=25
        )

        self.__o_email.grid(
            row=4,
            column=1,
            padx=10,
            pady=8
        )

        self.__o_email.insert(
            0,
            self.__email
        )

        ghi_chu = tk.Label(
            khung_noi_dung,
            text=(
                "Để trống mật khẩu mới "
                "nếu không muốn đổi"
            ),
            font=("Arial", 10, "italic"),
            fg="gray"
        )

        ghi_chu.grid(
            row=5,
            column=0,
            columnspan=2,
            pady=10
        )

        nut_luu = tk.Button(
            khung_noi_dung,
            text="Lưu thay đổi",
            font=("Arial", 11, "bold"),
            bg="blue",
            fg="white",
            width=16,
            command=self.__luu_thay_doi
        )

        nut_luu.grid(
            row=6,
            column=0,
            columnspan=2,
            pady=15
        )

        self.__o_ho_ten.focus()

    def __luu_thay_doi(self):
        mat_khau_moi = (
            self.__o_mat_khau_moi.get()
        )

        ho_ten = self.__o_ho_ten.get()
        email = self.__o_email.get()

        ket_qua, thong_bao = (
            self.__quan_ly_tai_khoan
            .cap_nhat_tai_khoan(
                self.__ten_dang_nhap,
                mat_khau_moi,
                ho_ten,
                email
            )
        )

        if not ket_qua:
            messagebox.showerror(
                "Cập nhật thất bại",
                thong_bao
            )
            return

        messagebox.showinfo(
            "Thành công",
            thong_bao
        )

        self.__ham_lam_moi()
        self.__cua_so.destroy()