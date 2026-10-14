import os

# Lấy đường dẫn thư mục gốc của dự án
THU_MUC_GOC = os.path.dirname(os.path.abspath(__file__))

# Đường dẫn đến thư mục data
THU_MUC_DU_LIEU = os.path.join(THU_MUC_GOC, "data")

# Đường dẫn đến từng file JSON
FILE_TAI_KHOAN = os.path.join(THU_MUC_DU_LIEU, "tai_khoan.json")
FILE_CAU_HOI = os.path.join(THU_MUC_DU_LIEU, "cau_hoi.json")
FILE_DE_THI = os.path.join(THU_MUC_DU_LIEU, "de_thi.json")
FILE_KET_QUA = os.path.join(THU_MUC_DU_LIEU, "ket_qua.json")