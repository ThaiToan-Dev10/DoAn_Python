import tkinter as tk
from tkinter import ttk, messagebox

from managers.quan_ly_de_thi import QuanLyDeThi


class GiaoDienChiTietKetQua:
    def __init__(
        self,
        cua_so_cha,
        quan_ly_ket_qua,
        ma_ket_qua,
        quan_ly_de_thi=None
    ):
        self.__cua_so_cha = cua_so_cha
        self.__quan_ly_ket_qua = (
            quan_ly_ket_qua
        )
        self.__ma_ket_qua = ma_ket_qua

        self.__ket_qua = (
            self.__quan_ly_ket_qua
            .tim_ket_qua_theo_ma(
                self.__ma_ket_qua
            )
        )

        if self.__ket_qua is None:
            messagebox.showerror(
                "Không tìm thấy kết quả",
                "Kết quả thi này không tồn tại",
                parent=self.__cua_so_cha
            )
            return

        if quan_ly_de_thi is None:
            self.__quan_ly_de_thi = (
                QuanLyDeThi()
            )
        else:
            self.__quan_ly_de_thi = (
                quan_ly_de_thi
            )

        self.__de_thi = (
            self.__quan_ly_de_thi
            .tim_de_thi_theo_ma(
                self.__ket_qua.ma_de_thi
            )
        )

        (
            self.__danh_sach_chi_tiet,
            thong_bao
        ) = (
            self.__quan_ly_ket_qua
            .lay_chi_tiet_bai_lam(
                self.__ma_ket_qua
            )
        )

        if self.__danh_sach_chi_tiet is None:
            messagebox.showerror(
                "Không thể xem đáp án",
                thong_bao,
                parent=self.__cua_so_cha
            )
            return

        self.__tao_cua_so()
        self.__tao_giao_dien()

    def __tao_cua_so(self):
        self.__cua_so = tk.Toplevel(
            self.__cua_so_cha
        )

        self.__cua_so.title(
            "Chi tiết bài làm"
        )

        self.__cua_so.geometry(
            "950x700"
        )

        self.__cua_so.minsize(
            800,
            600
        )

        self.__cua_so.transient(
            self.__cua_so_cha
        )

        self.__cua_so.grab_set()

    def __tao_giao_dien(self):
        tieu_de = tk.Label(
            self.__cua_so,
            text="CHI TIẾT BÀI LÀM",
            font=("Arial", 20, "bold"),
            fg="blue"
        )

        tieu_de.pack(pady=(15, 5))

        thong_tin = tk.Label(
            self.__cua_so,
            text=(
                "Mã kết quả: "
                + self.__ket_qua.ma_ket_qua
                + "   |   Mã đề: "
                + self.__ket_qua.ma_de_thi
                + "   |   Điểm: "
                + str(self.__ket_qua.diem)
                + "   |   Số câu đúng: "
                + str(self.__ket_qua.so_cau_dung)
                + "/"
                + str(self.__ket_qua.tong_so_cau)
                + self.__tao_noi_dung_seed()
            ),
            font=("Arial", 11, "bold")
        )

        thong_tin.pack(pady=(0, 10))

        chu_thich = tk.Label(
            self.__cua_so,
            text=(
                "Màu xanh: đáp án đúng   |   "
                "Màu đỏ: đáp án bạn chọn sai"
            ),
            font=("Arial", 10),
            fg="#555555"
        )

        chu_thich.pack(pady=(0, 8))

        khung_cuon = tk.Frame(
            self.__cua_so
        )

        khung_cuon.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        self.__khung_canvas = tk.Canvas(
            khung_cuon,
            highlightthickness=0
        )

        thanh_cuon = ttk.Scrollbar(
            khung_cuon,
            orient="vertical",
            command=self.__khung_canvas.yview
        )

        self.__khung_noi_dung = tk.Frame(
            self.__khung_canvas
        )

        self.__ma_cua_so_noi_dung = (
            self.__khung_canvas.create_window(
                (0, 0),
                window=self.__khung_noi_dung,
                anchor="nw"
            )
        )

        self.__khung_noi_dung.bind(
            "<Configure>",
            self.__cap_nhat_vung_cuon
        )

        self.__khung_canvas.bind(
            "<Configure>",
            self.__cap_nhat_chieu_rong
        )

        self.__khung_canvas.configure(
            yscrollcommand=thanh_cuon.set
        )

        self.__khung_canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        thanh_cuon.pack(
            side="right",
            fill="y"
        )

        self.__hien_thi_cac_cau_hoi()

        nut_dong = tk.Button(
            self.__cua_so,
            text="Đóng",
            font=("Arial", 11, "bold"),
            bg="#607D8B",
            fg="white",
            width=14,
            command=self.__cua_so.destroy
        )

        nut_dong.pack(pady=15)

    def __tao_noi_dung_seed(self):
        if self.__de_thi is None:
            return ""

        return (
            "   |   Seed: "
            + str(self.__de_thi.seed)
        )

    def __cap_nhat_vung_cuon(self, su_kien):
        self.__khung_canvas.configure(
            scrollregion=(
                self.__khung_canvas.bbox("all")
            )
        )

    def __cap_nhat_chieu_rong(self, su_kien):
        self.__khung_canvas.itemconfigure(
            self.__ma_cua_so_noi_dung,
            width=su_kien.width
        )

    def __hien_thi_cac_cau_hoi(self):
        if len(self.__danh_sach_chi_tiet) == 0:
            thong_bao = tk.Label(
                self.__khung_noi_dung,
                text=(
                    "Kết quả này không có dữ liệu "
                    "câu trả lời để xem lại"
                ),
                font=("Arial", 12),
                fg="red"
            )

            thong_bao.pack(pady=30)
            return

        so_thu_tu = 1

        for chi_tiet in self.__danh_sach_chi_tiet:
            self.__tao_khung_cau_hoi(
                so_thu_tu,
                chi_tiet
            )

            so_thu_tu += 1

    def __lay_thu_tu_phuong_an(
        self,
        ma_cau_hoi
    ):
        if self.__de_thi is None:
            return ["A", "B", "C", "D"]

        return (
            self.__de_thi
            .lay_thu_tu_phuong_an(
                ma_cau_hoi
            )
        )

    def __chuyen_dap_an_goc_sang_hien_thi(
        self,
        ma_cau_hoi,
        dap_an_goc
    ):
        dap_an_goc = str(
            dap_an_goc
        ).strip().upper()

        if dap_an_goc == "":
            return ""

        if self.__de_thi is None:
            return dap_an_goc

        return (
            self.__de_thi
            .chuyen_dap_an_goc_sang_hien_thi(
                ma_cau_hoi,
                dap_an_goc
            )
        )

    def __tao_khung_cau_hoi(
        self,
        so_thu_tu,
        chi_tiet
    ):
        khung_cau_hoi = tk.Frame(
            self.__khung_noi_dung,
            bd=1,
            relief="solid",
            padx=15,
            pady=12
        )

        khung_cau_hoi.pack(
            fill="x",
            padx=5,
            pady=8
        )

        cau_hoi = chi_tiet["cau_hoi"]

        if cau_hoi is None:
            dap_an_hien_thi = (
                self.__chuyen_dap_an_goc_sang_hien_thi(
                    chi_tiet["ma_cau_hoi"],
                    chi_tiet[
                        "dap_an_nguoi_dung"
                    ]
                )
            )

            tk.Label(
                khung_cau_hoi,
                text=(
                    "Câu "
                    + str(so_thu_tu)
                    + ": Câu hỏi "
                    + chi_tiet["ma_cau_hoi"]
                    + " đã bị xóa khỏi ngân hàng câu hỏi"
                ),
                font=("Arial", 11, "bold"),
                fg="red",
                anchor="w",
                justify="left"
            ).pack(fill="x")

            tk.Label(
                khung_cau_hoi,
                text=(
                    "Đáp án bạn đã chọn: "
                    + self.__hien_thi_dap_an(
                        dap_an_hien_thi
                    )
                ),
                font=("Arial", 10),
                anchor="w"
            ).pack(fill="x", pady=(8, 0))

            return

        tk.Label(
            khung_cau_hoi,
            text=(
                "Câu "
                + str(so_thu_tu)
                + ": "
                + cau_hoi.noi_dung
            ),
            font=("Arial", 11, "bold"),
            anchor="w",
            justify="left",
            wraplength=820
        ).pack(fill="x", pady=(0, 8))

        cac_phuong_an_goc = {
            "A": cau_hoi.phuong_an_a,
            "B": cau_hoi.phuong_an_b,
            "C": cau_hoi.phuong_an_c,
            "D": cau_hoi.phuong_an_d
        }

        thu_tu_phuong_an = (
            self.__lay_thu_tu_phuong_an(
                cau_hoi.ma_cau_hoi
            )
        )

        cac_ky_tu_hien_thi = (
            "A",
            "B",
            "C",
            "D"
        )

        dap_an_nguoi_dung_hien_thi = (
            self.__chuyen_dap_an_goc_sang_hien_thi(
                cau_hoi.ma_cau_hoi,
                chi_tiet[
                    "dap_an_nguoi_dung"
                ]
            )
        )

        dap_an_dung_hien_thi = (
            self.__chuyen_dap_an_goc_sang_hien_thi(
                cau_hoi.ma_cau_hoi,
                chi_tiet["dap_an_dung"]
            )
        )

        for vi_tri in range(4):
            ky_tu_hien_thi = (
                cac_ky_tu_hien_thi[vi_tri]
            )

            ky_tu_goc = (
                thu_tu_phuong_an[vi_tri]
            )

            noi_dung = cac_phuong_an_goc.get(
                ky_tu_goc,
                ""
            )

            mau_nen = "#F5F5F5"
            mau_chu = "black"
            ghi_chu = ""

            if (
                ky_tu_hien_thi
                == dap_an_dung_hien_thi
            ):
                mau_nen = "#C8E6C9"
                mau_chu = "#1B5E20"
                ghi_chu = "  ← Đáp án đúng"

            if (
                ky_tu_hien_thi
                == dap_an_nguoi_dung_hien_thi
            ):
                if (
                    ky_tu_hien_thi
                    == dap_an_dung_hien_thi
                ):
                    mau_nen = "#A5D6A7"
                    mau_chu = "#1B5E20"
                    ghi_chu = (
                        "  ← Bạn đã chọn (Đúng)"
                    )
                else:
                    mau_nen = "#FFCDD2"
                    mau_chu = "#B71C1C"
                    ghi_chu = (
                        "  ← Bạn đã chọn (Sai)"
                    )

            tk.Label(
                khung_cau_hoi,
                text=(
                    ky_tu_hien_thi
                    + ". "
                    + str(noi_dung)
                    + ghi_chu
                ),
                font=("Arial", 10),
                bg=mau_nen,
                fg=mau_chu,
                anchor="w",
                justify="left",
                wraplength=800,
                padx=8,
                pady=5
            ).pack(
                fill="x",
                pady=2
            )

        if dap_an_nguoi_dung_hien_thi == "":
            noi_dung_ket_qua = (
                "Bạn chưa trả lời câu này"
            )
            mau_ket_qua = "#E65100"
        elif chi_tiet["tra_loi_dung"]:
            noi_dung_ket_qua = (
                "Kết quả câu này: Đúng"
            )
            mau_ket_qua = "green"
        else:
            noi_dung_ket_qua = (
                "Kết quả câu này: Sai"
            )
            mau_ket_qua = "red"

        tk.Label(
            khung_cau_hoi,
            text=noi_dung_ket_qua,
            font=("Arial", 10, "bold"),
            fg=mau_ket_qua,
            anchor="w"
        ).pack(fill="x", pady=(8, 0))

    def __hien_thi_dap_an(self, dap_an):
        dap_an = str(dap_an).strip().upper()

        if dap_an == "":
            return "Chưa trả lời"

        return dap_an
