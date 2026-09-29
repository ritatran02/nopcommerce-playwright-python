from faker import Faker


class DataConfig:

    def __init__(self):
        self.faker = Faker("en_US")

    @staticmethod
    def get_data():
        return DataConfig()

    def get_first_name(self):
        return self.faker.first_name()

    def get_last_name(self):
        return self.faker.last_name()

    def get_random_number(self):
        return str(self.faker.random_digit())

    def get_email_address(self):
        return self.faker.email()