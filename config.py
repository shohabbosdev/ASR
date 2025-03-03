from environs import Env

env=Env()

env.read_env()

API_KEY = env('API_KEY')