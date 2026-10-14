import tkinter as tk

from managers.quan_ly_cau_hoi import QuanLyCauHoi
from managers.quan_ly_de_thi import QuanLyDeThi
from managers.quan_ly_ket_qua import QuanLyKetQua

from views.giao_dien_chon_de_thi import (
    GiaoDienChonDeThi
)


def mo_giao_dien_chon_de():
    GiaoDienChonDeThi(
        cua_so_chinh,
        "user01",
        quan_ly_de_thi,
        quan_ly_cau_hoi,
        quan_ly_ket_qua
    )


cua_so_chinh = tk.Tk()

cua_so_chinh.title(
    "Kiểm tra làm bài thi"
)

cua_so_chinh.geometry(
    "400x200"
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
    text="KIỂM TRA LÀM BÀI",
    font=("Arial", 16, "bold")
)

tieu_de.pack(pady=30)


nut_mo = tk.Button(
    cua_so_chinh,
    text="Mở danh sách đề thi",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    command=mo_giao_dien_chon_de
)

nut_mo.pack()


cua_so_chinh.mainloop()