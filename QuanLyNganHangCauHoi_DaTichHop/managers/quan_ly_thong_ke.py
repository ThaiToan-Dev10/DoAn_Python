from services.xu_ly_json import XuLyJSON
from config import (
    FILE_TAI_KHOAN,
    FILE_CAU_HOI,
    FILE_DE_THI,
    FILE_KET_QUA
)


class QuanLyThongKe:
    def __init__(self):
        self.__xu_ly_tai_khoan = (
            XuLyJSON(FILE_TAI_KHOAN)
        )

        self.__xu_ly_cau_hoi = (
            XuLyJSON(FILE_CAU_HOI)
        )

        self.__xu_ly_de_thi = (
            XuLyJSON(FILE_DE_THI)
        )

        self.__xu_ly_ket_qua = (
            XuLyJSON(FILE_KET_QUA)
        )

    def __doc_danh_sach(
        self,
        xu_ly_json
    ):
        danh_sach = xu_ly_json.doc_du_lieu()

        if not isinstance(danh_sach, list):
            return []

        return danh_sach

    def __dem_so_luong(
        self,
        xu_ly_json
    ):
        danh_sach = self.__doc_danh_sach(
            xu_ly_json
        )

        return len(danh_sach)

    def lay_thong_ke_tong_quan(self):
        thong_ke = {
            "so_tai_khoan": (
                self.__dem_so_luong(
                    self.__xu_ly_tai_khoan
                )
            ),
            "so_cau_hoi": (
                self.__dem_so_luong(
                    self.__xu_ly_cau_hoi
                )
            ),
            "so_de_thi": (
                self.__dem_so_luong(
                    self.__xu_ly_de_thi
                )
            ),
            "so_ket_qua": (
                self.__dem_so_luong(
                    self.__xu_ly_ket_qua
                )
            )
        }

        return thong_ke

    def lay_thong_ke_cau_hoi_theo_chu_de(
        self
    ):
        danh_sach_cau_hoi = (
            self.__doc_danh_sach(
                self.__xu_ly_cau_hoi
            )
        )

        thong_ke_theo_chu_de = {}

        for cau_hoi in danh_sach_cau_hoi:
            if not isinstance(cau_hoi, dict):
                continue

            chu_de = str(
                cau_hoi.get("chu_de", "")
            ).strip()

            if chu_de == "":
                chu_de = "Chưa phân loại"

            if chu_de not in thong_ke_theo_chu_de:
                thong_ke_theo_chu_de[
                    chu_de
                ] = 0

            thong_ke_theo_chu_de[
                chu_de
            ] += 1

        danh_sach_da_sap_xep = sorted(
            thong_ke_theo_chu_de.items(),
            key=lambda phan_tu: (
                -phan_tu[1],
                phan_tu[0].casefold()
            )
        )

        ket_qua = {}

        for chu_de, so_luong in (
            danh_sach_da_sap_xep
        ):
            ket_qua[chu_de] = so_luong

        return ket_qua
