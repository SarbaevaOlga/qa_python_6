class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    DZEN_URL_PART = "dzen.ru"

    @property
    def MAIN_PAGE(self):
        return f"{self.BASE_URL}/"

    @property
    def ORDER_PAGE(self):
        return f"{self.BASE_URL}/order"

    @property
    def ORDER_STATUS_PAGE(self):
        return f"{self.BASE_URL}/track"