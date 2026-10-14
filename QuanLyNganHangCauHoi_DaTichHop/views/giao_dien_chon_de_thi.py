import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

from views.giao_dien_lam_bai import GiaoDienLamBai


class GiaoDienChonDeThi:
    def __init__(
        self,
        cua_so_cha,
        ten_dang_nhap,
        quan_ly_de_thi,
        quan_ly_cau_hoi,
        quan_ly_ket_qua
    ):
        self.__cua_so_cha = cua_so_cha
        self.__ten_dang_nhap = ten_dang_nhap
    
        self.__quan_ly_de_thi = (
            quan_ly_de_thi
        )
    
        self.__quan_ly_cau_hoi = (
            quan_ly_cau_hoi
        )
    
        self.__quan_ly_ket_qua = (
            quan_ly_ket_qua
        )
    
        self.__cua_so = tk.Toplevel(
            self.__cua_so_cha
        )
    
        self.__cua_so.title(
            "Chọn đề thi"
        )
    
        self.__cua_so.geometry(
            "850x500"
        )
    
        self.__tao_giao_dien()
        self.__hien_thi_de_thi_dang_mo()

    def __tao_giao_dien(self):
        tieu_de = tk.Label(
            self.__cua_so,
            text="DANH SÁCH ĐỀ THI ĐANG MỞ",
            font=("Arial", 20, "bold"),
            fg="blue"
        )

        tieu_de.pack(pady=20)

        thong_tin_nguoi_dung = tk.Label(
            self.__cua_so,
            text=(
                "Người làm bài: "
                + self.__ten_dang_nhap
            ),
            font=("Arial", 12)
        )

        thong_tin_nguoi_dung.pack(
            pady=5
        )

        khung_bang = tk.Frame(
            self.__cua_so,
            padx=20,
            pady=10
        )

        khung_bang.pack(
            fill="both",
            expand=True
        )

        cac_cot = (
            "ma_de_thi",
            "ten_de_thi",
            "mon_hoc",
            "thoi_gian",
            "so_cau"
        )

        self.__bang_de_thi = ttk.Treeview(
            khung_bang,
            columns=cac_cot,
            show="headings",
            height=12
        )

        self.__bang_de_thi.heading(
            "ma_de_thi",
            text="Mã đề"
        )

        self.__bang_de_thi.heading(
            "ten_de_thi",
            text="Tên đề thi"
        )

        self.__bang_de_thi.heading(
            "mon_hoc",
            text="Môn học"
        )

        self.__bang_de_thi.heading(
            "thoi_gian",
            text="Thời gian"
        )

        self.__bang_de_thi.heading(
            "so_cau",
            text="Số câu"
        )

        self.__bang_de_thi.column(
            "ma_de_thi",
            width=90,
            anchor="center"
        )

        self.__bang_de_thi.column(
            "ten_de_thi",
            width=270
        )

        self.__bang_de_thi.column(
            "mon_hoc",
            width=130,
            anchor="center"
        )

        self.__bang_de_thi.column(
            "thoi_gian",
            width=110,
            anchor="center"
        )

        self.__bang_de_thi.column(
            "so_cau",
            width=90,
            anchor="center"
        )

        thanh_cuon = ttk.Scrollbar(
            khung_bang,
            orient="vertical",
            command=self.__bang_de_thi.yview
        )

        self.__bang_de_thi.configure(
            yscrollcommand=thanh_cuon.set
        )

        self.__bang_de_thi.pack(
            side="left",
            fill="both",
            expand=True
        )

        thanh_cuon.pack(
            side="right",
            fill="y"
        )

        khung_nut = tk.Frame(
            self.__cua_so
        )

        khung_nut.pack(pady=15)

        nut_bat_dau = tk.Button(
            khung_nut,
            text="Bắt đầu làm bài",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=18,
            command=self.__xu_ly_bat_dau
        )

        nut_bat_dau.pack(
            side="left",
            padx=5
        )

        nut_lam_moi = tk.Button(
            khung_nut,
            text="Làm mới",
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            width=12,
            command=self.__hien_thi_de_thi_dang_mo
        )

        nut_lam_moi.pack(
            side="left",
            padx=5
        )

        nut_dong = tk.Button(
            khung_nut,
            text="Đóng",
            font=("Arial", 12, "bold"),
            width=12,
            command=self.__cua_so.destroy
        )

        nut_dong.pack(
            side="left",
            padx=5
        )

    def __hien_thi_de_thi_dang_mo(self):
        cac_dong_cu = (
            self.__bang_de_thi.get_children()
        )

        for dong in cac_dong_cu:
            self.__bang_de_thi.delete(dong)

        danh_sach = (
            self.__quan_ly_de_thi
            .lay_danh_sach_de_thi_dang_mo()
        )

        for de_thi in danh_sach:
            self.__bang_de_thi.insert(
                "",
                "end",
                values=(
                    de_thi.ma_de_thi,
                    de_thi.ten_de_thi,
                    de_thi.mon_hoc,
                    str(
                        de_thi.thoi_gian_lam_bai
                    ) + " phút",
                    de_thi.so_luong_cau_hoi
                )
            )

    def __lay_de_thi_duoc_chon(self):
        dong_duoc_chon = (
            self.__bang_de_thi.selection()
        )

        if len(dong_duoc_chon) == 0:
            messagebox.showwarning(
                "Chưa chọn đề thi",
                "Bạn hãy chọn một đề thi trong bảng",
                parent=self.__cua_so
            )

            return None

        du_lieu = self.__bang_de_thi.item(
            dong_duoc_chon[0],
            "values"
        )

        ma_de_thi = du_lieu[0]

        de_thi = (
            self.__quan_ly_de_thi
            .tim_de_thi_theo_ma(ma_de_thi)
        )

        return de_thi

    def __xu_ly_bat_dau(self):
        de_thi = (
            self.__lay_de_thi_duoc_chon()
        )

        if de_thi is None:
            return

        noi_dung_xac_nhan = (
            "Bạn có muốn bắt đầu làm đề này không?"
            + "\n\nTên đề: "
            + de_thi.ten_de_thi
            + "\nMã đề: "
            + de_thi.ma_de_thi
            + "\nSố câu: "
            + str(de_thi.so_luong_cau_hoi)
            + "\nThời gian: "
            + str(de_thi.thoi_gian_lam_bai)
            + " phút"
        )

        dong_y = messagebox.askyesno(
            "Xác nhận làm bài",
            noi_dung_xac_nhan,
            parent=self.__cua_so
        )

        if not dong_y:
            return

        self.__giao_dien_lam_bai = (
            GiaoDienLamBai(
                self.__cua_so,
                self.__ten_dang_nhap,
                de_thi,
                self.__quan_ly_cau_hoi,
                self.__quan_ly_ket_qua
            )
        )