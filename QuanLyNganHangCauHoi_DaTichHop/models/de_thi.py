class DeThi:
    def __init__(
        self,
        ma_de_thi,
        ten_de_thi,
        mon_hoc,
        thoi_gian_lam_bai,
        danh_sach_ma_cau_hoi,
        trang_thai="Mở",
        ma_tran_muc_do=None,
        seed=0,
        thu_tu_phuong_an=None
    ):
        self.__ma_de_thi = ma_de_thi
        self.__ten_de_thi = ten_de_thi
        self.__mon_hoc = mon_hoc
        self.__thoi_gian_lam_bai = (
            thoi_gian_lam_bai
        )

        if isinstance(
            danh_sach_ma_cau_hoi,
            list
        ):
            self.__danh_sach_ma_cau_hoi = (
                danh_sach_ma_cau_hoi.copy()
            )
        else:
            self.__danh_sach_ma_cau_hoi = []

        self.__trang_thai = trang_thai

        self.__ma_tran_muc_do = (
            self.__tao_ma_tran_muc_do(
                ma_tran_muc_do
            )
        )

        self.__seed = seed

        self.__thu_tu_phuong_an = (
            self.__tao_ban_sao_thu_tu_phuong_an(
                thu_tu_phuong_an
            )
        )

        self.__bo_sung_thu_tu_mac_dinh()

    def __chuyen_thanh_so_nguyen(
        self,
        gia_tri
    ):
        try:
            so_nguyen = int(gia_tri)

            if so_nguyen < 0:
                return 0

            return so_nguyen

        except (TypeError, ValueError):
            return 0

    def __tao_ma_tran_muc_do(
        self,
        ma_tran_muc_do
    ):
        ma_tran_mac_dinh = {
            "Dễ": 0,
            "Trung bình": 0,
            "Khó": 0
        }

        if not isinstance(
            ma_tran_muc_do,
            dict
        ):
            return ma_tran_mac_dinh

        for muc_do in ma_tran_mac_dinh:
            ma_tran_mac_dinh[muc_do] = (
                self.__chuyen_thanh_so_nguyen(
                    ma_tran_muc_do.get(
                        muc_do,
                        0
                    )
                )
            )

        return ma_tran_mac_dinh

    def __tao_ban_sao_thu_tu_phuong_an(
        self,
        thu_tu_phuong_an
    ):
        ket_qua = {}

        if not isinstance(
            thu_tu_phuong_an,
            dict
        ):
            return ket_qua

        for (
            ma_cau_hoi,
            danh_sach_thu_tu
        ) in thu_tu_phuong_an.items():

            if not isinstance(
                danh_sach_thu_tu,
                list
            ):
                continue

            thu_tu_sach = []

            for dap_an in danh_sach_thu_tu:
                dap_an = str(
                    dap_an
                ).strip().upper()

                if (
                    dap_an in ("A", "B", "C", "D")
                    and dap_an not in thu_tu_sach
                ):
                    thu_tu_sach.append(
                        dap_an
                    )

            if len(thu_tu_sach) == 4:
                ket_qua[
                    str(ma_cau_hoi)
                ] = thu_tu_sach

        return ket_qua

    def __bo_sung_thu_tu_mac_dinh(self):
        for ma_cau_hoi in (
            self.__danh_sach_ma_cau_hoi
        ):
            if (
                ma_cau_hoi
                not in self.__thu_tu_phuong_an
            ):
                self.__thu_tu_phuong_an[
                    ma_cau_hoi
                ] = ["A", "B", "C", "D"]

    @property
    def ma_de_thi(self):
        return self.__ma_de_thi

    @ma_de_thi.setter
    def ma_de_thi(self, value):
        self.__ma_de_thi = value

    @property
    def ten_de_thi(self):
        return self.__ten_de_thi

    @ten_de_thi.setter
    def ten_de_thi(self, value):
        self.__ten_de_thi = value

    @property
    def mon_hoc(self):
        return self.__mon_hoc

    @mon_hoc.setter
    def mon_hoc(self, value):
        self.__mon_hoc = value

    @property
    def thoi_gian_lam_bai(self):
        return self.__thoi_gian_lam_bai

    @thoi_gian_lam_bai.setter
    def thoi_gian_lam_bai(self, value):
        self.__thoi_gian_lam_bai = value

    @property
    def danh_sach_ma_cau_hoi(self):
        return (
            self.__danh_sach_ma_cau_hoi
            .copy()
        )

    @danh_sach_ma_cau_hoi.setter
    def danh_sach_ma_cau_hoi(self, value):
        if isinstance(value, list):
            self.__danh_sach_ma_cau_hoi = (
                value.copy()
            )
        else:
            self.__danh_sach_ma_cau_hoi = []

        self.__bo_sung_thu_tu_mac_dinh()

    @property
    def trang_thai(self):
        return self.__trang_thai

    @trang_thai.setter
    def trang_thai(self, value):
        self.__trang_thai = value

    @property
    def ma_tran_muc_do(self):
        return self.__ma_tran_muc_do.copy()

    @ma_tran_muc_do.setter
    def ma_tran_muc_do(self, value):
        self.__ma_tran_muc_do = (
            self.__tao_ma_tran_muc_do(value)
        )

    @property
    def seed(self):
        return self.__seed

    @seed.setter
    def seed(self, value):
        self.__seed = value

    @property
    def thu_tu_phuong_an(self):
        return (
            self.__tao_ban_sao_thu_tu_phuong_an(
                self.__thu_tu_phuong_an
            )
        )

    @thu_tu_phuong_an.setter
    def thu_tu_phuong_an(self, value):
        self.__thu_tu_phuong_an = (
            self.__tao_ban_sao_thu_tu_phuong_an(
                value
            )
        )

        self.__bo_sung_thu_tu_mac_dinh()

    @property
    def so_luong_cau_hoi(self):
        return len(
            self.__danh_sach_ma_cau_hoi
        )

    def lay_thu_tu_phuong_an(
        self,
        ma_cau_hoi
    ):
        thu_tu = (
            self.__thu_tu_phuong_an.get(
                ma_cau_hoi,
                ["A", "B", "C", "D"]
            )
        )

        return thu_tu.copy()

    def chuyen_dap_an_goc_sang_hien_thi(
        self,
        ma_cau_hoi,
        dap_an_goc
    ):
        cac_ky_tu = ("A", "B", "C", "D")

        thu_tu = self.lay_thu_tu_phuong_an(
            ma_cau_hoi
        )

        dap_an_goc = str(
            dap_an_goc
        ).strip().upper()

        for vi_tri, dap_an in enumerate(
            thu_tu
        ):
            if dap_an == dap_an_goc:
                return cac_ky_tu[vi_tri]

        return ""

    def chuyen_dap_an_hien_thi_sang_goc(
        self,
        ma_cau_hoi,
        dap_an_hien_thi
    ):
        cac_ky_tu = ("A", "B", "C", "D")

        dap_an_hien_thi = str(
            dap_an_hien_thi
        ).strip().upper()

        if dap_an_hien_thi not in cac_ky_tu:
            return ""

        vi_tri = cac_ky_tu.index(
            dap_an_hien_thi
        )

        thu_tu = self.lay_thu_tu_phuong_an(
            ma_cau_hoi
        )

        return thu_tu[vi_tri]

    def chuyen_thanh_dict(self):
        return {
            "ma_de_thi": self.__ma_de_thi,
            "ten_de_thi": self.__ten_de_thi,
            "mon_hoc": self.__mon_hoc,
            "thoi_gian_lam_bai": (
                self.__thoi_gian_lam_bai
            ),
            "danh_sach_ma_cau_hoi": (
                self.__danh_sach_ma_cau_hoi
                .copy()
            ),
            "ma_tran_muc_do": (
                self.__ma_tran_muc_do.copy()
            ),
            "seed": self.__seed,
            "thu_tu_phuong_an": (
                self.thu_tu_phuong_an
            ),
            "trang_thai": self.__trang_thai
        }

    @classmethod
    def tao_tu_dict(cls, du_lieu):
        return cls(
            du_lieu.get("ma_de_thi", ""),
            du_lieu.get("ten_de_thi", ""),
            du_lieu.get("mon_hoc", ""),
            du_lieu.get(
                "thoi_gian_lam_bai",
                0
            ),
            du_lieu.get(
                "danh_sach_ma_cau_hoi",
                []
            ),
            du_lieu.get(
                "trang_thai",
                "Mở"
            ),
            du_lieu.get(
                "ma_tran_muc_do",
                {}
            ),
            du_lieu.get("seed", 0),
            du_lieu.get(
                "thu_tu_phuong_an",
                {}
            )
        )
