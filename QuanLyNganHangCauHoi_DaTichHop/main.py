import tkinter as tk

from managers.quan_ly_tai_khoan import QuanLyTaiKhoan
from views.giao_dien_dang_nhap import GiaoDienDangNhap


cua_so = tk.Tk()

cua_so.title("Hệ thống quản lý ngân hàng câu hỏi")

cua_so.geometry("900x600")

quan_ly_tai_khoan = QuanLyTaiKhoan()

giao_dien_dang_nhap = GiaoDienDangNhap(cua_so, quan_ly_tai_khoan)

cua_so.mainloop()