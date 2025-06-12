import qrcode

# QR 코드에 넣을 데이터
data = "https://www.data.go.kr/"

# QR 코드 생성
qr = qrcode.QRCode(
    version=1,  # 1부터 40까지 숫자로, QR 코드의 크기를 결정
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 수정 수준
    box_size=10,  # QR 코드의 각 사각형의 크기
    border=4,  # 테두리의 두께
)

# 데이터 추가
qr.add_data(data)
qr.make(fit=True)

# 이미지로 변환
img = qr.make_image(fill='black', back_color='white')

# 이미지 파일로 저장
img.save("./16GPT/qrcode_example.png")
