from models.de_thi import DeThi


# Tạo một đối tượng đề thi để kiểm tra
de_thi = DeThi(
    "DT001",
    "Kiểm tra Python cơ bản",
    "Tin học",
    15,
    ["CH001", "CH002", "API001"],
    "Mở"
)


print("===== THÔNG TIN ĐỀ THI =====")
print("Mã đề thi:", de_thi.ma_de_thi)
print("Tên đề thi:", de_thi.ten_de_thi)
print("Môn học:", de_thi.mon_hoc)
print("Thời gian:", de_thi.thoi_gian_lam_bai, "phút")
print("Số lượng câu hỏi:", de_thi.so_luong_cau_hoi)
print("Danh sách mã câu hỏi:", de_thi.danh_sach_ma_cau_hoi)
print("Trạng thái:", de_thi.trang_thai)


print("\n===== CHUYỂN THÀNH DICTIONARY =====")
du_lieu_dict = de_thi.chuyen_thanh_dict()
print(du_lieu_dict)


print("\n===== TẠO LẠI ĐỐI TƯỢNG TỪ DICTIONARY =====")
de_thi_moi = DeThi.tao_tu_dict(du_lieu_dict)

print("Mã đề thi:", de_thi_moi.ma_de_thi)
print("Tên đề thi:", de_thi_moi.ten_de_thi)
print("Số lượng câu hỏi:", de_thi_moi.so_luong_cau_hoi)