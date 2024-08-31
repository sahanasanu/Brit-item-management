from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Settings class to load environment variables using Pydantic's BaseSettings.

    Attributes:
    ----------
    DATABASE_URL : str
        The URL of the database connection.
    SECRET_KEY : str
        The secret key used for encoding and decoding JWT tokens.
    """

    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        """
        Configuration class for Pydantic settings.

        Attributes:
        ----------
        env_file : str
            Specifies the file from which environment variables should be loaded.
        """

        env_file = ".env"  # Path to the environment file

# Create an instance of the Settings class to be used throughout the application.
settings = Settings()
print(settings)
