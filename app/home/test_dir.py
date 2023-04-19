import os
path = r"../static/captch/"


current_path = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
path = parent_path + r'\static\captch'
image = path + r'\0f7ce0137ac742c1a59f3a14bbbc38ca.jpg'

print(image)
# image = r'D:\PythonSpace\flask_Project-Exercise\app\static\captcha\0f7ce0137ac742c1a59f3a14bbbc38ca.jpg'

with open(image, 'rb') as f:
    image = f.read()
    print('ok')
