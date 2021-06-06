from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 5000

    database_url: str

    # jwt_secret: str
    # jwt_algorithm: str = 'HS256'
    # jwt_expires_s: int = 3600


abspath = os.path.abspath(__file__)
# print("abspath: ", abspath)
dname = os.path.dirname(abspath)
# print("dname: ", dname)
file_name = os.path.join(dname, ".env")

settings = Settings(
    _env_file=file_name,
    _env_file_encoding='utf-8',
)
