class User:

  def __init__(self, first_name, last_name, address, mobile_number):
    self.first_name = first_name
    self.last_name = last_name
    self.address = address
    self.mobile_number = mobile_number
    self.login_attempts = 0

  def describe_user(self):
    print(f"I will provide some info about {self.first_name} {self.last_name}")
    print(f"Address: {self.address} \nMobile number: {self.mobile_number}")

  def greet_user(self):
    print(f"Hello dear, {self.first_name}!")

  def increment_login_attempts(self):
    self.login_attempts += 1

  def reset_login_attempts(self):
    self.login_attempts = 0
