from managers.quan_ly_cau_hoi import QuanLyCauHoi
from managers.quan_ly_de_thi import QuanLyDeThi
from managers.quan_ly_ket_qua import QuanLyKetQua


quan_ly_cau_hoi = QuanLyCauHoi()

quan_ly_de_thi = QuanLyDeThi(
    quan_ly_cau_hoi
)

quan_ly_ket_qua = QuanLyKetQua(
    quan_ly_cau_hoi,
    quan_ly_de_thi
)


danh_sach_de_thi = (
    quan_ly_de_thi.lay_danh_sach_de_thi()
)


print("===== KIỂM TRA CHẤM ĐIỂM =====")


if len(danh_sach_de_thi) == 0:
    print("Chưa có đề thi để kiểm tra")

else:
    # Lấy đề thi cuối cùng trong danh sách
    de_thi = danh_sach_de_thi[-1]

    print("Mã đề:", de_thi.ma_de_thi)
    print("Tên đề:", de_thi.ten_de_thi)

    print(
        "Số câu:",
        de_thi.so_luong_cau_hoi
    )

    tat_ca_cau_hoi = (
        quan_ly_cau_hoi
        .lay_danh_sach_cau_hoi()
    )

    cau_tra_loi_kiem_tra = {}

    for ma_cau_hoi in (
        de_thi.danh_sach_ma_cau_hoi
    ):
        for cau_hoi in tat_ca_cau_hoi:
            if (
                cau_hoi.ma_cau_hoi
                == ma_cau_hoi
            ):
                cau_tra_loi_kiem_tra[
                    ma_cau_hoi
                ] = cau_hoi.dap_an_dung

                break

    print(
        "Đáp án dùng để kiểm tra:",
        cau_tra_loi_kiem_tra
    )

    ket_qua, thong_bao = (
        quan_ly_ket_qua
        .cham_diem_va_luu(
            "user01",
            de_thi.ma_de_thi,
            cau_tra_loi_kiem_tra
        )
    )

    print("\n===== KẾT QUẢ =====")
    print(thong_bao)

    if ket_qua is not None:
        print(
            "Mã kết quả:",
            ket_qua.ma_ket_qua
        )

        print(
            "Người làm:",
            ket_qua.ten_dang_nhap
        )

        print(
            "Mã đề:",
            ket_qua.ma_de_thi
        )

        print(
            "Số câu đúng:",
            ket_qua.so_cau_dung,
            "/",
            ket_qua.tong_so_cau
        )

        print(
            "Điểm:",
            ket_qua.diem
        )

        print(
            "Xếp loại:",
            ket_qua.xep_loai
        )

        print(
            "Thời gian nộp:",
            ket_qua.thoi_gian_nop_bai
        )