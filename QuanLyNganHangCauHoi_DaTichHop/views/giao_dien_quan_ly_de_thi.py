import tkinter as tk
from tkinter import ttk, messagebox


class GiaoDienQuanLyDeThi:
    def __init__(
        self,
        cua_so_cha,
        quan_ly_de_thi,
        ham_quay_lai
    ):
        self.__cua_so_cha = cua_so_cha
        self.__quan_ly_de_thi = quan_ly_de_thi
        self.__ham_quay_lai = ham_quay_lai

        self.__cua_so = tk.Toplevel(
            self.__cua_so_cha
        )

        self.__cua_so.title(
            "Quản lý đề thi"
        )

        self.__cua_so.geometry(
            "1180x680"
        )

        self.__cua_so.minsize(
            1050,
            620
        )

        self.__cua_so.protocol(
            "WM_DELETE_WINDOW",
            self.__dong_cua_so
        )

        self.__tao_giao_dien()
        self.__hien_thi_danh_sach_de_thi()

    def __tao_giao_dien(self):
        tieu_de = tk.Label(
            self.__cua_so,
            text="QUẢN LÝ ĐỀ THI",
            font=("Arial", 20, "bold"),
            fg="blue"
        )

        tieu_de.pack(pady=(15, 10))

        self.__khung_tao_de = tk.LabelFrame(
            self.__cua_so,
            text="Tạo đề tự động theo ma trận mức độ",
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10
        )

        self.__khung_tao_de.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        nhan_ten_de = tk.Label(
            self.__khung_tao_de,
            text="Tên đề thi:",
            font=("Arial", 11)
        )

        nhan_ten_de.grid(
            row=0,
            column=0,
            padx=5,
            pady=7,
            sticky="e"
        )

        self.__o_ten_de_thi = tk.Entry(
            self.__khung_tao_de,
            font=("Arial", 11),
            width=30
        )

        self.__o_ten_de_thi.grid(
            row=0,
            column=1,
            padx=5,
            pady=7,
            sticky="we"
        )

        nhan_mon_hoc = tk.Label(
            self.__khung_tao_de,
            text="Môn học:",
            font=("Arial", 11)
        )

        nhan_mon_hoc.grid(
            row=0,
            column=2,
            padx=5,
            pady=7,
            sticky="e"
        )

        self.__o_mon_hoc = tk.Entry(
            self.__khung_tao_de,
            font=("Arial", 11),
            width=22
        )

        self.__o_mon_hoc.grid(
            row=0,
            column=3,
            padx=5,
            pady=7,
            sticky="we"
        )

        self.__o_mon_hoc.insert(
            0,
            "Tin học"
        )

        nhan_thoi_gian = tk.Label(
            self.__khung_tao_de,
            text="Thời gian (phút):",
            font=("Arial", 11)
        )

        nhan_thoi_gian.grid(
            row=1,
            column=0,
            padx=5,
            pady=7,
            sticky="e"
        )

        self.__o_thoi_gian = tk.Entry(
            self.__khung_tao_de,
            font=("Arial", 11),
            width=30
        )

        self.__o_thoi_gian.grid(
            row=1,
            column=1,
            padx=5,
            pady=7,
            sticky="we"
        )

        self.__o_thoi_gian.insert(
            0,
            "20"
        )

        nhan_seed = tk.Label(
            self.__khung_tao_de,
            text="Seed trộn đề:",
            font=("Arial", 11)
        )

        nhan_seed.grid(
            row=1,
            column=2,
            padx=5,
            pady=7,
            sticky="e"
        )

        self.__o_seed = tk.Entry(
            self.__khung_tao_de,
            font=("Arial", 11),
            width=22
        )

        self.__o_seed.grid(
            row=1,
            column=3,
            padx=5,
            pady=7,
            sticky="we"
        )

        self.__o_seed.insert(
            0,
            "2026"
        )

        nhan_so_cau_de = tk.Label(
            self.__khung_tao_de,
            text="Số câu Dễ:",
            font=("Arial", 11)
        )

        nhan_so_cau_de.grid(
            row=2,
            column=0,
            padx=5,
            pady=7,
            sticky="e"
        )

        self.__o_so_cau_de = tk.Entry(
            self.__khung_tao_de,
            font=("Arial", 11),
            width=30
        )

        self.__o_so_cau_de.grid(
            row=2,
            column=1,
            padx=5,
            pady=7,
            sticky="we"
        )

        self.__o_so_cau_de.insert(
            0,
            "2"
        )

        nhan_so_cau_trung_binh = tk.Label(
            self.__khung_tao_de,
            text="Số câu Trung bình:",
            font=("Arial", 11)
        )

        nhan_so_cau_trung_binh.grid(
            row=2,
            column=2,
            padx=5,
            pady=7,
            sticky="e"
        )

        self.__o_so_cau_trung_binh = tk.Entry(
            self.__khung_tao_de,
            font=("Arial", 11),
            width=22
        )

        self.__o_so_cau_trung_binh.grid(
            row=2,
            column=3,
            padx=5,
            pady=7,
            sticky="we"
        )

        self.__o_so_cau_trung_binh.insert(
            0,
            "2"
        )

        nhan_so_cau_kho = tk.Label(
            self.__khung_tao_de,
            text="Số câu Khó:",
            font=("Arial", 11)
        )

        nhan_so_cau_kho.grid(
            row=3,
            column=0,
            padx=5,
            pady=7,
            sticky="e"
        )

        self.__o_so_cau_kho = tk.Entry(
            self.__khung_tao_de,
            font=("Arial", 11),
            width=30
        )

        self.__o_so_cau_kho.grid(
            row=3,
            column=1,
            padx=5,
            pady=7,
            sticky="we"
        )

        self.__o_so_cau_kho.insert(
            0,
            "1"
        )

        self.__nhan_tong_so_cau = tk.Label(
            self.__khung_tao_de,
            text="Tổng số câu: 5",
            font=("Arial", 11, "bold"),
            fg="#00695C"
        )

        self.__nhan_tong_so_cau.grid(
            row=3,
            column=2,
            columnspan=2,
            padx=5,
            pady=7
        )

        for o_nhap in (
            self.__o_so_cau_de,
            self.__o_so_cau_trung_binh,
            self.__o_so_cau_kho
        ):
            o_nhap.bind(
                "<KeyRelease>",
                self.__cap_nhat_tong_so_cau
            )

        nut_tao_de = tk.Button(
            self.__khung_tao_de,
            text="Tạo đề tự động",
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            command=self.__xu_ly_tao_de_thi
        )

        nut_tao_de.grid(
            row=4,
            column=0,
            columnspan=4,
            pady=(8, 2)
        )

        self.__khung_tao_de.columnconfigure(
            1,
            weight=1
        )

        self.__khung_tao_de.columnconfigure(
            3,
            weight=1
        )

        self.__khung_nut = tk.Frame(
            self.__cua_so
        )

        self.__khung_nut.pack(
            pady=5
        )

        nut_dong_mo = tk.Button(
            self.__khung_nut,
            text="Đóng/Mở đề",
            font=("Arial", 11, "bold"),
            bg="#FF9800",
            fg="white",
            width=16,
            command=self.__xu_ly_doi_trang_thai
        )

        nut_dong_mo.pack(
            side="left",
            padx=5
        )

        nut_xoa = tk.Button(
            self.__khung_nut,
            text="Xóa đề",
            font=("Arial", 11, "bold"),
            bg="#F44336",
            fg="white",
            width=16,
            command=self.__xu_ly_xoa_de_thi
        )

        nut_xoa.pack(
            side="left",
            padx=5
        )

        nut_lam_moi = tk.Button(
            self.__khung_nut,
            text="Làm mới",
            font=("Arial", 11, "bold"),
            bg="#2196F3",
            fg="white",
            width=16,
            command=self.__hien_thi_danh_sach_de_thi
        )

        nut_lam_moi.pack(
            side="left",
            padx=5
        )

        nut_quay_lai = tk.Button(
            self.__khung_nut,
            text="Quay lại",
            font=("Arial", 11, "bold"),
            bg="#607D8B",
            fg="white",
            width=16,
            command=self.__dong_cua_so
        )

        nut_quay_lai.pack(
            side="left",
            padx=5
        )

        self.__khung_bang = tk.Frame(
            self.__cua_so,
            padx=20,
            pady=10
        )

        self.__khung_bang.pack(
            fill="both",
            expand=True
        )

        cac_cot = (
            "ma_de_thi",
            "ten_de_thi",
            "mon_hoc",
            "thoi_gian",
            "so_cau",
            "ma_tran",
            "seed",
            "trang_thai"
        )

        self.__bang_de_thi = ttk.Treeview(
            self.__khung_bang,
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

        self.__bang_de_thi.heading(
            "ma_tran",
            text="Ma trận D/TB/K"
        )

        self.__bang_de_thi.heading(
            "seed",
            text="Seed"
        )

        self.__bang_de_thi.heading(
            "trang_thai",
            text="Trạng thái"
        )

        self.__bang_de_thi.column(
            "ma_de_thi",
            width=80,
            anchor="center"
        )

        self.__bang_de_thi.column(
            "ten_de_thi",
            width=240
        )

        self.__bang_de_thi.column(
            "mon_hoc",
            width=120,
            anchor="center"
        )

        self.__bang_de_thi.column(
            "thoi_gian",
            width=90,
            anchor="center"
        )

        self.__bang_de_thi.column(
            "so_cau",
            width=70,
            anchor="center"
        )

        self.__bang_de_thi.column(
            "ma_tran",
            width=130,
            anchor="center"
        )

        self.__bang_de_thi.column(
            "seed",
            width=90,
            anchor="center"
        )

        self.__bang_de_thi.column(
            "trang_thai",
            width=90,
            anchor="center"
        )

        thanh_cuon = ttk.Scrollbar(
            self.__khung_bang,
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

        self.__o_ten_de_thi.focus_set()

    def __cap_nhat_tong_so_cau(self, su_kien=None):
        try:
            so_cau_de = int(
                self.__o_so_cau_de.get()
            )

            so_cau_trung_binh = int(
                self.__o_so_cau_trung_binh.get()
            )

            so_cau_kho = int(
                self.__o_so_cau_kho.get()
            )

            if (
                so_cau_de < 0
                or so_cau_trung_binh < 0
                or so_cau_kho < 0
            ):
                raise ValueError

            tong_so_cau = (
                so_cau_de
                + so_cau_trung_binh
                + so_cau_kho
            )

            noi_dung = (
                "Tổng số câu: "
                + str(tong_so_cau)
            )

        except ValueError:
            noi_dung = "Tổng số câu: chưa hợp lệ"

        self.__nhan_tong_so_cau.config(
            text=noi_dung
        )

    def __tao_chuoi_ma_tran(self, de_thi):
        ma_tran = de_thi.ma_tran_muc_do

        so_cau_de = ma_tran.get("Dễ", 0)
        so_cau_trung_binh = ma_tran.get(
            "Trung bình",
            0
        )
        so_cau_kho = ma_tran.get("Khó", 0)

        tong_so_cau = (
            so_cau_de
            + so_cau_trung_binh
            + so_cau_kho
        )

        if tong_so_cau == 0:
            return "Chưa lưu"

        return (
            str(so_cau_de)
            + "/"
            + str(so_cau_trung_binh)
            + "/"
            + str(so_cau_kho)
        )

    def __hien_thi_danh_sach_de_thi(self):
        cac_dong_cu = (
            self.__bang_de_thi.get_children()
        )

        for dong in cac_dong_cu:
            self.__bang_de_thi.delete(dong)

        danh_sach = (
            self.__quan_ly_de_thi
            .lay_danh_sach_de_thi()
        )

        for de_thi in danh_sach:
            self.__bang_de_thi.insert(
                "",
                "end",
                values=(
                    de_thi.ma_de_thi,
                    de_thi.ten_de_thi,
                    de_thi.mon_hoc,
                    (
                        str(de_thi.thoi_gian_lam_bai)
                        + " phút"
                    ),
                    de_thi.so_luong_cau_hoi,
                    self.__tao_chuoi_ma_tran(
                        de_thi
                    ),
                    de_thi.seed,
                    de_thi.trang_thai
                )
            )

    def __xu_ly_tao_de_thi(self):
        ten_de_thi = (
            self.__o_ten_de_thi
            .get()
            .strip()
        )

        mon_hoc = (
            self.__o_mon_hoc
            .get()
            .strip()
        )

        thoi_gian = (
            self.__o_thoi_gian
            .get()
            .strip()
        )

        so_cau_de = (
            self.__o_so_cau_de
            .get()
            .strip()
        )

        so_cau_trung_binh = (
            self.__o_so_cau_trung_binh
            .get()
            .strip()
        )

        so_cau_kho = (
            self.__o_so_cau_kho
            .get()
            .strip()
        )

        seed = (
            self.__o_seed
            .get()
            .strip()
        )

        de_thi_moi, thong_bao = (
            self.__quan_ly_de_thi
            .tao_de_thi_tu_dong(
                ten_de_thi,
                mon_hoc,
                thoi_gian,
                so_cau_de,
                so_cau_trung_binh,
                so_cau_kho,
                seed
            )
        )

        if de_thi_moi is None:
            messagebox.showerror(
                "Không thể tạo đề",
                thong_bao,
                parent=self.__cua_so
            )

            return

        ma_tran = de_thi_moi.ma_tran_muc_do

        messagebox.showinfo(
            "Tạo đề thành công",
            (
                thong_bao
                + "\nMã đề: "
                + de_thi_moi.ma_de_thi
                + "\nSố câu Dễ: "
                + str(ma_tran.get("Dễ", 0))
                + "\nSố câu Trung bình: "
                + str(
                    ma_tran.get(
                        "Trung bình",
                        0
                    )
                )
                + "\nSố câu Khó: "
                + str(ma_tran.get("Khó", 0))
                + "\nTổng số câu: "
                + str(de_thi_moi.so_luong_cau_hoi)
                + "\nSeed: "
                + str(de_thi_moi.seed)
            ),
            parent=self.__cua_so
        )

        self.__o_ten_de_thi.delete(
            0,
            tk.END
        )

        self.__o_ten_de_thi.focus_set()
        self.__hien_thi_danh_sach_de_thi()

    def __lay_ma_de_thi_duoc_chon(self):
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

        return du_lieu[0]

    def __xu_ly_doi_trang_thai(self):
        ma_de_thi = (
            self.__lay_ma_de_thi_duoc_chon()
        )

        if ma_de_thi is None:
            return

        de_thi = (
            self.__quan_ly_de_thi
            .tim_de_thi_theo_ma(ma_de_thi)
        )

        if de_thi is None:
            messagebox.showerror(
                "Lỗi",
                "Không tìm thấy đề thi",
                parent=self.__cua_so
            )
            return

        if de_thi.trang_thai == "Mở":
            trang_thai_moi = "Đóng"
        else:
            trang_thai_moi = "Mở"

        xac_nhan = messagebox.askyesno(
            "Xác nhận",
            (
                "Bạn có muốn chuyển đề "
                + ma_de_thi
                + " sang trạng thái "
                + trang_thai_moi
                + " không?"
            ),
            parent=self.__cua_so
        )

        if not xac_nhan:
            return

        thanh_cong, thong_bao = (
            self.__quan_ly_de_thi
            .cap_nhat_trang_thai(
                ma_de_thi,
                trang_thai_moi
            )
        )

        if thanh_cong:
            messagebox.showinfo(
                "Thành công",
                thong_bao,
                parent=self.__cua_so
            )
            self.__hien_thi_danh_sach_de_thi()
        else:
            messagebox.showerror(
                "Không thành công",
                thong_bao,
                parent=self.__cua_so
            )

    def __xu_ly_xoa_de_thi(self):
        ma_de_thi = (
            self.__lay_ma_de_thi_duoc_chon()
        )

        if ma_de_thi is None:
            return

        de_thi = (
            self.__quan_ly_de_thi
            .tim_de_thi_theo_ma(ma_de_thi)
        )

        if de_thi is None:
            messagebox.showerror(
                "Lỗi",
                "Không tìm thấy đề thi",
                parent=self.__cua_so
            )
            return

        xac_nhan = messagebox.askyesno(
            "Xác nhận xóa",
            (
                "Bạn có chắc muốn xóa đề:\n"
                + de_thi.ten_de_thi
                + "\nMã đề: "
                + de_thi.ma_de_thi
                + "?"
            ),
            parent=self.__cua_so
        )

        if not xac_nhan:
            return

        thanh_cong, thong_bao = (
            self.__quan_ly_de_thi
            .xoa_de_thi(ma_de_thi)
        )

        if thanh_cong:
            messagebox.showinfo(
                "Thành công",
                thong_bao,
                parent=self.__cua_so
            )
            self.__hien_thi_danh_sach_de_thi()
        else:
            messagebox.showerror(
                "Không thành công",
                thong_bao,
                parent=self.__cua_so
            )

    def __dong_cua_so(self):
        self.__cua_so.destroy()
        self.__ham_quay_lai()
