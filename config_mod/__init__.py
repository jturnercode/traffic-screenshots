import pathlib
import tomli

# ================================================
#                auto load config
#   This is method to auto load config variables
#   __init__.py loads the .toml file at the
#   start of script. The config module is imported
#   where needed to access the values.
#   This can be done with .env, using dotenv.load_env()
# ================================================

# note path is determined automatically
path = pathlib.Path(__file__).parent / "config.toml"
with path.open(mode="rb") as fp:
    config = tomli.load(fp)
