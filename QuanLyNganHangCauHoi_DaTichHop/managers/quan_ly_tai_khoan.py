import re

from models.tai_khoan import TaiKhoan
from services.xu_ly_json import XuLyJSON
from config import FILE_TAI_KHOAN


class QuanLyTaiKhoan:
    def __init__(self):
        self.__xu_ly_json = XuLyJSON(FILE_TAI_KHOAN)
        self.__danh_sach_tai_khoan = []

        self.doc_danh_sach_tai_khoan()

    def doc_danh_sach_tai_khoan(self):
        du_lieu = self.__xu_ly_json.doc_du_lieu()

        if du_lieu is None:
            print("Không thể đọc dữ liệu tài khoản")
            return False

        if not isinstance(du_lieu, list):
            print("Dữ liệu tài khoản phải là một danh sách")
            return False

        self.__danh_sach_tai_khoan.clear()

        for item in du_lieu:
            tai_khoan = TaiKhoan(
                item.get("ten_dang_nhap", ""),
                item.get("mat_khau", ""),
                item.get("ho_ten", ""),
                item.get("email", ""),
                item.get("vai_tro", "user")
            )

            self.__danh_sach_tai_khoan.append(tai_khoan)

        return True

    def lay_danh_sach_tai_khoan(self):
        return self.__danh_sach_tai_khoan.copy()

    def hien_thi_danh_sach(self):
        if len(self.__danh_sach_tai_khoan) == 0:
            print("Danh sách tài khoản đang rỗng")
            return

        for tai_khoan in self.__danh_sach_tai_khoan:
            print(
                "Tên đăng nhập:",
                tai_khoan.ten_dang_nhap,
                "- Vai trò:",
                tai_khoan.vai_tro
            )

    def kiem_tra_ten_dang_nhap_hop_le(self, ten_dang_nhap):
        mau = r"^[A-Za-z][A-Za-z0-9_]{4,19}$"

        return re.fullmatch(mau, ten_dang_nhap) is not None

    def kiem_tra_email_hop_le(self, email):
        mau = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        return re.fullmatch(mau, email) is not None

    def ten_dang_nhap_da_ton_tai(self, ten_dang_nhap):
        for tai_khoan in self.__danh_sach_tai_khoan:
            if (
                tai_khoan.ten_dang_nhap.lower()
                == ten_dang_nhap.lower()
            ):
                return True

        return False

    def email_da_ton_tai(self, email):
        for tai_khoan in self.__danh_sach_tai_khoan:
            if tai_khoan.email.lower() == email.lower():
                return True

        return False

    def luu_danh_sach_tai_khoan(self):
        du_lieu = []

        for tai_khoan in self.__danh_sach_tai_khoan:
            du_lieu.append(
                tai_khoan.chuyen_thanh_dict()
            )

        return self.__xu_ly_json.ghi_du_lieu(du_lieu)

    def dang_ky_tai_khoan(
        self,
        ten_dang_nhap,
        mat_khau,
        ho_ten,
        email
    ):
        ten_dang_nhap = ten_dang_nhap.strip()
        mat_khau = mat_khau.strip()
        ho_ten = ho_ten.strip()
        email = email.strip().lower()

        if (
            ten_dang_nhap == ""
            or mat_khau == ""
            or ho_ten == ""
            or email == ""
        ):
            return False, "Không được bỏ trống thông tin"

        if not self.kiem_tra_ten_dang_nhap_hop_le(
            ten_dang_nhap
        ):
            return False, "Tên đăng nhập không hợp lệ"

        if len(mat_khau) < 6:
            return False, "Mật khẩu phải có ít nhất 6 ký tự"

        if not self.kiem_tra_email_hop_le(email):
            return False, "Email không hợp lệ"

        if self.ten_dang_nhap_da_ton_tai(ten_dang_nhap):
            return False, "Tên đăng nhập đã tồn tại"

        if self.email_da_ton_tai(email):
            return False, "Email đã tồn tại"

        tai_khoan_moi = TaiKhoan(
            ten_dang_nhap,
            mat_khau,
            ho_ten,
            email,
            "user"
        )

        self.__danh_sach_tai_khoan.append(
            tai_khoan_moi
        )

        if self.luu_danh_sach_tai_khoan():
            return True, "Đăng ký tài khoản thành công"

        self.__danh_sach_tai_khoan.remove(
            tai_khoan_moi
        )

        return False, "Không thể lưu tài khoản"
    
    def dang_nhap(self, ten_dang_nhap, mat_khau):
        ten_dang_nhap = ten_dang_nhap.strip()
        mat_khau = mat_khau.strip()

        if ten_dang_nhap == "" or mat_khau == "":
            return None, "Không được bỏ trống thông tin"

        for tai_khoan in self.__danh_sach_tai_khoan:
            if (
                tai_khoan.ten_dang_nhap.lower()
                == ten_dang_nhap.lower()
            ):
                if tai_khoan.mat_khau == mat_khau:
                    return tai_khoan, "Đăng nhập thành công"

                return None, "Mật khẩu không đúng"

        return None, "Tên đăng nhập không tồn tại"
    
    def xoa_tai_khoan(self,ten_dang_nhap):
        ten_dang_nhap = ten_dang_nhap.strip()
        
        if ten_dang_nhap == "":
            return False, "Tên đăng nhập không được để trống"
        
        for vi_tri, tai_khoan in enumerate(self.__danh_sach_tai_khoan):
            if(tai_khoan.ten_dang_nhap.lower() == ten_dang_nhap.lower()):
                if tai_khoan.vai_tro == "admin":
                    return(False, "Không được xóa tài khoản của quản trị viên")
                tai_khoan_da_xoa = (self.__danh_sach_tai_khoan.pop(vi_tri))
                
                if self.luu_danh_sach_tai_khoan():
                    return(True, "Xóa tài khoản thành công")
                self.__danh_sach_tai_khoan.insert(vi_tri, tai_khoan_da_xoa)
                return(False, "Không thể lưu dữ liệu sau khi xóa")
        return False, "Tài khoản đã tồn tại"
    
    def cap_nhat_tai_khoan(self, ten_dang_nhap, mat_khau_moi, ho_ten, email):
        ten_dang_nhap = ten_dang_nhap.strip()
        mat_khau_moi = mat_khau_moi.strip()
        ho_ten = ho_ten.strip()
        email = email.strip().lower()
        
        if ho_ten == "" or email == "":
            return False, "Không được bỏ trống họ tên và email"

        if mat_khau_moi != "" and len(mat_khau_moi) < 6:
            return (
                False,
                "Mật khẩu mới phải có ít nhất 6 ký tự"
            )

        if not self.kiem_tra_email_hop_le(email):
            return False, "Email không hợp lệ"

        tai_khoan_can_sua = None

        for tai_khoan in self.__danh_sach_tai_khoan:
            if (
                tai_khoan.ten_dang_nhap.lower()
                == ten_dang_nhap.lower()
            ):
                tai_khoan_can_sua = tai_khoan
                break

        if tai_khoan_can_sua is None:
            return False, "Tài khoản không tồn tại"

        for tai_khoan in self.__danh_sach_tai_khoan:
            if (
                tai_khoan.ten_dang_nhap.lower()
                != ten_dang_nhap.lower()
                and tai_khoan.email.lower() == email
            ):
                return False, "Email đã được sử dụng"

        mat_khau_cu = tai_khoan_can_sua.mat_khau
        ho_ten_cu = tai_khoan_can_sua.ho_ten
        email_cu = tai_khoan_can_sua.email

        if mat_khau_moi != "":
            tai_khoan_can_sua.mat_khau = mat_khau_moi

        tai_khoan_can_sua.ho_ten = ho_ten
        tai_khoan_can_sua.email = email

        if self.luu_danh_sach_tai_khoan():
            return True, "Cập nhật tài khoản thành công"

        tai_khoan_can_sua.mat_khau = mat_khau_cu
        tai_khoan_can_sua.ho_ten = ho_ten_cu
        tai_khoan_can_sua.email = email_cu

        return False, "Không thể lưu thông tin tài khoản"
    
    def dat_lai_mat_khau(
        self,
        ten_dang_nhap,
        email,
        mat_khau_moi
    ):
        ten_dang_nhap = ten_dang_nhap.strip()
        email = email.strip()
        mat_khau_moi = mat_khau_moi.strip()
    
        if ten_dang_nhap == "":
            return False, "Vui lòng nhập tên đăng nhập"
    
        if email == "":
            return False, "Vui lòng nhập email đã đăng ký"
    
        if mat_khau_moi == "":
            return False, "Vui lòng nhập mật khẩu mới"
    
        if len(mat_khau_moi) < 6:
            return (
                False,
                "Mật khẩu mới phải có ít nhất 6 ký tự"
            )
    
        for tai_khoan in self.__danh_sach_tai_khoan:
            if (
                tai_khoan.ten_dang_nhap
                == ten_dang_nhap
            ):
                if (
                    tai_khoan.email.lower()
                    != email.lower()
                ):
                    return (
                        False,
                        "Email không đúng với tài khoản"
                    )
    
                tai_khoan.mat_khau = mat_khau_moi
    
                self.luu_danh_sach_tai_khoan()
    
                return (
                    True,
                    "Đặt lại mật khẩu thành công"
                )
    
        return False, "Tên đăng nhập không tồn tại"