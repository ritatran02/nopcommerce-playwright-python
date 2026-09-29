from dotenv import load_dotenv
import os

load_dotenv()


class Config:

    @staticmethod
    def get_url():
        return os.getenv("App.Url")

    @staticmethod
    def get_password():
        return os.getenv("App.Pass")