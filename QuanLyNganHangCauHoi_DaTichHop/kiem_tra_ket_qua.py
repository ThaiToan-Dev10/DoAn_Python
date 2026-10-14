from models.ket_qua import KetQua


cau_tra_loi = {
    "CH001": "A",
    "CH002": "C",
    "API001": "D"
}


ket_qua = KetQua(
    "KQ001",
    "user01",
    "DT003",
    2,
    3,
    6.67,
    cau_tra_loi,
    "14/10/2026 10:25:00"
)


print("===== THÔNG TIN KẾT QUẢ =====")
print("Mã kết quả:", ket_qua.ma_ket_qua)
print("Tên đăng nhập:", ket_qua.ten_dang_nhap)
print("Mã đề thi:", ket_qua.ma_de_thi)
print("Số câu đúng:", ket_qua.so_cau_dung)
print("Tổng số câu:", ket_qua.tong_so_cau)
print("Điểm:", ket_qua.diem)
print("Xếp loại:", ket_qua.xep_loai)
print("Câu trả lời:", ket_qua.cau_tra_loi)

print(
    "Thời gian nộp:",
    ket_qua.thoi_gian_nop_bai
)


print("\n===== CHUYỂN THÀNH DICTIONARY =====")

du_lieu_dict = ket_qua.chuyen_thanh_dict()

print(du_lieu_dict)


print("\n===== TẠO LẠI TỪ DICTIONARY =====")

ket_qua_moi = KetQua.tao_tu_dict(
    du_lieu_dict
)

print("Mã kết quả:", ket_qua_moi.ma_ket_qua)
print("Người làm:", ket_qua_moi.ten_dang_nhap)
print("Mã đề:", ket_qua_moi.ma_de_thi)
print("Điểm:", ket_qua_moi.diem)
print("Xếp loại:", ket_qua_moi.xep_loai)