import html
import random
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError

class LayCauHoiAPI:
    def __init__(self):
        self.__duong_dan_api = (
            "https://opentdb.com/api.php"
        )

    def lay_cau_hoi(self, so_luong=5):
        if (
            not isinstance(so_luong, int)
            or so_luong < 1
            or so_luong > 50
        ):
            return (
                [],
                "Số lượng câu hỏi phải từ 1 đến 50"
            )

        tham_so = {
            "amount": so_luong,
            "category": 18,
            "type": "multiple"
        }

        duong_dan_day_du = (
            self.__duong_dan_api
            + "?"
            + urlencode(tham_so)
        )

        try:
            yeu_cau = Request(
                duong_dan_day_du,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )

            with urlopen(
                yeu_cau,
                timeout=15
            ) as phan_hoi:
                noi_dung = (
                    phan_hoi
                    .read()
                    .decode("utf-8")
                )

            du_lieu = json.loads(noi_dung)

            ma_phan_hoi = du_lieu.get(
                "response_code"
            )

            if ma_phan_hoi != 0:
                return (
                    [],
                    "API không trả về câu hỏi. "
                    + "Mã phản hồi: "
                    + str(ma_phan_hoi)
                )

            danh_sach = du_lieu.get(
                "results",
                []
            )

            return (
                danh_sach,
                "Lấy câu hỏi từ API thành công"
            )

        except TimeoutError:
            return (
                [],
                "API phản hồi quá lâu"
            )

        except URLError as loi:
            return (
                [],
                "Không thể kết nối API: "
                + str(loi)
            )

        except (
            json.JSONDecodeError,
            UnicodeDecodeError
        ):
            return (
                [],
                "Dữ liệu API trả về không hợp lệ"
            )
    def chuyen_doi_cau_hoi(self,cau_hoi_api, ma_cau_hoi):
        noi_dung = html.unescape(cau_hoi_api.get("question",""))
        
        dap_an_dung_api = html.unescape(cau_hoi_api.get("correct_answer", ""))
        
        cac_phuong_an = [dap_an_dung_api]
        
        danh_sach_dap_an_sai = (cau_hoi_api.get("incorrect_answers",[]))
        
        for dap_an_sai in danh_sach_dap_an_sai:
            cac_phuong_an.append(html.unescape(dap_an_sai))
            
        if len(cac_phuong_an) !=4:
            return None
        random.shuffle(cac_phuong_an)
        vi_tri_dap_an_dung =(cac_phuong_an.index(dap_an_dung_api))
        
        cac_ky_tu_dap_an = (
            "A",
            "B",
            "C",
            "D"
        )

        dap_an_dung = cac_ky_tu_dap_an[
            vi_tri_dap_an_dung
        ]

        bang_muc_do = {
            "easy": "Dễ",
            "medium": "Trung bình",
            "hard": "Khó"
        }

        muc_do_api = cau_hoi_api.get(
            "difficulty",
            "easy"
        )

        muc_do = bang_muc_do.get(
            muc_do_api,
            "Dễ"
        )

        chu_de = html.unescape(
            cau_hoi_api.get(
                "category",
                "Tin học"
            )
        )

        return {
            "ma_cau_hoi": ma_cau_hoi,
            "mon_hoc": "Tin học",
            "chu_de": chu_de,
            "muc_do": muc_do,
            "noi_dung": noi_dung,
            "phuong_an_a": cac_phuong_an[0],
            "phuong_an_b": cac_phuong_an[1],
            "phuong_an_c": cac_phuong_an[2],
            "phuong_an_d": cac_phuong_an[3],
            "dap_an_dung": dap_an_dung,
            "nguon_cau_hoi": "Open Trivia DB"
        }