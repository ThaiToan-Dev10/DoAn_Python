import tkinter as tk
from tkinter import messagebox


class GiaoDienLamBai:
    def __init__(
        self,
        cua_so_cha,
        ten_dang_nhap,
        de_thi,
        quan_ly_cau_hoi,
        quan_ly_ket_qua
    ):
        self.__cua_so_cha = cua_so_cha
        self.__ten_dang_nhap = ten_dang_nhap
        self.__de_thi = de_thi

        self.__quan_ly_cau_hoi = (
            quan_ly_cau_hoi
        )

        self.__quan_ly_ket_qua = (
            quan_ly_ket_qua
        )

        self.__danh_sach_cau_hoi = []
        self.__cau_tra_loi = {}
        self.__vi_tri_hien_tai = 0
        self.__da_nop_bai = False
        self.__ma_hen_gio = None

        thanh_cong, thong_bao = (
            self.__tai_danh_sach_cau_hoi()
        )

        if not thanh_cong:
            messagebox.showerror(
                "Không thể mở đề thi",
                thong_bao,
                parent=self.__cua_so_cha
            )

            return

        self.__so_giay_con_lai = (
            int(
                self.__de_thi
                .thoi_gian_lam_bai
            )
            * 60
        )

        self.__cua_so = tk.Toplevel(
            self.__cua_so_cha
        )
        self.__cua_so.transient(
            self.__cua_so_cha
        )
        
        self.__cua_so.grab_set()

        self.__cua_so.title(
            "Làm bài thi"
        )

        self.__cua_so.geometry(
            "900x650"
        )

        self.__cua_so.protocol(
            "WM_DELETE_WINDOW",
            self.__dong_cua_so
        )

        self.__dap_an_dang_chon = (
            tk.StringVar(
                master=self.__cua_so,
                value=""
            )
        )

        self.__tao_giao_dien()
        self.__hien_thi_cau_hoi()
        self.__dem_nguoc_thoi_gian()

    def __tai_danh_sach_cau_hoi(self):
        tat_ca_cau_hoi = (
            self.__quan_ly_cau_hoi
            .lay_danh_sach_cau_hoi()
        )

        bang_cau_hoi = {}

        for cau_hoi in tat_ca_cau_hoi:
            bang_cau_hoi[
                cau_hoi.ma_cau_hoi
            ] = cau_hoi

        for ma_cau_hoi in (
            self.__de_thi
            .danh_sach_ma_cau_hoi
        ):
            if ma_cau_hoi not in bang_cau_hoi:
                return False, (
                    "Không tìm thấy câu hỏi "
                    + ma_cau_hoi
                )

            self.__danh_sach_cau_hoi.append(
                bang_cau_hoi[ma_cau_hoi]
            )

        if len(self.__danh_sach_cau_hoi) == 0:
            return False, (
                "Đề thi không có câu hỏi"
            )

        return True, "Tải câu hỏi thành công"

    def __tao_giao_dien(self):
        khung_thong_tin = tk.Frame(
            self.__cua_so,
            bg="#e8f0fe",
            padx=20,
            pady=15
        )

        khung_thong_tin.pack(
            fill="x"
        )

        nhan_ten_de = tk.Label(
            khung_thong_tin,
            text=self.__de_thi.ten_de_thi,
            font=("Arial", 18, "bold"),
            fg="blue",
            bg="#e8f0fe"
        )

        nhan_ten_de.pack(
            side="left"
        )

        self.__nhan_thoi_gian = tk.Label(
            khung_thong_tin,
            text="",
            font=("Arial", 16, "bold"),
            fg="red",
            bg="#e8f0fe"
        )

        self.__nhan_thoi_gian.pack(
            side="right"
        )

        thong_tin_nguoi_lam = tk.Label(
            self.__cua_so,
            text=(
                "Người làm bài: "
                + self.__ten_dang_nhap
                + " | Mã đề: "
                + self.__de_thi.ma_de_thi
                + " | Seed: "
                + str(self.__de_thi.seed)
            ),
            font=("Arial", 11)
        )

        thong_tin_nguoi_lam.pack(
            pady=10
        )

        self.__nhan_vi_tri_cau = tk.Label(
            self.__cua_so,
            text="",
            font=("Arial", 13, "bold"),
            fg="#333333"
        )

        self.__nhan_vi_tri_cau.pack(
            pady=(10, 5)
        )

        self.__nhan_noi_dung = tk.Label(
            self.__cua_so,
            text="",
            font=("Arial", 14, "bold"),
            wraplength=800,
            justify="left",
            anchor="w",
            padx=20,
            pady=15
        )

        self.__nhan_noi_dung.pack(
            fill="x"
        )

        khung_dap_an = tk.LabelFrame(
            self.__cua_so,
            text="Chọn một đáp án",
            font=("Arial", 11, "bold"),
            padx=20,
            pady=15
        )

        khung_dap_an.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        self.__nut_dap_an_a = tk.Radiobutton(
            khung_dap_an,
            text="",
            variable=self.__dap_an_dang_chon,
            value="A",
            font=("Arial", 12),
            anchor="w",
            justify="left",
            wraplength=760,
            command=self.__khi_chon_dap_an
        )

        self.__nut_dap_an_a.pack(
            fill="x",
            pady=8
        )

        self.__nut_dap_an_b = tk.Radiobutton(
            khung_dap_an,
            text="",
            variable=self.__dap_an_dang_chon,
            value="B",
            font=("Arial", 12),
            anchor="w",
            justify="left",
            wraplength=760,
            command=self.__khi_chon_dap_an
        )

        self.__nut_dap_an_b.pack(
            fill="x",
            pady=8
        )

        self.__nut_dap_an_c = tk.Radiobutton(
            khung_dap_an,
            text="",
            variable=self.__dap_an_dang_chon,
            value="C",
            font=("Arial", 12),
            anchor="w",
            justify="left",
            wraplength=760,
            command=self.__khi_chon_dap_an
        )

        self.__nut_dap_an_c.pack(
            fill="x",
            pady=8
        )

        self.__nut_dap_an_d = tk.Radiobutton(
            khung_dap_an,
            text="",
            variable=self.__dap_an_dang_chon,
            value="D",
            font=("Arial", 12),
            anchor="w",
            justify="left",
            wraplength=760,
            command=self.__khi_chon_dap_an
        )

        self.__nut_dap_an_d.pack(
            fill="x",
            pady=8
        )

        self.__nhan_so_cau_da_lam = tk.Label(
            self.__cua_so,
            text="",
            font=("Arial", 11, "italic")
        )

        self.__nhan_so_cau_da_lam.pack(
            pady=5
        )

        khung_nut = tk.Frame(
            self.__cua_so
        )

        khung_nut.pack(
            pady=15
        )

        self.__nut_cau_truoc = tk.Button(
            khung_nut,
            text="Câu trước",
            font=("Arial", 11, "bold"),
            width=14,
            command=self.__chuyen_cau_truoc
        )

        self.__nut_cau_truoc.pack(
            side="left",
            padx=5
        )

        self.__nut_cau_tiep = tk.Button(
            khung_nut,
            text="Câu tiếp theo",
            font=("Arial", 11, "bold"),
            bg="#2196F3",
            fg="white",
            width=16,
            command=self.__chuyen_cau_tiep
        )

        self.__nut_cau_tiep.pack(
            side="left",
            padx=5
        )

        nut_nop_bai = tk.Button(
            khung_nut,
            text="Nộp bài",
            font=("Arial", 11, "bold"),
            bg="#F44336",
            fg="white",
            width=14,
            command=self.__xu_ly_nop_bai
        )

        nut_nop_bai.pack(
            side="left",
            padx=5
        )

    def __lay_noi_dung_phuong_an(
        self,
        cau_hoi,
        ky_tu_phuong_an_goc
    ):
        cac_phuong_an_goc = {
            "A": cau_hoi.phuong_an_a,
            "B": cau_hoi.phuong_an_b,
            "C": cau_hoi.phuong_an_c,
            "D": cau_hoi.phuong_an_d
        }

        return cac_phuong_an_goc.get(
            ky_tu_phuong_an_goc,
            ""
        )

    def __hien_thi_cau_hoi(self):
        cau_hoi = self.__danh_sach_cau_hoi[
            self.__vi_tri_hien_tai
        ]

        so_thu_tu = self.__vi_tri_hien_tai + 1
        tong_so_cau = len(
            self.__danh_sach_cau_hoi
        )

        self.__nhan_vi_tri_cau.config(
            text=(
                "Câu "
                + str(so_thu_tu)
                + "/"
                + str(tong_so_cau)
                + " - Mã câu: "
                + cau_hoi.ma_cau_hoi
            )
        )

        self.__nhan_noi_dung.config(
            text=cau_hoi.noi_dung
        )

        thu_tu_phuong_an = (
            self.__de_thi
            .lay_thu_tu_phuong_an(
                cau_hoi.ma_cau_hoi
            )
        )

        self.__nut_dap_an_a.config(
            text=(
                "A. "
                + str(
                    self.__lay_noi_dung_phuong_an(
                        cau_hoi,
                        thu_tu_phuong_an[0]
                    )
                )
            )
        )

        self.__nut_dap_an_b.config(
            text=(
                "B. "
                + str(
                    self.__lay_noi_dung_phuong_an(
                        cau_hoi,
                        thu_tu_phuong_an[1]
                    )
                )
            )
        )

        self.__nut_dap_an_c.config(
            text=(
                "C. "
                + str(
                    self.__lay_noi_dung_phuong_an(
                        cau_hoi,
                        thu_tu_phuong_an[2]
                    )
                )
            )
        )

        self.__nut_dap_an_d.config(
            text=(
                "D. "
                + str(
                    self.__lay_noi_dung_phuong_an(
                        cau_hoi,
                        thu_tu_phuong_an[3]
                    )
                )
            )
        )

        dap_an_da_chon = (
            self.__cau_tra_loi.get(
                cau_hoi.ma_cau_hoi,
                ""
            )
        )

        self.__dap_an_dang_chon.set(
            dap_an_da_chon
        )

        if self.__vi_tri_hien_tai == 0:
            self.__nut_cau_truoc.config(
                state="disabled"
            )
        else:
            self.__nut_cau_truoc.config(
                state="normal"
            )

        if (
            self.__vi_tri_hien_tai
            == tong_so_cau - 1
        ):
            self.__nut_cau_tiep.config(
                state="disabled"
            )
        else:
            self.__nut_cau_tiep.config(
                state="normal"
            )

        self.__cap_nhat_so_cau_da_lam()

    def __khi_chon_dap_an(self):
        cau_hoi = self.__danh_sach_cau_hoi[
            self.__vi_tri_hien_tai
        ]

        dap_an = (
            self.__dap_an_dang_chon.get()
        )

        self.__cau_tra_loi[
            cau_hoi.ma_cau_hoi
        ] = dap_an

        self.__cap_nhat_so_cau_da_lam()

    def __luu_cau_tra_loi_hien_tai(self):
        cau_hoi = self.__danh_sach_cau_hoi[
            self.__vi_tri_hien_tai
        ]

        dap_an = (
            self.__dap_an_dang_chon.get()
        )

        if dap_an != "":
            self.__cau_tra_loi[
                cau_hoi.ma_cau_hoi
            ] = dap_an

    def __cap_nhat_so_cau_da_lam(self):
        so_cau_da_lam = 0

        for dap_an in self.__cau_tra_loi.values():
            if dap_an != "":
                so_cau_da_lam += 1

        self.__nhan_so_cau_da_lam.config(
            text=(
                "Đã trả lời: "
                + str(so_cau_da_lam)
                + "/"
                + str(
                    len(self.__danh_sach_cau_hoi)
                )
                + " câu"
            )
        )

    def __chuyen_cau_truoc(self):
        self.__luu_cau_tra_loi_hien_tai()

        if self.__vi_tri_hien_tai > 0:
            self.__vi_tri_hien_tai -= 1
            self.__hien_thi_cau_hoi()

    def __chuyen_cau_tiep(self):
        self.__luu_cau_tra_loi_hien_tai()

        if (
            self.__vi_tri_hien_tai
            < len(self.__danh_sach_cau_hoi) - 1
        ):
            self.__vi_tri_hien_tai += 1
            self.__hien_thi_cau_hoi()

    def __dem_nguoc_thoi_gian(self):
        if self.__da_nop_bai:
            return

        phut = self.__so_giay_con_lai // 60
        giay = self.__so_giay_con_lai % 60

        self.__nhan_thoi_gian.config(
            text=(
                "Còn lại: "
                + str(phut).zfill(2)
                + ":"
                + str(giay).zfill(2)
            )
        )

        if self.__so_giay_con_lai <= 0:
            self.__ma_hen_gio = None

            messagebox.showwarning(
                "Hết thời gian",
                "Thời gian làm bài đã hết. "
                "Hệ thống sẽ tự động nộp bài.",
                parent=self.__cua_so
            )

            self.__nop_bai()
            return

        self.__so_giay_con_lai -= 1

        self.__ma_hen_gio = (
            self.__cua_so.after(
                1000,
                self.__dem_nguoc_thoi_gian
            )
        )

    def __xu_ly_nop_bai(self):
        self.__luu_cau_tra_loi_hien_tai()

        tong_so_cau = len(
            self.__danh_sach_cau_hoi
        )

        so_cau_da_lam = len(
            self.__cau_tra_loi
        )

        so_cau_bo_trong = (
            tong_so_cau - so_cau_da_lam
        )

        noi_dung_xac_nhan = (
            "Bạn có chắc muốn nộp bài không?"
        )

        if so_cau_bo_trong > 0:
            noi_dung_xac_nhan += (
                "\nBạn còn bỏ trống "
                + str(so_cau_bo_trong)
                + " câu."
            )

        dong_y = messagebox.askyesno(
            "Xác nhận nộp bài",
            noi_dung_xac_nhan,
            parent=self.__cua_so
        )

        if not dong_y:
            return

        self.__nop_bai()

    def __chuyen_cau_tra_loi_ve_dap_an_goc(
        self
    ):
        cau_tra_loi_goc = {}

        for (
            ma_cau_hoi,
            dap_an_hien_thi
        ) in self.__cau_tra_loi.items():
            dap_an_goc = (
                self.__de_thi
                .chuyen_dap_an_hien_thi_sang_goc(
                    ma_cau_hoi,
                    dap_an_hien_thi
                )
            )

            if dap_an_goc != "":
                cau_tra_loi_goc[
                    ma_cau_hoi
                ] = dap_an_goc

        return cau_tra_loi_goc

    def __nop_bai(self):
        if self.__da_nop_bai:
            return

        self.__luu_cau_tra_loi_hien_tai()
        self.__da_nop_bai = True

        if self.__ma_hen_gio is not None:
            try:
                self.__cua_so.after_cancel(
                    self.__ma_hen_gio
                )
            except tk.TclError:
                pass

            self.__ma_hen_gio = None

        cau_tra_loi_goc = (
            self.__chuyen_cau_tra_loi_ve_dap_an_goc()
        )

        ket_qua, thong_bao = (
            self.__quan_ly_ket_qua
            .cham_diem_va_luu(
                self.__ten_dang_nhap,
                self.__de_thi.ma_de_thi,
                cau_tra_loi_goc
            )
        )

        if ket_qua is None:
            self.__da_nop_bai = False

            messagebox.showerror(
                "Không thể nộp bài",
                thong_bao,
                parent=self.__cua_so
            )

            if self.__so_giay_con_lai > 0:
                self.__dem_nguoc_thoi_gian()

            return

        messagebox.showinfo(
            "Kết quả bài thi",
            thong_bao
            + "\n\nSố câu đúng: "
            + str(ket_qua.so_cau_dung)
            + "/"
            + str(ket_qua.tong_so_cau)
            + "\nĐiểm: "
            + str(ket_qua.diem)
            + "\nXếp loại: "
            + ket_qua.xep_loai,
            parent=self.__cua_so
        )

        self.__cua_so.destroy()

    def __dong_cua_so(self):
        if self.__da_nop_bai:
            self.__cua_so.destroy()
            return

        dong_y = messagebox.askyesno(
            "Thoát bài thi",
            "Bạn có chắc muốn thoát không?\n"
            "Các đáp án hiện tại sẽ không được lưu.",
            parent=self.__cua_so
        )

        if not dong_y:
            return

        if self.__ma_hen_gio is not None:
            try:
                self.__cua_so.after_cancel(
                    self.__ma_hen_gio
                )
            except tk.TclError:
                pass

        self.__cua_so.destroy()
