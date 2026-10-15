import tkinter as tk


class GiaoDienThongKe:
    def __init__(
        self,
        cua_so,
        quan_ly_thong_ke,
        ham_quay_lai
    ):
        self.__cua_so_cha = cua_so
        self.__quan_ly_thong_ke = (
            quan_ly_thong_ke
        )
        self.__ham_quay_lai = ham_quay_lai

        self.__cac_nhan_so_luong = {}
        self.__du_lieu_chu_de = {}

        self.__tao_giao_dien()

    def __tao_giao_dien(self):
        self.__cua_so_thong_ke = tk.Toplevel(
            self.__cua_so_cha
        )

        self.__cua_so_thong_ke.title(
            "Thống kê hệ thống"
        )

        self.__cua_so_thong_ke.geometry(
            "1000x720"
        )

        self.__cua_so_thong_ke.minsize(
            850,
            620
        )

        self.__cua_so_thong_ke.protocol(
            "WM_DELETE_WINDOW",
            self.__dong_cua_so
        )

        tieu_de = tk.Label(
            self.__cua_so_thong_ke,
            text="THỐNG KÊ HỆ THỐNG",
            font=("Arial", 20, "bold"),
            fg="blue"
        )

        tieu_de.pack(pady=(15, 10))

        khung_cac_o = tk.Frame(
            self.__cua_so_thong_ke
        )

        khung_cac_o.pack(
            fill="x",
            padx=20,
            pady=(0, 10)
        )

        self.__tao_o_thong_ke(
            khung_cac_o,
            "Tài khoản",
            "so_tai_khoan",
            0,
            "#1976D2"
        )

        self.__tao_o_thong_ke(
            khung_cac_o,
            "Câu hỏi",
            "so_cau_hoi",
            1,
            "#388E3C"
        )

        self.__tao_o_thong_ke(
            khung_cac_o,
            "Đề thi",
            "so_de_thi",
            2,
            "#F57C00"
        )

        self.__tao_o_thong_ke(
            khung_cac_o,
            "Kết quả thi",
            "so_ket_qua",
            3,
            "#7B1FA2"
        )

        for cot in range(4):
            khung_cac_o.columnconfigure(
                cot,
                weight=1
            )

        khung_bieu_do = tk.LabelFrame(
            self.__cua_so_thong_ke,
            text=(
                "BIỂU ĐỒ SỐ CÂU HỎI "
                "THEO CHỦ ĐỀ"
            ),
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )

        khung_bieu_do.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        khung_canvas = tk.Frame(
            khung_bieu_do
        )

        khung_canvas.pack(
            fill="both",
            expand=True
        )

        self.__canvas_bieu_do = tk.Canvas(
            khung_canvas,
            bg="white",
            height=350,
            highlightthickness=1,
            highlightbackground="#BDBDBD"
        )

        thanh_cuon = tk.Scrollbar(
            khung_canvas,
            orient="vertical",
            command=(
                self.__canvas_bieu_do.yview
            )
        )

        self.__canvas_bieu_do.configure(
            yscrollcommand=thanh_cuon.set
        )

        self.__canvas_bieu_do.pack(
            side="left",
            fill="both",
            expand=True
        )

        thanh_cuon.pack(
            side="right",
            fill="y"
        )

        self.__canvas_bieu_do.bind(
            "<Configure>",
            self.__khi_canvas_thay_doi_kich_thuoc
        )

        khung_nut = tk.Frame(
            self.__cua_so_thong_ke
        )

        khung_nut.pack(pady=15)

        nut_lam_moi = tk.Button(
            khung_nut,
            text="Làm mới",
            font=("Arial", 11, "bold"),
            bg="#2196F3",
            fg="white",
            width=12,
            command=self.__lam_moi_du_lieu
        )

        nut_lam_moi.pack(
            side="left",
            padx=5
        )

        nut_quay_lai = tk.Button(
            khung_nut,
            text="Quay lại",
            font=("Arial", 11, "bold"),
            bg="#607D8B",
            fg="white",
            width=12,
            command=self.__dong_cua_so
        )

        nut_quay_lai.pack(
            side="left",
            padx=5
        )

        self.__lam_moi_du_lieu()

    def __tao_o_thong_ke(
        self,
        khung_cha,
        ten_thong_ke,
        ma_thong_ke,
        cot,
        mau_nen
    ):
        khung = tk.Frame(
            khung_cha,
            width=205,
            height=100,
            bg=mau_nen,
            relief="ridge",
            bd=2
        )

        khung.grid(
            row=0,
            column=cot,
            padx=8,
            pady=5,
            sticky="nsew"
        )

        khung.grid_propagate(False)

        nhan_ten = tk.Label(
            khung,
            text=ten_thong_ke,
            font=("Arial", 12, "bold"),
            bg=mau_nen,
            fg="white"
        )

        nhan_ten.pack(pady=(15, 3))

        nhan_so_luong = tk.Label(
            khung,
            text="0",
            font=("Arial", 22, "bold"),
            bg=mau_nen,
            fg="white"
        )

        nhan_so_luong.pack()

        self.__cac_nhan_so_luong[
            ma_thong_ke
        ] = nhan_so_luong

    def __lam_moi_du_lieu(self):
        thong_ke_tong_quan = (
            self.__quan_ly_thong_ke
            .lay_thong_ke_tong_quan()
        )

        for (
            ma_thong_ke,
            nhan_so_luong
        ) in self.__cac_nhan_so_luong.items():
            so_luong = thong_ke_tong_quan.get(
                ma_thong_ke,
                0
            )

            nhan_so_luong.config(
                text=str(so_luong)
            )

        self.__du_lieu_chu_de = (
            self.__quan_ly_thong_ke
            .lay_thong_ke_cau_hoi_theo_chu_de()
        )

        self.__ve_bieu_do_chu_de()

    def __khi_canvas_thay_doi_kich_thuoc(
        self,
        su_kien
    ):
        self.__ve_bieu_do_chu_de()

    def __ve_bieu_do_chu_de(self):
        self.__canvas_bieu_do.delete("all")

        chieu_rong_canvas = max(
            self.__canvas_bieu_do.winfo_width(),
            760
        )

        if len(self.__du_lieu_chu_de) == 0:
            self.__canvas_bieu_do.configure(
                scrollregion=(
                    0,
                    0,
                    chieu_rong_canvas,
                    320
                )
            )

            self.__canvas_bieu_do.create_text(
                chieu_rong_canvas / 2,
                150,
                text=(
                    "Chưa có dữ liệu câu hỏi "
                    "để vẽ biểu đồ"
                ),
                font=("Arial", 12, "italic"),
                fill="#757575"
            )

            return

        so_chu_de = len(
            self.__du_lieu_chu_de
        )

        chieu_cao_moi_dong = 55
        le_tren = 35

        chieu_cao_noi_dung = max(
            320,
            (
                le_tren
                + so_chu_de
                * chieu_cao_moi_dong
                + 25
            )
        )

        self.__canvas_bieu_do.configure(
            scrollregion=(
                0,
                0,
                chieu_rong_canvas,
                chieu_cao_noi_dung
            )
        )

        so_luong_lon_nhat = max(
            self.__du_lieu_chu_de.values()
        )

        le_trai = 230
        le_phai = 70

        chieu_rong_toi_da = max(
            200,
            chieu_rong_canvas
            - le_trai
            - le_phai
        )

        cac_mau = (
            "#42A5F5",
            "#66BB6A",
            "#FFA726",
            "#AB47BC",
            "#26A69A",
            "#EF5350",
            "#5C6BC0",
            "#8D6E63"
        )

        vi_tri = 0

        for (
            chu_de,
            so_luong
        ) in self.__du_lieu_chu_de.items():
            y = (
                le_tren
                + vi_tri * chieu_cao_moi_dong
            )

            chieu_rong_cot = (
                so_luong
                / so_luong_lon_nhat
                * chieu_rong_toi_da
            )

            mau_cot = cac_mau[
                vi_tri % len(cac_mau)
            ]

            self.__canvas_bieu_do.create_text(
                le_trai - 12,
                y,
                text=chu_de,
                font=("Arial", 10),
                anchor="e",
                justify="right",
                width=200
            )

            self.__canvas_bieu_do.create_rectangle(
                le_trai,
                y - 14,
                le_trai + chieu_rong_cot,
                y + 14,
                fill=mau_cot,
                outline=""
            )

            self.__canvas_bieu_do.create_text(
                le_trai + chieu_rong_cot + 10,
                y,
                text=str(so_luong),
                font=("Arial", 10, "bold"),
                anchor="w",
                fill="#333333"
            )

            vi_tri += 1

    def __dong_cua_so(self):
        self.__cua_so_thong_ke.destroy()
        self.__ham_quay_lai()
