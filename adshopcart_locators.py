from faker import Faker

advantage_shopping_cart_url = 'https://advantageonlineshopping.com/#/'

# fake = Faker(['it_IT', 'en_US', 'ja_JP', 'zh_CN', 'en_CA', 'fr_CA'])
fake = Faker('en_CA')
# Account Details
user_name = fake.user_name()
if len(user_name) > 15:
    user_name = user_name[0:14]
password = fake.password(length=10, special_chars=False, digits=True, upper_case=True, lower_case=True)
email = fake.email()
# Personal Details
first_name = fake.first_name()
last_name = fake.last_name()
phone_number = fake.phone_number()
# Address
country = fake.country()
city = fake.city()
street_address = fake.street_address()
province = fake.province()
if len(province) > 10:
    province = province[0:9]
postal_code = fake.postcode()

full_name = first_name + ' ' + last_name


