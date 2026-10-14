import tkinter as tk
from tkinter import ttk, messagebox

from views.giao_dien_chi_tiet_ket_qua import (
    GiaoDienChiTietKetQua
)


class GiaoDienXemKetQua:
    def __init__(
        self,
        cua_so_cha,
        quan_ly_ket_qua,
        quan_ly_de_thi,
        ten_dang_nhap=None,
        ham_quay_lai=None
    ):
        self.__cua_so_cha = cua_so_cha

        self.__quan_ly_ket_qua = (
            quan_ly_ket_qua
        )

        self.__quan_ly_de_thi = (
            quan_ly_de_thi
        )

        self.__ten_dang_nhap = (
            ten_dang_nhap
        )

        self.__ham_quay_lai = (
            ham_quay_lai
        )

        self.__cua_so = tk.Toplevel(
            self.__cua_so_cha
        )

        self.__cua_so.title(
            "Xem kết quả thi"
        )

        self.__cua_so.geometry(
            "1100x550"
        )

        self.__cua_so.protocol(
            "WM_DELETE_WINDOW",
            self.__dong_cua_so
        )

        self.__tao_giao_dien()
        self.__hien_thi_danh_sach_ket_qua()

    def __tao_giao_dien(self):
        if self.__ten_dang_nhap is None:
            noi_dung_tieu_de = (
                "KẾT QUẢ THI CỦA TẤT CẢ NGƯỜI DÙNG"
            )
        else:
            noi_dung_tieu_de = (
                "KẾT QUẢ THI CỦA "
                + self.__ten_dang_nhap.upper()
            )

        tieu_de = tk.Label(
            self.__cua_so,
            text=noi_dung_tieu_de,
            font=("Arial", 19, "bold"),
            fg="blue"
        )

        tieu_de.pack(pady=20)

        self.__nhan_so_luong = tk.Label(
            self.__cua_so,
            text="",
            font=("Arial", 11)
        )

        self.__nhan_so_luong.pack(
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
            "ma_ket_qua",
            "ten_dang_nhap",
            "ma_de_thi",
            "ten_de_thi",
            "so_cau_dung",
            "diem",
            "xep_loai",
            "thoi_gian"
        )

        self.__bang_ket_qua = ttk.Treeview(
            khung_bang,
            columns=cac_cot,
            show="headings",
            height=15
        )

        self.__bang_ket_qua.heading(
            "ma_ket_qua",
            text="Mã kết quả"
        )

        self.__bang_ket_qua.heading(
            "ten_dang_nhap",
            text="Người làm"
        )

        self.__bang_ket_qua.heading(
            "ma_de_thi",
            text="Mã đề"
        )

        self.__bang_ket_qua.heading(
            "ten_de_thi",
            text="Tên đề thi"
        )

        self.__bang_ket_qua.heading(
            "so_cau_dung",
            text="Số câu đúng"
        )

        self.__bang_ket_qua.heading(
            "diem",
            text="Điểm"
        )

        self.__bang_ket_qua.heading(
            "xep_loai",
            text="Xếp loại"
        )

        self.__bang_ket_qua.heading(
            "thoi_gian",
            text="Thời gian nộp"
        )

        self.__bang_ket_qua.column(
            "ma_ket_qua",
            width=90,
            anchor="center"
        )

        self.__bang_ket_qua.column(
            "ten_dang_nhap",
            width=110,
            anchor="center"
        )

        self.__bang_ket_qua.column(
            "ma_de_thi",
            width=80,
            anchor="center"
        )

        self.__bang_ket_qua.column(
            "ten_de_thi",
            width=220
        )

        self.__bang_ket_qua.column(
            "so_cau_dung",
            width=100,
            anchor="center"
        )

        self.__bang_ket_qua.column(
            "diem",
            width=70,
            anchor="center"
        )

        self.__bang_ket_qua.column(
            "xep_loai",
            width=90,
            anchor="center"
        )

        self.__bang_ket_qua.column(
            "thoi_gian",
            width=150,
            anchor="center"
        )

        thanh_cuon = ttk.Scrollbar(
            khung_bang,
            orient="vertical",
            command=self.__bang_ket_qua.yview
        )

        self.__bang_ket_qua.configure(
            yscrollcommand=thanh_cuon.set
        )

        self.__bang_ket_qua.pack(
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

        nut_lam_moi = tk.Button(
            khung_nut,
            text="Làm mới",
            font=("Arial", 11, "bold"),
            bg="#2196F3",
            fg="white",
            width=14,
            command=self.__hien_thi_danh_sach_ket_qua
        )

        nut_lam_moi.pack(
            side="left",
            padx=5
        )

        nut_xem_dap_an = tk.Button(
            khung_nut,
            text="Xem đáp án",
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            width=14,
            command=self.__xem_chi_tiet_ket_qua
        )

        nut_xem_dap_an.pack(
            side="left",
            padx=5
        )

        nut_quay_lai = tk.Button(
            khung_nut,
            text="Quay lại",
            font=("Arial", 11, "bold"),
            bg="#607D8B",
            fg="white",
            width=14,
            command=self.__dong_cua_so
        )

        nut_quay_lai.pack(
            side="left",
            padx=5
        )

    def __hien_thi_danh_sach_ket_qua(self):
        cac_dong_cu = (
            self.__bang_ket_qua.get_children()
        )

        for dong in cac_dong_cu:
            self.__bang_ket_qua.delete(dong)

        if self.__ten_dang_nhap is None:
            danh_sach = (
                self.__quan_ly_ket_qua
                .lay_danh_sach_ket_qua()
            )
        else:
            danh_sach = (
                self.__quan_ly_ket_qua
                .lay_ket_qua_theo_nguoi_dung(
                    self.__ten_dang_nhap
                )
            )

        self.__nhan_so_luong.config(
            text=(
                "Số lượt thi: "
                + str(len(danh_sach))
            )
        )

        for ket_qua in danh_sach:
            de_thi = (
                self.__quan_ly_de_thi
                .tim_de_thi_theo_ma(
                    ket_qua.ma_de_thi
                )
            )

            if de_thi is None:
                ten_de_thi = "(Đề đã bị xóa)"
            else:
                ten_de_thi = de_thi.ten_de_thi

            self.__bang_ket_qua.insert(
                "",
                "end",
                values=(
                    ket_qua.ma_ket_qua,
                    ket_qua.ten_dang_nhap,
                    ket_qua.ma_de_thi,
                    ten_de_thi,
                    (
                        str(ket_qua.so_cau_dung)
                        + "/"
                        + str(ket_qua.tong_so_cau)
                    ),
                    ket_qua.diem,
                    ket_qua.xep_loai,
                    ket_qua.thoi_gian_nop_bai
                )
            )

    def __xem_chi_tiet_ket_qua(self):
        cac_dong_da_chon = (
            self.__bang_ket_qua.selection()
        )

        if len(cac_dong_da_chon) == 0:
            messagebox.showwarning(
                "Chưa chọn kết quả",
                "Bạn phải chọn một kết quả cần xem",
                parent=self.__cua_so
            )
            return

        dong_da_chon = cac_dong_da_chon[0]

        du_lieu = self.__bang_ket_qua.item(
            dong_da_chon,
            "values"
        )

        ma_ket_qua = du_lieu[0]

        self.__giao_dien_chi_tiet_ket_qua = (
            GiaoDienChiTietKetQua(
                self.__cua_so,
                self.__quan_ly_ket_qua,
                ma_ket_qua
            )
        )

    def __dong_cua_so(self):
        self.__cua_so.destroy()

        if self.__ham_quay_lai is not None:
            self.__ham_quay_lai()
