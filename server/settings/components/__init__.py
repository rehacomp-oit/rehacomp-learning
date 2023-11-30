from pathlib import Path

from decouple import AutoConfig


# Build paths inside the project like this: BASE_DIR.joinpath('some')
BASE_DIR = Path(__file__).parent.parent.parent.parent
PROJECT_PACKAGE_DIR = BASE_DIR.joinpath('server')

# Loading `.env` files
# See docs: https://gitlab.com/mkleehammer/autoconfig
env_config = AutoConfig(search_path=BASE_DIR.joinpath('config'))
