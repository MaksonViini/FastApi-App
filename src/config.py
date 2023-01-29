from typing import Literal, Union

from pydantic import BaseModel, BaseSettings, Field


class TestConfig(BaseSettings):
    env: Literal["test"]
    db_host: str = Field(env='db_host_test')
    db_password: str = Field(env='db_password_test')
    db_database: str = Field(env='db_database_test')
    db_port: str = Field(env='db_port_test')


class ProdConfig(BaseSettings):
    env: Literal["prod"]
    db_host: str = Field(env='db_host_prod')
    db_password: str = Field(env='db_password_prod')
    db_database: str = Field(env='db_database_prod')
    db_port: str = Field(env='db_port_prod')


class DevConfig(BaseSettings):
    env: Literal["dev"]
    db_host: str = Field(env='db_host_dev')
    db_password: str = Field(env='db_password_dev')
    db_database: str = Field(env='db_database_dev')
    db_port: str = Field(env='db_port_dev')


class Settings(BaseModel):
    config: Union[DevConfig, ProdConfig, TestConfig]
