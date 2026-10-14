from config import FILE_CAU_HOI
from models.cau_hoi import CauHoiTracNghiem
from services.xu_ly_json import XuLyJSON
from services.lay_cau_hoi_api import LayCauHoiAPI

MUC_DO_HOP_LE = ("Dễ", "Trung bình", "Khó")
DAP_AN_HOP_LE = ("A", "B", "C", "D")


class QuanLyCauHoi:
    def __init__(self, duong_dan=FILE_CAU_HOI):
        self.__xu_ly_json = XuLyJSON(duong_dan)
        self.__lay_cau_hoi_api = LayCauHoiAPI()
        self.__danh_sach_cau_hoi = []

        self.doc_danh_sach_cau_hoi()

    def doc_danh_sach_cau_hoi(self):
        du_lieu = self.__xu_ly_json.doc_du_lieu()

        if du_lieu is None:
            print("Không thể đọc dữ liệu câu hỏi")
            return False

        if not isinstance(du_lieu, list):
            print("Dữ liệu câu hỏi phải là một danh sách")
            return False

        danh_sach_moi = []

        for item in du_lieu:
            if not isinstance(item, dict):
                print("Mỗi câu hỏi phải có dạng object trong JSON")
                return False

            danh_sach_moi.append(
                CauHoiTracNghiem.tao_tu_dict(item)
            )

        self.__danh_sach_cau_hoi = danh_sach_moi
        return True

    def lay_danh_sach_cau_hoi(self):
        return self.__danh_sach_cau_hoi.copy()

    def tim_cau_hoi_theo_ma(self, ma_cau_hoi):
        ma_cau_hoi = ma_cau_hoi.strip().casefold()

        for cau_hoi in self.__danh_sach_cau_hoi:
            if cau_hoi.ma_cau_hoi.casefold() == ma_cau_hoi:
                return cau_hoi

        return None

    def tim_kiem_va_loc(
        self,
        tu_khoa="",
        mon_hoc="Tất cả",
        chu_de="Tất cả",
        muc_do="Tất cả"
    ):
        tu_khoa = tu_khoa.strip().casefold()
        ket_qua = []

        for cau_hoi in self.__danh_sach_cau_hoi:
            if (
                tu_khoa != ""
                and tu_khoa not in cau_hoi.ma_cau_hoi.casefold()
                and tu_khoa not in cau_hoi.noi_dung.casefold()
            ):
                continue

            if mon_hoc not in ("", "Tất cả"):
                if cau_hoi.mon_hoc != mon_hoc:
                    continue

            if chu_de not in ("", "Tất cả"):
                if cau_hoi.chu_de != chu_de:
                    continue

            if muc_do not in ("", "Tất cả"):
                if cau_hoi.muc_do != muc_do:
                    continue

            ket_qua.append(cau_hoi)

        return ket_qua

    def __lam_sach_du_lieu(self, du_lieu):
        cac_truong = (
            "ma_cau_hoi",
            "mon_hoc",
            "chu_de",
            "muc_do",
            "noi_dung",
            "phuong_an_a",
            "phuong_an_b",
            "phuong_an_c",
            "phuong_an_d",
            "dap_an_dung",
            "nguon_cau_hoi"
        )

        du_lieu_sach = {}

        for truong in cac_truong:
            du_lieu_sach[truong] = str(
                du_lieu.get(truong, "")
            ).strip()

        du_lieu_sach["ma_cau_hoi"] = (
            du_lieu_sach["ma_cau_hoi"].upper()
        )

        du_lieu_sach["dap_an_dung"] = (
            du_lieu_sach["dap_an_dung"].upper()
        )

        return du_lieu_sach

    def __kiem_tra_du_lieu(
        self,
        du_lieu,
        ma_cau_hoi_cu=None
    ):
        truong_bat_buoc = {
            "Mã câu hỏi": "ma_cau_hoi",
            "Môn học": "mon_hoc",
            "Chủ đề": "chu_de",
            "Mức độ": "muc_do",
            "Nội dung": "noi_dung",
            "Phương án A": "phuong_an_a",
            "Phương án B": "phuong_an_b",
            "Phương án C": "phuong_an_c",
            "Phương án D": "phuong_an_d",
            "Đáp án đúng": "dap_an_dung",
            "Nguồn câu hỏi": "nguon_cau_hoi"
        }

        for ten_hien_thi, ten_truong in truong_bat_buoc.items():
            if du_lieu[ten_truong] == "":
                return False, ten_hien_thi + " không được để trống"

        if du_lieu["muc_do"] not in MUC_DO_HOP_LE:
            return (
                False,
                "Mức độ phải là Dễ, Trung bình hoặc Khó"
            )

        if du_lieu["dap_an_dung"] not in DAP_AN_HOP_LE:
            return False, "Đáp án đúng phải là A, B, C hoặc D"

        for cau_hoi in self.__danh_sach_cau_hoi:
            trung_ma = (
                cau_hoi.ma_cau_hoi.casefold()
                == du_lieu["ma_cau_hoi"].casefold()
            )

            la_cau_hoi_dang_sua = (
                ma_cau_hoi_cu is not None
                and cau_hoi.ma_cau_hoi.casefold()
                == ma_cau_hoi_cu.casefold()
            )

            if trung_ma and not la_cau_hoi_dang_sua:
                return False, "Mã câu hỏi đã tồn tại"

        return True, "Dữ liệu hợp lệ"

    def __luu_danh_sach_cau_hoi(self):
        du_lieu = []

        for cau_hoi in self.__danh_sach_cau_hoi:
            du_lieu.append(cau_hoi.chuyen_thanh_dict())

        return self.__xu_ly_json.ghi_du_lieu(du_lieu)

    def them_cau_hoi(self, du_lieu):
        du_lieu = self.__lam_sach_du_lieu(du_lieu)
        hop_le, thong_bao = self.__kiem_tra_du_lieu(du_lieu)

        if not hop_le:
            return False, thong_bao

        cau_hoi_moi = CauHoiTracNghiem.tao_tu_dict(du_lieu)
        self.__danh_sach_cau_hoi.append(cau_hoi_moi)

        if self.__luu_danh_sach_cau_hoi():
            return True, "Thêm câu hỏi thành công"

        self.__danh_sach_cau_hoi.remove(cau_hoi_moi)
        return False, "Không thể lưu câu hỏi"

    def cap_nhat_cau_hoi(self, ma_cau_hoi_cu, du_lieu):
        du_lieu = self.__lam_sach_du_lieu(du_lieu)

        hop_le, thong_bao = self.__kiem_tra_du_lieu(
            du_lieu,
            ma_cau_hoi_cu
        )

        if not hop_le:
            return False, thong_bao

        vi_tri = None

        for chi_so, cau_hoi in enumerate(
            self.__danh_sach_cau_hoi
        ):
            if (
                cau_hoi.ma_cau_hoi.casefold()
                == ma_cau_hoi_cu.casefold()
            ):
                vi_tri = chi_so
                break

        if vi_tri is None:
            return False, "Không tìm thấy câu hỏi cần sửa"

        cau_hoi_cu = self.__danh_sach_cau_hoi[vi_tri]
        cau_hoi_moi = CauHoiTracNghiem.tao_tu_dict(du_lieu)
        self.__danh_sach_cau_hoi[vi_tri] = cau_hoi_moi

        if self.__luu_danh_sach_cau_hoi():
            return True, "Cập nhật câu hỏi thành công"

        self.__danh_sach_cau_hoi[vi_tri] = cau_hoi_cu
        return False, "Không thể lưu câu hỏi sau khi cập nhật"

    def xoa_cau_hoi(self, ma_cau_hoi):
        for vi_tri, cau_hoi in enumerate(
            self.__danh_sach_cau_hoi
        ):
            if (
                cau_hoi.ma_cau_hoi.casefold()
                == ma_cau_hoi.strip().casefold()
            ):
                cau_hoi_da_xoa = self.__danh_sach_cau_hoi.pop(
                    vi_tri
                )

                if self.__luu_danh_sach_cau_hoi():
                    return True, "Xóa câu hỏi thành công"

                self.__danh_sach_cau_hoi.insert(
                    vi_tri,
                    cau_hoi_da_xoa
                )

                return False, "Không thể lưu dữ liệu sau khi xóa"

        return False, "Câu hỏi không tồn tại"

    def __tao_ma_api_tiep_theo(self):
        so_lon_nhat = 0

        for cau_hoi in self.__danh_sach_cau_hoi:
            ma_cau_hoi = (
                cau_hoi.ma_cau_hoi.upper()
            )

            if ma_cau_hoi.startswith("API"):
                phan_so = ma_cau_hoi[3:]

                if phan_so.isdigit():
                    so_hien_tai = int(phan_so)

                    if so_hien_tai > so_lon_nhat:
                        so_lon_nhat = so_hien_tai

        so_tiep_theo = so_lon_nhat + 1

        return (
            "API"
            + str(so_tiep_theo).zfill(3)
        )
    def nhap_cau_hoi_tu_api(self,so_luong=5):
        danh_sach_api, thong_bao = (
            self.__lay_cau_hoi_api
            .lay_cau_hoi(so_luong)
        )
    
        if len(danh_sach_api) == 0:
            return False, thong_bao
    
        danh_sach_da_them = []
    
        noi_dung_da_co = {
            cau_hoi.noi_dung
            .strip()
            .casefold()
            for cau_hoi
            in self.__danh_sach_cau_hoi
        }
    
        for cau_hoi_api in danh_sach_api:
            ma_cau_hoi = (
                self.__tao_ma_api_tiep_theo()
            )
    
            du_lieu = (
                self.__lay_cau_hoi_api
                .chuyen_doi_cau_hoi(
                    cau_hoi_api,
                    ma_cau_hoi
                )
            )
    
            if du_lieu is None:
                continue
    
            noi_dung = (
                du_lieu["noi_dung"]
                .strip()
                .casefold()
            )
    
            if noi_dung in noi_dung_da_co:
                continue
    
            hop_le, _ = self.__kiem_tra_du_lieu(
                du_lieu
            )
    
            if not hop_le:
                continue
    
            cau_hoi_moi = (
                CauHoiTracNghiem
                .tao_tu_dict(du_lieu)
            )
    
            self.__danh_sach_cau_hoi.append(
                cau_hoi_moi
            )
    
            danh_sach_da_them.append(
                cau_hoi_moi
            )
    
            noi_dung_da_co.add(noi_dung)
    
        if len(danh_sach_da_them) == 0:
            return (
                False,
                "Không có câu hỏi mới để lưu"
            )
    
        if self.__luu_danh_sach_cau_hoi():
            return (
                True,
                "Đã lấy và lưu "
                + str(len(danh_sach_da_them))
                + " câu hỏi từ API"
            )
    
        for cau_hoi in danh_sach_da_them:
            self.__danh_sach_cau_hoi.remove(
                cau_hoi
            )
    
        return (
            False,
            "Không thể lưu câu hỏi từ API"
        )