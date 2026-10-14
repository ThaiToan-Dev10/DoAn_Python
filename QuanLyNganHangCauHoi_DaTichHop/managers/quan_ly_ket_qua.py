from datetime import datetime

from config import FILE_KET_QUA
from models.ket_qua import KetQua
from services.xu_ly_json import XuLyJSON

from managers.quan_ly_cau_hoi import QuanLyCauHoi
from managers.quan_ly_de_thi import QuanLyDeThi


class QuanLyKetQua:
    def __init__(
        self,
        quan_ly_cau_hoi=None,
        quan_ly_de_thi=None
    ):
        self.__xu_ly_json = XuLyJSON(
            FILE_KET_QUA
        )

        self.__danh_sach_ket_qua = []

        if quan_ly_cau_hoi is None:
            self.__quan_ly_cau_hoi = (
                QuanLyCauHoi()
            )
        else:
            self.__quan_ly_cau_hoi = (
                quan_ly_cau_hoi
            )

        if quan_ly_de_thi is None:
            self.__quan_ly_de_thi = (
                QuanLyDeThi(
                    self.__quan_ly_cau_hoi
                )
            )
        else:
            self.__quan_ly_de_thi = (
                quan_ly_de_thi
            )

        self.__doc_danh_sach_ket_qua()

    def __doc_danh_sach_ket_qua(self):
        du_lieu = (
            self.__xu_ly_json.doc_du_lieu()
        )

        if not isinstance(du_lieu, list):
            du_lieu = []

        self.__danh_sach_ket_qua = []

        for thong_tin_ket_qua in du_lieu:
            if isinstance(
                thong_tin_ket_qua,
                dict
            ):
                ket_qua = KetQua.tao_tu_dict(
                    thong_tin_ket_qua
                )

                self.__danh_sach_ket_qua.append(
                    ket_qua
                )

    def __luu_danh_sach_ket_qua(self):
        du_lieu = []

        for ket_qua in self.__danh_sach_ket_qua:
            du_lieu.append(
                ket_qua.chuyen_thanh_dict()
            )

        ket_qua_ghi = (
            self.__xu_ly_json.ghi_du_lieu(
                du_lieu
            )
        )

        return ket_qua_ghi is not False

    def __tao_ma_ket_qua_tiep_theo(self):
        so_lon_nhat = 0

        for ket_qua in self.__danh_sach_ket_qua:
            ma_ket_qua = (
                ket_qua.ma_ket_qua
                .strip()
                .upper()
            )

            if ma_ket_qua.startswith("KQ"):
                phan_so = ma_ket_qua[2:]

                if phan_so.isdigit():
                    so_hien_tai = int(phan_so)

                    if so_hien_tai > so_lon_nhat:
                        so_lon_nhat = so_hien_tai

        so_tiep_theo = so_lon_nhat + 1

        return (
            "KQ"
            + str(so_tiep_theo).zfill(3)
        )

    def lay_danh_sach_ket_qua(self):
        return self.__danh_sach_ket_qua.copy()

    def tim_ket_qua_theo_ma(
        self,
        ma_ket_qua
    ):
        ma_can_tim = (
            str(ma_ket_qua)
            .strip()
            .upper()
        )

        for ket_qua in self.__danh_sach_ket_qua:
            if (
                ket_qua.ma_ket_qua.upper()
                == ma_can_tim
            ):
                return ket_qua

        return None

    def lay_ket_qua_theo_nguoi_dung(
        self,
        ten_dang_nhap
    ):
        ten_can_tim = (
            str(ten_dang_nhap)
            .strip()
            .lower()
        )

        danh_sach_tim_duoc = []

        for ket_qua in self.__danh_sach_ket_qua:
            if (
                ket_qua.ten_dang_nhap
                .strip()
                .lower()
                == ten_can_tim
            ):
                danh_sach_tim_duoc.append(
                    ket_qua
                )

        return danh_sach_tim_duoc

    def cham_diem_va_luu(
        self,
        ten_dang_nhap,
        ma_de_thi,
        cau_tra_loi
    ):
        ten_dang_nhap = (
            str(ten_dang_nhap).strip()
        )

        if ten_dang_nhap == "":
            return None, (
                "Tên đăng nhập không được để trống"
            )

        if not isinstance(cau_tra_loi, dict):
            return None, (
                "Danh sách câu trả lời không hợp lệ"
            )

        de_thi = (
            self.__quan_ly_de_thi
            .tim_de_thi_theo_ma(ma_de_thi)
        )

        if de_thi is None:
            return None, "Không tìm thấy đề thi"

        danh_sach_ma_cau_hoi = (
            de_thi.danh_sach_ma_cau_hoi
        )

        tong_so_cau = len(
            danh_sach_ma_cau_hoi
        )

        if tong_so_cau == 0:
            return None, (
                "Đề thi không có câu hỏi"
            )

        tat_ca_cau_hoi = (
            self.__quan_ly_cau_hoi
            .lay_danh_sach_cau_hoi()
        )

        bang_cau_hoi = {}

        for cau_hoi in tat_ca_cau_hoi:
            bang_cau_hoi[
                cau_hoi.ma_cau_hoi
            ] = cau_hoi

        so_cau_dung = 0
        cau_tra_loi_chuan = {}

        for ma_cau_hoi in danh_sach_ma_cau_hoi:
            if ma_cau_hoi not in bang_cau_hoi:
                return None, (
                    "Không tìm thấy câu hỏi "
                    + ma_cau_hoi
                    + " trong ngân hàng câu hỏi"
                )

            cau_hoi = bang_cau_hoi[
                ma_cau_hoi
            ]

            dap_an_nguoi_dung = str(
                cau_tra_loi.get(
                    ma_cau_hoi,
                    ""
                )
            ).strip().upper()

            cau_tra_loi_chuan[
                ma_cau_hoi
            ] = dap_an_nguoi_dung

            dap_an_dung = str(
                cau_hoi.dap_an_dung
            ).strip().upper()

            if dap_an_nguoi_dung == dap_an_dung:
                so_cau_dung += 1

        diem = round(
            so_cau_dung
            / tong_so_cau
            * 10,
            2
        )

        ma_ket_qua = (
            self.__tao_ma_ket_qua_tiep_theo()
        )

        thoi_gian_nop_bai = (
            datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        )

        ket_qua_moi = KetQua(
            ma_ket_qua,
            ten_dang_nhap,
            de_thi.ma_de_thi,
            so_cau_dung,
            tong_so_cau,
            diem,
            cau_tra_loi_chuan,
            thoi_gian_nop_bai
        )

        self.__danh_sach_ket_qua.append(
            ket_qua_moi
        )

        if not self.__luu_danh_sach_ket_qua():
            self.__danh_sach_ket_qua.remove(
                ket_qua_moi
            )

            return None, (
                "Không thể lưu kết quả vào JSON"
            )

        return ket_qua_moi, (
            "Chấm điểm và lưu kết quả thành công"
        )
    
    def lay_chi_tiet_bai_lam(
        self,
        ma_ket_qua
    ):
        ket_qua = self.tim_ket_qua_theo_ma(
            ma_ket_qua
        )
    
        if ket_qua is None:
            return None, (
                "Không tìm thấy kết quả thi"
            )
    
        tat_ca_cau_hoi = (
            self.__quan_ly_cau_hoi
            .lay_danh_sach_cau_hoi()
        )
    
        bang_cau_hoi = {}
    
        for cau_hoi in tat_ca_cau_hoi:
            bang_cau_hoi[
                cau_hoi.ma_cau_hoi
            ] = cau_hoi
    
        danh_sach_chi_tiet = []
    
        for (
            ma_cau_hoi,
            dap_an_nguoi_dung
        ) in ket_qua.cau_tra_loi.items():
    
            cau_hoi = bang_cau_hoi.get(
                ma_cau_hoi
            )
    
            if cau_hoi is None:
                danh_sach_chi_tiet.append(
                    {
                        "ma_cau_hoi": ma_cau_hoi,
                        "cau_hoi": None,
                        "dap_an_nguoi_dung": (
                            dap_an_nguoi_dung
                        ),
                        "dap_an_dung": "",
                        "tra_loi_dung": False
                    }
                )
    
                continue
    
            dap_an_nguoi_dung = str(
                dap_an_nguoi_dung
            ).strip().upper()
    
            dap_an_dung = str(
                cau_hoi.dap_an_dung
            ).strip().upper()
    
            danh_sach_chi_tiet.append(
                {
                    "ma_cau_hoi": ma_cau_hoi,
                    "cau_hoi": cau_hoi,
                    "dap_an_nguoi_dung": (
                        dap_an_nguoi_dung
                    ),
                    "dap_an_dung": dap_an_dung,
                    "tra_loi_dung": (
                        dap_an_nguoi_dung
                        == dap_an_dung
                    )
                }
            )
    
        return danh_sach_chi_tiet, (
            "Lấy chi tiết bài làm thành công"
        )