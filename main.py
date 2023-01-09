# # from string import ascii_letters, digits
# # from random import choice
# # from json import dump, load
# # from argparse import ArgumentParser
# #
# #
# # parser = ArgumentParser()
# # parser.add_argument('--name')
# # parser.add_argument('--length')
# #
# #
# # def generate_password(length: int = 8) -> str:
# #     return ''.join(choice(ascii_letters + digits) for _ in range(length))
# #
# #
# # def save_password(password: str, name: str) -> None:
# #     with open('password.json', 'a+', encoding='utf-8') as file:
# #         try:
# #             data = load(file)
# #         except:
# #             data = []
# #         data.append({name: password})
# #         print(data)
# #         dump(data, file, ensure_ascii=False, indent=2)
# #
# #
# # if __name__ == '__main__':
# #     args = parser.parse_args()
# #     length = int(args.length)
# #     name = args.name
# #     save_password(generate_password(length), name)
#
from requests import Session


def post(json: dict, url: str) -> dict:
    with Session() as session:
        response = session.post(
            url=url,
            json=json
        )
        if response.status_code == 200:
            return response.json()


if __name__ == '__main__':
    print(
        post(
            url='http://localhost:8070/api/v1/login/',
            json={'username': 'admin', 'password': 'admin'},
        )
    )
# from datetime import datetime, timedelta
#
# from jose import jwt
#
#
# token = jwt.encode({'user': 'qwertyuwertyu', 'exp': datetime.utcnow() + timedelta(minutes=2)}, 'secret2', algorithm='HS256')
# print(token)
# print(jwt.decode(token, 'secret2', algorithms='HS256'))
