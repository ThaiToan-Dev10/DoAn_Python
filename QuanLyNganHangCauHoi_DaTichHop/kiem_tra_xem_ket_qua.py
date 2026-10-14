import tkinter as tk

from managers.quan_ly_cau_hoi import QuanLyCauHoi
from managers.quan_ly_de_thi import QuanLyDeThi
from managers.quan_ly_ket_qua import QuanLyKetQua

from views.giao_dien_xem_ket_qua import (
    GiaoDienXemKetQua
)


def mo_ket_qua_nguoi_dung():
    GiaoDienXemKetQua(
        cua_so_chinh,
        quan_ly_ket_qua,
        quan_ly_de_thi,
        "user01"
    )


def mo_tat_ca_ket_qua():
    GiaoDienXemKetQua(
        cua_so_chinh,
        quan_ly_ket_qua,
        quan_ly_de_thi,
        None
    )


cua_so_chinh = tk.Tk()

cua_so_chinh.title(
    "Kiểm tra xem kết quả"
)

cua_so_chinh.geometry(
    "450x250"
)


quan_ly_cau_hoi = QuanLyCauHoi()

quan_ly_de_thi = QuanLyDeThi(
    quan_ly_cau_hoi
)

quan_ly_ket_qua = QuanLyKetQua(
    quan_ly_cau_hoi,
    quan_ly_de_thi
)


tieu_de = tk.Label(
    cua_so_chinh,
    text="KIỂM TRA KẾT QUẢ",
    font=("Arial", 16, "bold")
)

tieu_de.pack(pady=25)


nut_nguoi_dung = tk.Button(
    cua_so_chinh,
    text="Xem kết quả của user01",
    font=("Arial", 11, "bold"),
    width=25,
    command=mo_ket_qua_nguoi_dung
)

nut_nguoi_dung.pack(pady=5)


nut_admin = tk.Button(
    cua_so_chinh,
    text="Admin xem tất cả kết quả",
    font=("Arial", 11, "bold"),
    width=25,
    command=mo_tat_ca_ket_qua
)

nut_admin.pack(pady=5)


cua_so_chinh.mainloop()