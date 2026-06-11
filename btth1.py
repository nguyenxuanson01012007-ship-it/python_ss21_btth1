balance = 0
import logging

logging.basicConfig(
    filename='momo_log.log',
    level = logging.INFO,
    format='[%(asctime)s]-[%(levelname)s]-[%(message)s]'
)
# nhập tiền
def recharge():
    global balance
    print("--- NẠP TIỀN VÀO VÍ ---")

    while True:
        try:
            amount = int(input("Nhập số tiền cần nạp: "))

            if amount <= 0:
                logging.error(f'InvalidAmountError: Attempted to process {amount} VND.')
                print("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
                return
            balance += amount
            logging.info(f'Deposit successful: +{amount} VND. Current Balance: {balance}')

            print(f'Nạp tiền thành công: +{amount} VND')
            print(f'Số dư hiện tại: {balance} VND')

            break

        except ValueError as e:
            logging.error(f' "ValueError: Invalid numeric input for deposit."')
            print("Lỗi ",e)
# Liểm tra số điện thoại
def check_phone(phone):
    if len(phone) != 10 or not phone.isdigit()   or not phone.startswith('0'):
        return False
    return phone

# chuyển tiền
def Transfer():
    global balance
    print("--- CHUYỂN TIỀN ---")

    phone_number = input("Nhập số điện thoại người nhận: ")

    if check_phone(phone_number):
        try:
            amount = int(input("Nhập số tiền cần chuyển: "))

            if amount <= 0 :
                logging.error(f' ERROR - InvalidAmountError: Attempted to process {amount} VND')
                print("Số tiền không được bé hơn 0")
                return
            if amount > balance:
                logging.error(f'InsufficientBalanceError: Attempted to transfer {amount} VND with balance {balance} VND.')
                print("Giao dịch thất bại: Số dư của bạn không đủ.")
                return
            if amount >= 10000000:
                logging.warning(f' High value transaction detected: {amount} VND to {phone_number}')
                print("Số tiền giao dịch lớn")
                balance -= amount
                return
            
            balance -= amount
            print(f'Số dư hiện tại: {balance} VND')

        except ValueError as e:
            logging.error(f'ValueError: Invalid numeric input for deposit.')
            print("Lỗi ",e)

    else:
        print("Lỗi: Số điện thoại phải gồm đúng 10 chữ số.")
        return
    
def read_logs():
    with open('momo_log.log', 'r') as file:
        print("--- 5 SỰ KIỆN GẦN NHẤT TRONG HỆ THỐNG ---")
        i = 1
        for line in file:
            print(f"{i}. {line.strip()}")
            i += 1
    
# xem số dư
def check_balance():
    global balance

    print("--- SỐ DƯ VÍ MOMO ---")
    print(f"Số dư hiện tại: {balance} VND")

    logging.info(f'Balance checked. Current Balance: {balance}')


while True:
    print("""
    \n========== VÍ MOMO GIẢ LẬP ==========
    1. Nạp tiền vào ví
    2. Chuyển tiền
    3. Xem lịch sử hệ thống
    4. Xem số dư tài khoản
    5. Thoát chương trình 
===============================================
""")

    choice = input("Chọn chức năng (1-5): ")

    if choice == "1":
        recharge()
    elif choice == "2":
        Transfer()
    elif choice == "3":
        read_logs()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Bạn đã thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ !")