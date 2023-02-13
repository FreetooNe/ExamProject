# """Stores value objects related to the product"""
# import random
# from pages.utils import random_str
#
#
# class User:
#
#     def __init__(self, username="", lastname="", email="", password="", phone=""):
#         self.username = username
#         self.email = email
#         self.password = password
#         self.lastname = lastname
#         self.phone = phone
#         # self.const = StartPageConst
#         # self.consts_header = HeaderConsts
#
#     def fill_data(self):
#         """Fill data  by random generated text"""
#
#         self.username = f"D{random_str(length=7).lower()}"
#         self.lastname = f"{self.username}"
#         self.email = f"{self.username}@gmail.com"
#         self.password = f"{self.username}pw2!"
#         self.phone = f"+380506188{random.randint(100, 999)}"
#
#     def __repr__(self):
#         return f"User:(username{self.username}, lastname = {self.lastname}, email ={self.email}, password ={self.password}),phone = {self.phone}"
