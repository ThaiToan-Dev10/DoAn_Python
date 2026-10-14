from managers.quan_ly_tai_khoan import QuanLyTaiKhoan


quan_ly = QuanLyTaiKhoan()

print("===== ĐĂNG NHẬP =====")

ten_dang_nhap = input("Nhập tên đăng nhập: ")
mat_khau = input("Nhập mật khẩu: ")

tai_khoan, thong_bao = quan_ly.dang_nhap(
    ten_dang_nhap,
    mat_khau
)

print(thong_bao)

if tai_khoan is not None:
    print("Họ tên:", tai_khoan.ho_ten)
    print("Email:", tai_khoan.email)
    print("Vai trò:", tai_khoan.vai_tro)