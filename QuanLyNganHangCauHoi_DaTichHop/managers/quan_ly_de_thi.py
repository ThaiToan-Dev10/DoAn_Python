import random

from config import FILE_DE_THI
from models.de_thi import DeThi
from services.xu_ly_json import XuLyJSON
from managers.quan_ly_cau_hoi import QuanLyCauHoi


class QuanLyDeThi:
    def __init__(self, quan_ly_cau_hoi=None):
        self.__xu_ly_json = XuLyJSON(
            FILE_DE_THI
        )

        self.__danh_sach_de_thi = []

        if quan_ly_cau_hoi is None:
            self.__quan_ly_cau_hoi = (
                QuanLyCauHoi()
            )
        else:
            self.__quan_ly_cau_hoi = (
                quan_ly_cau_hoi
            )

        self.__doc_danh_sach_de_thi()

    def __doc_danh_sach_de_thi(self):
        du_lieu = (
            self.__xu_ly_json.doc_du_lieu()
        )

        if not isinstance(du_lieu, list):
            du_lieu = []

        self.__danh_sach_de_thi = []

        for thong_tin_de_thi in du_lieu:
            if isinstance(
                thong_tin_de_thi,
                dict
            ):
                de_thi = DeThi.tao_tu_dict(
                    thong_tin_de_thi
                )

                self.__danh_sach_de_thi.append(
                    de_thi
                )

    def __luu_danh_sach_de_thi(self):
        du_lieu = []

        for de_thi in self.__danh_sach_de_thi:
            du_lieu.append(
                de_thi.chuyen_thanh_dict()
            )

        ket_qua = (
            self.__xu_ly_json.ghi_du_lieu(
                du_lieu
            )
        )

        return ket_qua is not False

    def lay_danh_sach_de_thi(self):
        return self.__danh_sach_de_thi.copy()

    def tim_de_thi_theo_ma(self, ma_de_thi):
        ma_can_tim = (
            str(ma_de_thi)
            .strip()
            .upper()
        )

        for de_thi in self.__danh_sach_de_thi:
            if (
                de_thi.ma_de_thi.upper()
                == ma_can_tim
            ):
                return de_thi

        return None

    def them_de_thi(self, de_thi):
        if not isinstance(de_thi, DeThi):
            return False, (
                "Dữ liệu không phải là một đề thi"
            )

        ma_de_thi = (
            str(de_thi.ma_de_thi)
            .strip()
            .upper()
        )

        ten_de_thi = (
            str(de_thi.ten_de_thi).strip()
        )

        mon_hoc = str(de_thi.mon_hoc).strip()

        if ma_de_thi == "":
            return False, (
                "Mã đề thi không được để trống"
            )

        if ten_de_thi == "":
            return False, (
                "Tên đề thi không được để trống"
            )

        if mon_hoc == "":
            return False, (
                "Môn học không được để trống"
            )

        if self.tim_de_thi_theo_ma(
            ma_de_thi
        ) is not None:
            return False, "Mã đề thi đã tồn tại"

        try:
            thoi_gian = int(
                de_thi.thoi_gian_lam_bai
            )

            if thoi_gian <= 0:
                return False, (
                    "Thời gian làm bài phải lớn hơn 0"
                )

        except (TypeError, ValueError):
            return False, (
                "Thời gian làm bài phải là số nguyên"
            )

        if de_thi.so_luong_cau_hoi == 0:
            return False, (
                "Đề thi phải có ít nhất một câu hỏi"
            )

        danh_sach_ma = (
            de_thi.danh_sach_ma_cau_hoi
        )

        if len(set(danh_sach_ma)) != len(
            danh_sach_ma
        ):
            return False, (
                "Đề thi không được chứa câu hỏi trùng nhau"
            )

        ma_tran = de_thi.ma_tran_muc_do

        tong_so_cau_ma_tran = (
            ma_tran.get("Dễ", 0)
            + ma_tran.get("Trung bình", 0)
            + ma_tran.get("Khó", 0)
        )

        if (
            tong_so_cau_ma_tran != 0
            and tong_so_cau_ma_tran
            != de_thi.so_luong_cau_hoi
        ):
            return False, (
                "Tổng số câu trong ma trận mức độ "
                "không khớp với đề thi"
            )

        try:
            seed = int(de_thi.seed)

            if seed < 0:
                return False, (
                    "Seed phải lớn hơn hoặc bằng 0"
                )

        except (TypeError, ValueError):
            return False, "Seed phải là số nguyên"

        de_thi.ma_de_thi = ma_de_thi
        de_thi.ten_de_thi = ten_de_thi
        de_thi.mon_hoc = mon_hoc
        de_thi.thoi_gian_lam_bai = thoi_gian
        de_thi.seed = seed

        self.__danh_sach_de_thi.append(
            de_thi
        )

        if not self.__luu_danh_sach_de_thi():
            self.__danh_sach_de_thi.remove(
                de_thi
            )

            return False, (
                "Không thể lưu đề thi vào file JSON"
            )

        return True, "Thêm đề thi thành công"

    def __tao_ma_de_thi_tiep_theo(self):
        so_lon_nhat = 0

        for de_thi in self.__danh_sach_de_thi:
            ma_de_thi = (
                de_thi.ma_de_thi.strip().upper()
            )

            if ma_de_thi.startswith("DT"):
                phan_so = ma_de_thi[2:]

                if phan_so.isdigit():
                    so_hien_tai = int(phan_so)

                    if so_hien_tai > so_lon_nhat:
                        so_lon_nhat = so_hien_tai

        so_tiep_theo = so_lon_nhat + 1

        return (
            "DT"
            + str(so_tiep_theo).zfill(3)
        )

    def __chuyen_so_nguyen_khong_am(
        self,
        gia_tri,
        ten_muc_do
    ):
        try:
            so_luong = int(gia_tri)

            if so_luong < 0:
                return None, (
                    "Số câu "
                    + ten_muc_do
                    + " không được là số âm"
                )

            return so_luong, ""

        except (TypeError, ValueError):
            return None, (
                "Số câu "
                + ten_muc_do
                + " phải là số nguyên"
            )

    def __lay_cau_hoi_theo_mon_va_muc_do(
        self,
        mon_hoc
    ):
        danh_sach_theo_muc_do = {
            "Dễ": [],
            "Trung bình": [],
            "Khó": []
        }

        tat_ca_cau_hoi = (
            self.__quan_ly_cau_hoi
            .lay_danh_sach_cau_hoi()
        )

        for cau_hoi in tat_ca_cau_hoi:
            if (
                cau_hoi.mon_hoc.strip().casefold()
                != mon_hoc.casefold()
            ):
                continue

            muc_do = cau_hoi.muc_do.strip()

            if muc_do in danh_sach_theo_muc_do:
                danh_sach_theo_muc_do[
                    muc_do
                ].append(cau_hoi)

        return danh_sach_theo_muc_do

    def __kiem_tra_du_cau_hoi(
        self,
        danh_sach_theo_muc_do,
        ma_tran_muc_do,
        mon_hoc
    ):
        for muc_do in (
            "Dễ",
            "Trung bình",
            "Khó"
        ):
            so_cau_can = ma_tran_muc_do[muc_do]
            so_cau_hien_co = len(
                danh_sach_theo_muc_do[muc_do]
            )

            if so_cau_hien_co < so_cau_can:
                return False, (
                    "Không đủ câu hỏi mức "
                    + muc_do
                    + " thuộc môn "
                    + mon_hoc
                    + ". Cần "
                    + str(so_cau_can)
                    + " câu nhưng hiện chỉ có "
                    + str(so_cau_hien_co)
                    + " câu."
                )

        return True, "Đủ số lượng câu hỏi"

    def __tao_thu_tu_phuong_an(
        self,
        danh_sach_cau_hoi,
        bo_tao_ngau_nhien
    ):
        thu_tu_phuong_an = {}

        for cau_hoi in danh_sach_cau_hoi:
            thu_tu = ["A", "B", "C", "D"]

            bo_tao_ngau_nhien.shuffle(
                thu_tu
            )

            thu_tu_phuong_an[
                cau_hoi.ma_cau_hoi
            ] = thu_tu

        return thu_tu_phuong_an

    def __tao_de_theo_tong_so_cau(
        self,
        mon_hoc,
        so_luong_cau_hoi,
        seed
    ):
        try:
            so_luong_cau_hoi = int(
                so_luong_cau_hoi
            )

            if so_luong_cau_hoi <= 0:
                return None, None, (
                    "Số lượng câu hỏi phải lớn hơn 0"
                )

        except (TypeError, ValueError):
            return None, None, (
                "Số lượng câu hỏi phải là số nguyên"
            )

        tat_ca_cau_hoi = (
            self.__quan_ly_cau_hoi
            .lay_danh_sach_cau_hoi()
        )

        cau_hoi_phu_hop = []

        for cau_hoi in tat_ca_cau_hoi:
            if (
                cau_hoi.mon_hoc.strip().casefold()
                == mon_hoc.casefold()
            ):
                cau_hoi_phu_hop.append(cau_hoi)

        if len(cau_hoi_phu_hop) < so_luong_cau_hoi:
            return None, None, (
                "Không đủ câu hỏi thuộc môn "
                + mon_hoc
                + ". Hiện có "
                + str(len(cau_hoi_phu_hop))
                + " câu."
            )

        bo_tao_ngau_nhien = random.Random(seed)

        cau_hoi_duoc_chon = (
            bo_tao_ngau_nhien.sample(
                cau_hoi_phu_hop,
                so_luong_cau_hoi
            )
        )

        bo_tao_ngau_nhien.shuffle(
            cau_hoi_duoc_chon
        )

        ma_tran_muc_do = {
            "Dễ": 0,
            "Trung bình": 0,
            "Khó": 0
        }

        for cau_hoi in cau_hoi_duoc_chon:
            muc_do = cau_hoi.muc_do.strip()

            if muc_do in ma_tran_muc_do:
                ma_tran_muc_do[muc_do] += 1

        return (
            cau_hoi_duoc_chon,
            ma_tran_muc_do,
            ""
        )

    def tao_de_thi_tu_dong(
        self,
        ten_de_thi,
        mon_hoc,
        thoi_gian_lam_bai,
        so_cau_de,
        so_cau_trung_binh=None,
        so_cau_kho=None,
        seed=None
    ):
        ten_de_thi = str(
            ten_de_thi
        ).strip()

        mon_hoc = str(mon_hoc).strip()

        if ten_de_thi == "":
            return None, (
                "Tên đề thi không được để trống"
            )

        if mon_hoc == "":
            return None, (
                "Môn học không được để trống"
            )

        try:
            thoi_gian_lam_bai = int(
                thoi_gian_lam_bai
            )

            if thoi_gian_lam_bai <= 0:
                return None, (
                    "Thời gian làm bài phải lớn hơn 0"
                )

        except (TypeError, ValueError):
            return None, (
                "Thời gian làm bài phải là số nguyên"
            )

        if seed is None or str(seed).strip() == "":
            seed = random.randint(
                1,
                999999999
            )
        else:
            try:
                seed = int(seed)

                if seed < 0:
                    return None, (
                        "Seed phải lớn hơn hoặc bằng 0"
                    )

            except (TypeError, ValueError):
                return None, (
                    "Seed phải là số nguyên"
                )

        che_do_giao_dien_cu = (
            so_cau_trung_binh is None
            and so_cau_kho is None
        )

        if che_do_giao_dien_cu:
            (
                cau_hoi_duoc_chon,
                ma_tran_muc_do,
                thong_bao_loi
            ) = self.__tao_de_theo_tong_so_cau(
                mon_hoc,
                so_cau_de,
                seed
            )

            if cau_hoi_duoc_chon is None:
                return None, thong_bao_loi

        else:
            so_cau_de, thong_bao = (
                self.__chuyen_so_nguyen_khong_am(
                    so_cau_de,
                    "Dễ"
                )
            )

            if so_cau_de is None:
                return None, thong_bao

            (
                so_cau_trung_binh,
                thong_bao
            ) = self.__chuyen_so_nguyen_khong_am(
                so_cau_trung_binh,
                "Trung bình"
            )

            if so_cau_trung_binh is None:
                return None, thong_bao

            so_cau_kho, thong_bao = (
                self.__chuyen_so_nguyen_khong_am(
                    so_cau_kho,
                    "Khó"
                )
            )

            if so_cau_kho is None:
                return None, thong_bao

            ma_tran_muc_do = {
                "Dễ": so_cau_de,
                "Trung bình": so_cau_trung_binh,
                "Khó": so_cau_kho
            }

            tong_so_cau = (
                so_cau_de
                + so_cau_trung_binh
                + so_cau_kho
            )

            if tong_so_cau == 0:
                return None, (
                    "Tổng số câu hỏi phải lớn hơn 0"
                )

            danh_sach_theo_muc_do = (
                self.__lay_cau_hoi_theo_mon_va_muc_do(
                    mon_hoc
                )
            )

            du_cau_hoi, thong_bao = (
                self.__kiem_tra_du_cau_hoi(
                    danh_sach_theo_muc_do,
                    ma_tran_muc_do,
                    mon_hoc
                )
            )

            if not du_cau_hoi:
                return None, thong_bao

            bo_tao_ngau_nhien = random.Random(
                seed
            )

            cau_hoi_duoc_chon = []

            for muc_do in (
                "Dễ",
                "Trung bình",
                "Khó"
            ):
                so_cau_can = ma_tran_muc_do[
                    muc_do
                ]

                if so_cau_can > 0:
                    cau_hoi_duoc_chon.extend(
                        bo_tao_ngau_nhien.sample(
                            danh_sach_theo_muc_do[
                                muc_do
                            ],
                            so_cau_can
                        )
                    )

            bo_tao_ngau_nhien.shuffle(
                cau_hoi_duoc_chon
            )

        bo_tao_ngau_nhien = random.Random(seed)

        thu_tu_phuong_an = (
            self.__tao_thu_tu_phuong_an(
                cau_hoi_duoc_chon,
                bo_tao_ngau_nhien
            )
        )

        danh_sach_ma_cau_hoi = []

        for cau_hoi in cau_hoi_duoc_chon:
            danh_sach_ma_cau_hoi.append(
                cau_hoi.ma_cau_hoi
            )

        ma_de_thi = (
            self.__tao_ma_de_thi_tiep_theo()
        )

        de_thi_moi = DeThi(
            ma_de_thi,
            ten_de_thi,
            mon_hoc,
            thoi_gian_lam_bai,
            danh_sach_ma_cau_hoi,
            "Mở",
            ma_tran_muc_do,
            seed,
            thu_tu_phuong_an
        )

        thanh_cong, thong_bao = (
            self.them_de_thi(de_thi_moi)
        )

        if not thanh_cong:
            return None, thong_bao

        return de_thi_moi, (
            "Tạo đề thi tự động thành công"
        )

    def lay_danh_sach_de_thi_dang_mo(self):
        danh_sach_dang_mo = []

        for de_thi in self.__danh_sach_de_thi:
            if (
                de_thi.trang_thai
                .strip()
                .lower()
                == "mở"
            ):
                danh_sach_dang_mo.append(
                    de_thi
                )

        return danh_sach_dang_mo

    def cap_nhat_trang_thai(
        self,
        ma_de_thi,
        trang_thai_moi
    ):
        de_thi = self.tim_de_thi_theo_ma(
            ma_de_thi
        )

        if de_thi is None:
            return False, "Không tìm thấy đề thi"

        trang_thai_moi = str(
            trang_thai_moi
        ).strip().lower()

        if trang_thai_moi == "mở":
            trang_thai_chuan = "Mở"
        elif trang_thai_moi == "đóng":
            trang_thai_chuan = "Đóng"
        else:
            return False, (
                "Trạng thái chỉ được là Mở hoặc Đóng"
            )

        trang_thai_cu = de_thi.trang_thai
        de_thi.trang_thai = trang_thai_chuan

        if not self.__luu_danh_sach_de_thi():
            de_thi.trang_thai = trang_thai_cu

            return False, (
                "Không thể lưu trạng thái đề thi"
            )

        return True, (
            "Cập nhật trạng thái đề thi thành công"
        )

    def xoa_de_thi(self, ma_de_thi):
        de_thi = self.tim_de_thi_theo_ma(
            ma_de_thi
        )

        if de_thi is None:
            return False, "Không tìm thấy đề thi"

        vi_tri = self.__danh_sach_de_thi.index(
            de_thi
        )

        self.__danh_sach_de_thi.pop(vi_tri)

        if not self.__luu_danh_sach_de_thi():
            self.__danh_sach_de_thi.insert(
                vi_tri,
                de_thi
            )

            return False, (
                "Không thể xóa đề thi khỏi file JSON"
            )

        return True, "Xóa đề thi thành công"
