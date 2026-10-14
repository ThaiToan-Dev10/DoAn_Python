import tkinter as tk
from tkinter import messagebox, ttk, simpledialog

from managers.quan_ly_cau_hoi import (
    DAP_AN_HOP_LE,
    MUC_DO_HOP_LE
)


MON_HOC_GOI_Y = (
    "Toán",
    "Tin học",
    "Vật lý",
    "Hóa học",
    "Ngữ văn",
    "Tiếng Anh"
)

CHU_DE_GOI_Y = (
    "Python cơ bản",
    "Lập trình hướng đối tượng",
    "Cấu trúc dữ liệu",
    "Thuật toán",
    "Cơ sở dữ liệu",
    "Mạng máy tính",
    "Đại số",
    "Hình học",
    "Cơ học",
    "Điện học",
    "Ngữ pháp",
    "Từ vựng"
)


class GiaoDienQuanLyCauHoi:
    def __init__(
        self,
        cua_so_cha,
        quan_ly_cau_hoi,
        ham_quay_lai
    ):
        self.__cua_so_cha = cua_so_cha
        self.__quan_ly_cau_hoi = quan_ly_cau_hoi
        self.__ham_quay_lai = ham_quay_lai
        self.__ma_cau_hoi_dang_chon = None

        self.__cua_so = tk.Toplevel(
            self.__cua_so_cha
        )
        self.__cua_so.title("Quản lý câu hỏi trắc nghiệm")
        self.__cua_so.geometry("1250x760")
        self.__cua_so.minsize(1000, 650)

        self.__cua_so.protocol(
            "WM_DELETE_WINDOW",
            self.__dong_cua_so
        )

        self.__tao_giao_dien()
        self.__cap_nhat_bo_loc()
        self.__hien_thi_danh_sach()

    def __tao_giao_dien(self):
        self.__tao_khung_tim_kiem()
        self.__tao_bang_cau_hoi()
        self.__tao_form_cau_hoi()

        self.__noi_dung_trang_thai = tk.StringVar()

        ttk.Label(
            self.__cua_so,
            textvariable=self.__noi_dung_trang_thai,
            anchor="w"
        ).pack(
            fill="x",
            padx=12,
            pady=(0, 8)
        )

    def __tao_khung_tim_kiem(self):
        khung_tim_kiem = ttk.LabelFrame(
            self.__cua_so,
            text="Tìm kiếm và lọc"
        )

        khung_tim_kiem.pack(
            fill="x",
            padx=10,
            pady=(10, 5)
        )

        ttk.Label(
            khung_tim_kiem,
            text="Từ khóa (mã/nội dung):"
        ).grid(row=0, column=0, padx=5, pady=7)

        self.__tu_khoa = tk.StringVar()

        o_tim_kiem = ttk.Entry(
            khung_tim_kiem,
            textvariable=self.__tu_khoa,
            width=25
        )

        o_tim_kiem.grid(
            row=0,
            column=1,
            padx=5,
            pady=7,
            sticky="ew"
        )

        o_tim_kiem.bind(
            "<KeyRelease>",
            lambda su_kien: self.__hien_thi_danh_sach()
        )

        ttk.Label(
            khung_tim_kiem,
            text="Môn học:"
        ).grid(row=0, column=2, padx=5)

        self.__loc_mon_hoc = tk.StringVar(value="Tất cả")
        self.__hop_loc_mon_hoc = ttk.Combobox(
            khung_tim_kiem,
            textvariable=self.__loc_mon_hoc,
            state="readonly",
            width=15
        )

        self.__hop_loc_mon_hoc.grid(
            row=0,
            column=3,
            padx=5,
            pady=7
        )

        self.__hop_loc_mon_hoc.bind(
            "<<ComboboxSelected>>",
            lambda su_kien: self.__hien_thi_danh_sach()
        )

        ttk.Label(
            khung_tim_kiem,
            text="Chủ đề:"
        ).grid(row=0, column=4, padx=5)

        self.__loc_chu_de = tk.StringVar(value="Tất cả")
        self.__hop_loc_chu_de = ttk.Combobox(
            khung_tim_kiem,
            textvariable=self.__loc_chu_de,
            state="readonly",
            width=22
        )

        self.__hop_loc_chu_de.grid(
            row=0,
            column=5,
            padx=5,
            pady=7
        )

        self.__hop_loc_chu_de.bind(
            "<<ComboboxSelected>>",
            lambda su_kien: self.__hien_thi_danh_sach()
        )

        ttk.Label(
            khung_tim_kiem,
            text="Mức độ:"
        ).grid(row=0, column=6, padx=5)

        self.__loc_muc_do = tk.StringVar(value="Tất cả")
        hop_loc_muc_do = ttk.Combobox(
            khung_tim_kiem,
            textvariable=self.__loc_muc_do,
            values=("Tất cả",) + MUC_DO_HOP_LE,
            state="readonly",
            width=13
        )

        hop_loc_muc_do.grid(
            row=0,
            column=7,
            padx=5,
            pady=7
        )

        hop_loc_muc_do.bind(
            "<<ComboboxSelected>>",
            lambda su_kien: self.__hien_thi_danh_sach()
        )

        ttk.Button(
            khung_tim_kiem,
            text="Xóa bộ lọc",
            command=self.__xoa_bo_loc
        ).grid(row=0, column=8, padx=7, pady=7)

        khung_tim_kiem.columnconfigure(1, weight=1)

    def __tao_bang_cau_hoi(self):
        khung_bang = ttk.LabelFrame(
            self.__cua_so,
            text="Danh sách câu hỏi"
        )

        khung_bang.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        ten_cot = (
            "ma",
            "mon",
            "chu_de",
            "muc_do",
            "noi_dung",
            "dap_an",
            "nguon"
        )

        self.__bang_cau_hoi = ttk.Treeview(
            khung_bang,
            columns=ten_cot,
            show="headings",
            selectmode="browse"
        )

        tieu_de_cot = {
            "ma": ("Mã câu hỏi", 100),
            "mon": ("Môn học", 100),
            "chu_de": ("Chủ đề", 150),
            "muc_do": ("Mức độ", 95),
            "noi_dung": ("Nội dung", 370),
            "dap_an": ("Đáp án", 70),
            "nguon": ("Nguồn", 180)
        }

        for ten, thong_tin in tieu_de_cot.items():
            nhan, do_rong = thong_tin
            self.__bang_cau_hoi.heading(ten, text=nhan)
            self.__bang_cau_hoi.column(
                ten,
                width=do_rong,
                minwidth=60,
                anchor="w"
            )

        thanh_cuon_doc = ttk.Scrollbar(
            khung_bang,
            orient="vertical",
            command=self.__bang_cau_hoi.yview
        )

        thanh_cuon_ngang = ttk.Scrollbar(
            khung_bang,
            orient="horizontal",
            command=self.__bang_cau_hoi.xview
        )

        self.__bang_cau_hoi.configure(
            yscrollcommand=thanh_cuon_doc.set,
            xscrollcommand=thanh_cuon_ngang.set
        )

        self.__bang_cau_hoi.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        thanh_cuon_doc.grid(row=0, column=1, sticky="ns")
        thanh_cuon_ngang.grid(row=1, column=0, sticky="ew")

        khung_bang.rowconfigure(0, weight=1)
        khung_bang.columnconfigure(0, weight=1)

        self.__bang_cau_hoi.bind(
            "<<TreeviewSelect>>",
            self.__chon_cau_hoi
        )

    def __tao_form_cau_hoi(self):
        khung_form = ttk.LabelFrame(
            self.__cua_so,
            text="Thông tin câu hỏi"
        )

        khung_form.pack(fill="x", padx=10, pady=5)

        cac_truong = (
            "ma_cau_hoi",
            "mon_hoc",
            "chu_de",
            "muc_do",
            "phuong_an_a",
            "phuong_an_b",
            "phuong_an_c",
            "phuong_an_d",
            "dap_an_dung",
            "nguon_cau_hoi"
        )

        self.__bien_form = {
            truong: tk.StringVar()
            for truong in cac_truong
        }

        self.__tao_nhan_o_nhap(
            khung_form,
            "Mã câu hỏi *",
            "ma_cau_hoi",
            0,
            0
        )

        ttk.Label(
            khung_form,
            text="Môn học *"
        ).grid(row=0, column=2, padx=5, pady=5)

        ttk.Combobox(
            khung_form,
            textvariable=self.__bien_form["mon_hoc"],
            values=MON_HOC_GOI_Y,
            width=20
        ).grid(row=0, column=3, padx=5, pady=5, sticky="ew")

        ttk.Label(
            khung_form,
            text="Chủ đề *"
        ).grid(row=0, column=4, padx=5, pady=5)

        ttk.Combobox(
            khung_form,
            textvariable=self.__bien_form["chu_de"],
            values=CHU_DE_GOI_Y,
            width=24
        ).grid(row=0, column=5, padx=5, pady=5, sticky="ew")

        ttk.Label(
            khung_form,
            text="Mức độ *"
        ).grid(row=0, column=6, padx=5, pady=5)

        ttk.Combobox(
            khung_form,
            textvariable=self.__bien_form["muc_do"],
            values=MUC_DO_HOP_LE,
            state="readonly",
            width=15
        ).grid(row=0, column=7, padx=5, pady=5, sticky="ew")

        ttk.Label(
            khung_form,
            text="Nội dung *"
        ).grid(row=1, column=0, padx=5, pady=5, sticky="nw")

        self.__o_noi_dung = tk.Text(
            khung_form,
            height=3,
            width=50,
            wrap="word"
        )

        self.__o_noi_dung.grid(
            row=1,
            column=1,
            columnspan=7,
            padx=5,
            pady=5,
            sticky="ew"
        )

        cac_phuong_an = (
            ("Phương án A *", "phuong_an_a"),
            ("Phương án B *", "phuong_an_b"),
            ("Phương án C *", "phuong_an_c"),
            ("Phương án D *", "phuong_an_d")
        )

        for chi_so, thong_tin in enumerate(cac_phuong_an):
            nhan, ten_truong = thong_tin
            hang = 2 + chi_so // 2
            cot = (chi_so % 2) * 4

            self.__tao_nhan_o_nhap(
                khung_form,
                nhan,
                ten_truong,
                hang,
                cot,
                3
            )

        ttk.Label(
            khung_form,
            text="Đáp án đúng *"
        ).grid(row=4, column=0, padx=5, pady=5)

        ttk.Combobox(
            khung_form,
            textvariable=self.__bien_form["dap_an_dung"],
            values=DAP_AN_HOP_LE,
            state="readonly",
            width=15
        ).grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        self.__tao_nhan_o_nhap(
            khung_form,
            "Nguồn câu hỏi *",
            "nguon_cau_hoi",
            4,
            2,
            5
        )

        khung_nut = ttk.Frame(khung_form)
        khung_nut.grid(
            row=5,
            column=0,
            columnspan=8,
            padx=5,
            pady=8,
            sticky="w"
        )
        
        ttk.Button(
            khung_nut,
            text="Lấy câu hỏi từ API",
            command=self.__lay_cau_hoi_tu_api
        ).pack(
            side="left",
            padx=6
        )
        ttk.Button(
            khung_nut,
            text="Thêm câu hỏi",
            command=self.__them_cau_hoi
        ).pack(side="left", padx=6)

        ttk.Button(
            khung_nut,
            text="Cập nhật câu hỏi",
            command=self.__cap_nhat_cau_hoi
        ).pack(side="left", padx=6)

        ttk.Button(
            khung_nut,
            text="Xóa câu hỏi",
            command=self.__xoa_cau_hoi
        ).pack(side="left", padx=6)

        ttk.Button(
            khung_nut,
            text="Làm mới form",
            command=self.__lam_moi_form
        ).pack(side="left", padx=6)

        ttk.Button(
            khung_nut,
            text="Quay lại",
            command=self.__dong_cua_so
        ).pack(side="left", padx=6)

        for cot in (1, 3, 5, 7):
            khung_form.columnconfigure(cot, weight=1)

    def __tao_nhan_o_nhap(
        self,
        khung_cha,
        nhan,
        ten_truong,
        hang,
        cot,
        so_cot=1
    ):
        ttk.Label(
            khung_cha,
            text=nhan
        ).grid(row=hang, column=cot, padx=5, pady=5)

        ttk.Entry(
            khung_cha,
            textvariable=self.__bien_form[ten_truong]
        ).grid(
            row=hang,
            column=cot + 1,
            columnspan=so_cot,
            padx=5,
            pady=5,
            sticky="ew"
        )

    def __lay_du_lieu_form(self):
        du_lieu = {
            ten: bien.get().strip()
            for ten, bien in self.__bien_form.items()
        }

        du_lieu["noi_dung"] = self.__o_noi_dung.get(
            "1.0",
            "end-1c"
        ).strip()

        return du_lieu

    def __hien_thi_danh_sach(self):
        for dong in self.__bang_cau_hoi.get_children():
            self.__bang_cau_hoi.delete(dong)

        danh_sach = self.__quan_ly_cau_hoi.tim_kiem_va_loc(
            self.__tu_khoa.get(),
            self.__loc_mon_hoc.get(),
            self.__loc_chu_de.get(),
            self.__loc_muc_do.get()
        )

        for cau_hoi in danh_sach:
            self.__bang_cau_hoi.insert(
                "",
                "end",
                iid=cau_hoi.ma_cau_hoi,
                values=(
                    cau_hoi.ma_cau_hoi,
                    cau_hoi.mon_hoc,
                    cau_hoi.chu_de,
                    cau_hoi.muc_do,
                    cau_hoi.noi_dung,
                    cau_hoi.dap_an_dung,
                    cau_hoi.nguon_cau_hoi
                )
            )

        tong_so = len(
            self.__quan_ly_cau_hoi.lay_danh_sach_cau_hoi()
        )

        self.__noi_dung_trang_thai.set(
            "Tổng số câu hỏi: "
            + str(tong_so)
            + " | Đang hiển thị: "
            + str(len(danh_sach))
        )

    def __cap_nhat_bo_loc(self):
        danh_sach = (
            self.__quan_ly_cau_hoi.lay_danh_sach_cau_hoi()
        )

        cac_mon_hoc = sorted({
            cau_hoi.mon_hoc
            for cau_hoi in danh_sach
        })

        cac_chu_de = sorted({
            cau_hoi.chu_de
            for cau_hoi in danh_sach
        })

        self.__hop_loc_mon_hoc["values"] = (
            "Tất cả",
            *cac_mon_hoc
        )

        self.__hop_loc_chu_de["values"] = (
            "Tất cả",
            *cac_chu_de
        )

        if self.__loc_mon_hoc.get() not in (
            "Tất cả",
            *cac_mon_hoc
        ):
            self.__loc_mon_hoc.set("Tất cả")

        if self.__loc_chu_de.get() not in (
            "Tất cả",
            *cac_chu_de
        ):
            self.__loc_chu_de.set("Tất cả")

    def __chon_cau_hoi(self, su_kien=None):
        cac_dong_da_chon = self.__bang_cau_hoi.selection()

        if len(cac_dong_da_chon) == 0:
            return

        ma_cau_hoi = cac_dong_da_chon[0]
        cau_hoi = self.__quan_ly_cau_hoi.tim_cau_hoi_theo_ma(
            ma_cau_hoi
        )

        if cau_hoi is None:
            return

        self.__ma_cau_hoi_dang_chon = cau_hoi.ma_cau_hoi

        for ten_truong, bien in self.__bien_form.items():
            bien.set(getattr(cau_hoi, ten_truong))

        self.__o_noi_dung.delete("1.0", "end")
        self.__o_noi_dung.insert("1.0", cau_hoi.noi_dung)

    def __them_cau_hoi(self):
        ket_qua, thong_bao = (
            self.__quan_ly_cau_hoi.them_cau_hoi(
                self.__lay_du_lieu_form()
            )
        )

        if not ket_qua:
            messagebox.showwarning(
                "Dữ liệu chưa hợp lệ",
                thong_bao,
                parent=self.__cua_so
            )
            return

        self.__sau_khi_thay_doi_du_lieu()
        messagebox.showinfo(
            "Thành công",
            thong_bao,
            parent=self.__cua_so
        )

    def __dong_cua_so(self):
        self.__cua_so.destroy()
        self.__ham_quay_lai()

    def __cap_nhat_cau_hoi(self):
        if self.__ma_cau_hoi_dang_chon is None:
            messagebox.showwarning(
                "Chưa chọn câu hỏi",
                "Bạn phải chọn câu hỏi cần cập nhật",
                parent=self.__cua_so
            )
            return

        ket_qua, thong_bao = (
            self.__quan_ly_cau_hoi.cap_nhat_cau_hoi(
                self.__ma_cau_hoi_dang_chon,
                self.__lay_du_lieu_form()
            )
        )

        if not ket_qua:
            messagebox.showwarning(
                "Cập nhật thất bại",
                thong_bao,
                parent=self.__cua_so
            )
            return

        self.__sau_khi_thay_doi_du_lieu()
        messagebox.showinfo(
            "Thành công",
            thong_bao,
            parent=self.__cua_so
        )

    def __xoa_cau_hoi(self):
        if self.__ma_cau_hoi_dang_chon is None:
            messagebox.showwarning(
                "Chưa chọn câu hỏi",
                "Bạn phải chọn câu hỏi cần xóa",
                parent=self.__cua_so
            )
            return

        dong_y = messagebox.askyesno(
            "Xác nhận xóa",
            "Bạn có chắc muốn xóa câu hỏi "
            + self.__ma_cau_hoi_dang_chon
            + " không?",
            parent=self.__cua_so
        )

        if not dong_y:
            return

        ket_qua, thong_bao = (
            self.__quan_ly_cau_hoi.xoa_cau_hoi(
                self.__ma_cau_hoi_dang_chon
            )
        )

        if not ket_qua:
            messagebox.showerror(
                "Xóa thất bại",
                thong_bao,
                parent=self.__cua_so
            )
            return

        self.__sau_khi_thay_doi_du_lieu()
        messagebox.showinfo(
            "Thành công",
            thong_bao,
            parent=self.__cua_so
        )

    def __sau_khi_thay_doi_du_lieu(self):
        self.__lam_moi_form()
        self.__cap_nhat_bo_loc()
        self.__hien_thi_danh_sach()

    def __lam_moi_form(self):
        self.__ma_cau_hoi_dang_chon = None

        for bien in self.__bien_form.values():
            bien.set("")

        self.__o_noi_dung.delete("1.0", "end")

        for dong in self.__bang_cau_hoi.selection():
            self.__bang_cau_hoi.selection_remove(dong)

    def __xoa_bo_loc(self):
        self.__tu_khoa.set("")
        self.__loc_mon_hoc.set("Tất cả")
        self.__loc_chu_de.set("Tất cả")
        self.__loc_muc_do.set("Tất cả")
        self.__hien_thi_danh_sach()

    def __lay_cau_hoi_tu_api(self):
        so_luong = simpledialog.askinteger(
            "Lấy câu hỏi từ API",
            "Nhập số lượng câu hỏi muốn lấy:",
            parent=self.__cua_so,
            minvalue=1,
            maxvalue=10
        )

        if so_luong is None:
            return

        self.__noi_dung_trang_thai.set(
            "Đang lấy câu hỏi từ API..."
        )

        self.__cua_so.update_idletasks()

        ket_qua, thong_bao = (
            self.__quan_ly_cau_hoi
            .nhap_cau_hoi_tu_api(
                so_luong
            )
        )

        if not ket_qua:
            self.__hien_thi_danh_sach()

            messagebox.showerror(
                "Lấy câu hỏi thất bại",
                thong_bao,
                parent=self.__cua_so
            )

            return

        self.__sau_khi_thay_doi_du_lieu()

        messagebox.showinfo(
            "Thành công",
            thong_bao,
            parent=self.__cua_so
        )
