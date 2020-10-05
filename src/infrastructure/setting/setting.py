from decouple import config


class Settings:

    def getDatabaseURL(self) -> str:
        return config('DATABASE_URL')
