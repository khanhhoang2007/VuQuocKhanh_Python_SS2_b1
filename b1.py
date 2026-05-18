print(" -- EMERGENCY TRIAGE SYSTEM --- ")

heart_rate = int(input("Enter patient's heart rate (bpm): "))
# LỖI LOGIC (PHÂN TÍCH TRONG CODE)

# LỖI 1: Sai thứ tự điều kiện trong if-elif-else
# Điều kiện "heart_rate > 100" đặt trước "heart_rate > 120"
#  khiến mọi giá trị > 100 (bao gồm 135) đều bị bắt vào nhánh YELLOW trước

if heart_rate > 100:
    # LỖI 2: Nhánh này quá rộng
    # Nó bao phủ luôn cả trường hợp nguy kịch (RED)
    print("Priority: YELLOW - Abnormal. Monitor closely.")

elif heart_rate > 120:
    # LỖI 3: Nhánh này KHÔNG BAO GIỜ được chạy
    # Vì nếu heart_rate > 120 thì đã bị if > 100 bắt trước rồi
    print("Priority: RED - Critical condition! Immediate action required.")

elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")

else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

# LỖI 4 (hệ quả logic):
# RED bị che (unreachable logic path)
#  hệ thống phân loại sai mức độ nguy hiểm

print("Triage process completed.")