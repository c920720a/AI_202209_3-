import time

class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr
        
    def print_info(self):
        print("이름 : ", self.name)
        print("휴대전화 번호 : ", self.phone_number)
        print("이메일 : ", self.e_mail)
        print("주소 : ", self.addr)
        print(" ")

# 메뉴 출력
def print_menu():
    print("1. 연락처 임력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    sel = int( input("메뉴 선택 : ") )
    return sel

# 연락처 입력 함수
def set_contact():
    name = input("이름 : ")
    phone_number = input("휴대전화 번호 : ")
    e_mail = input("이메일 : ")
    addr = input("주소 : ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

# 연락처 출력
def print_contact(contact_list):
    print(f"{len(contact_list)}개의 연락처")
    for one in contact_list:
        one.print_info()

# 연락처 삭제
def  delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]
            
def run():
    contact_list = []
    menu = print_menu()
    print("메뉴 선택 : ", menu)
    
    while (menu!=4):
        if menu == 1:
            c1 = set_contact()
            contact_list.append(c1)
            print("연락처 저장 완료")
            print(f"{len(contact_list)}개의 연락처가 있습니다.")
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("삭제할 이름 : ")
            delete_contact(contact_list, name)
        # 메뉴 출력
        elif menu == 4:
            break

    time.sleep(5)
    
if __name__ == "__main__":
    run()