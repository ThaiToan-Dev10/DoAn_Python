from managers.quan_ly_de_thi import QuanLyDeThi


quan_ly = QuanLyDeThi()

danh_sach = quan_ly.lay_danh_sach_de_thi()


print("===== DANH SÁCH ĐỀ THI =====")

for de_thi in danh_sach:
    print(
        de_thi.ma_de_thi,
        "-",
        de_thi.ten_de_thi,
        "-",
        de_thi.trang_thai
    )


if len(danh_sach) > 0:
    de_thi_kiem_tra = danh_sach[-1]

    ma_de_thi = de_thi_kiem_tra.ma_de_thi
    trang_thai_cu = de_thi_kiem_tra.trang_thai

    if trang_thai_cu == "Mở":
        trang_thai_moi = "Đóng"
    else:
        trang_thai_moi = "Mở"

    print("\n===== THỬ ĐỔI TRẠNG THÁI =====")

    thanh_cong, thong_bao = (
        quan_ly.cap_nhat_trang_thai(
            ma_de_thi,
            trang_thai_moi
        )
    )

    print(thong_bao)

    if thanh_cong:
        print(
            ma_de_thi,
            "đã chuyển thành:",
            trang_thai_moi
        )

        quan_ly.cap_nhat_trang_thai(
            ma_de_thi,
            trang_thai_cu
        )

        print(
            ma_de_thi,
            "đã được đưa lại về:",
            trang_thai_cu
        )


print("\n===== ĐỀ THI ĐANG MỞ =====")

danh_sach_dang_mo = (
    quan_ly.lay_danh_sach_de_thi_dang_mo()
)

print(
    "Số lượng đề đang mở:",
    len(danh_sach_dang_mo)
)