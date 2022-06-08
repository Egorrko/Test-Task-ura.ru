from environs import Env

env = Env()
env.read_env()

RULES = env.dict('RULES', subcast_keys=int)
