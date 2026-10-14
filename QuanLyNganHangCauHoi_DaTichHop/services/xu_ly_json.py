import json
import os
import shutil


class XuLyJSON:
    def __init__(self, duong_dan):
        self.__duong_dan = duong_dan

    def doc_du_lieu(self):
        if not os.path.exists(self.__duong_dan):
            print("File chưa tồn tại")
            return []

        try:
            with open(self.__duong_dan, "r", encoding="utf-8") as file:
                noi_dung = file.read().strip()

                if noi_dung == "":
                    return []

                return json.loads(noi_dung)

        except json.JSONDecodeError:
            print("Lỗi: File không đúng định dạng JSON")
            return None

        except PermissionError:
            print("Lỗi: Không có quyền đọc file")
            return None

        except OSError as loi:
            print("Lỗi khi đọc file:", loi)
            return None

    def sao_luu_du_lieu(self):
        if not os.path.exists(self.__duong_dan):
            return True

        try:
            ten_file, phan_mo_rong = os.path.splitext(
                self.__duong_dan
            )

            duong_dan_sao_luu = (
                ten_file + "_backup" + phan_mo_rong
            )

            shutil.copy2(
                self.__duong_dan,
                duong_dan_sao_luu
            )

            return True

        except OSError as loi:
            print("Lỗi khi sao lưu file:", loi)
            return False

    def ghi_du_lieu(self, du_lieu):
        try:
            noi_dung_json = json.dumps(
                du_lieu,
                ensure_ascii=False,
                indent=4
            )

            if not self.sao_luu_du_lieu():
                print("Không thể sao lưu nên dừng ghi dữ liệu")
                return False

            with open(
                self.__duong_dan,
                "w",
                encoding="utf-8"
            ) as file:
                file.write(noi_dung_json)

            return True

        except (TypeError, ValueError) as loi:
            print("Lỗi dữ liệu:", loi)
            return False

        except PermissionError:
            print("Lỗi: Không có quyền ghi file")
            return False

        except OSError as loi:
            print("Lỗi khi ghi file:", loi)
            return False