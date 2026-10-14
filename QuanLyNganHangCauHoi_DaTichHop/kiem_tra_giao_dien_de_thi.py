import tkinter as tk

from managers.quan_ly_de_thi import QuanLyDeThi
from views.giao_dien_quan_ly_de_thi import (
    GiaoDienQuanLyDeThi
)


def mo_giao_dien_de_thi():
    GiaoDienQuanLyDeThi(
        cua_so_chinh,
        quan_ly_de_thi
    )


cua_so_chinh = tk.Tk()

cua_so_chinh.title(
    "Kiểm tra giao diện đề thi"
)

cua_so_chinh.geometry(
    "400x200"
)


quan_ly_de_thi = QuanLyDeThi()


tieu_de = tk.Label(
    cua_so_chinh,
    text="KIỂM TRA GIAO DIỆN",
    font=("Arial", 16, "bold")
)

tieu_de.pack(pady=30)


nut_mo = tk.Button(
    cua_so_chinh,
    text="Mở quản lý đề thi",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    command=mo_giao_dien_de_thi
)

nut_mo.pack()


cua_so_chinh.mainloop()