### **문제: 은행 관리 프로그램**

# 1. `Account` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행 계좌의 소유주 이름과 초기 잔액을 설정합니다.
#     - `deposit` 메서드를 사용하여 입금을 처리합니다.
#     - `withdraw` 메서드를 사용하여 출금을 처리합니다. 출금할 금액이 잔액보다 크면 출금을 허용하지 않습니다.
#     - `display_balance` 메서드를 사용하여 현재 잔액을 출력합니다.
# 2. `Bank` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행의 이름을 설정합니다.
#     - `create_account` 메서드를 사용하여 새로운 계좌를 생성합니다.
#     - `get_account` 메서드를 사용하여 계좌를 반환합니다.
#     - `display_accounts` 메서드를 사용하여 현재 은행에 있는 모든 계좌 정보를 출력합니다.
# 3. 사용자가 여러 번 계좌를 생성하고 입금, 출금, 잔액 조회 등의 작업을 수행할 수 있도록 하세요. 
# 사용자가 프로그램을 종료하고 싶을 때에는 "종료"를 입력하면 됩니다.


class Account:
  def __init__(self,name,balance):
    self.name = name
    self.balance = balance

  def deposit(self,amount):
    if amount > 0:
      self.balance += amount
      return self.balance
    else:
      raise ValueError("입금하실 금액을 다시 기입해주세요.")
    
    # return print(f"{self.name}님이 입금하신 금액은 {amount}원 이고, 총 잔액은 {self.balance}원 입니다.")
  
  def withdraw(self,amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      return self.balance
    else:
      raise ValueError("잔액이 부족하거나 잘못된 출금 금액입니다.")
    
    # return print(f"{self.name}님이 출금하신 금액은 {amount}원 이고, 총 잔액은 {self.balance}원 입니다.")
  
  def display_balance(self):
    return self.balance
  

class Bank:
  def __init__(self, bank_name):
    self.bank_name = bank_name
    self.accounts = {}

  def create_account(self):
    self.account = input("생성할 계좌번호를 입력하세요 : ")

  def get_account(self):
    return self.account
  
  def display_accounts(self):
    return