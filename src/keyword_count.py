import toml


def load_config():
    return toml.load("config.toml")


def main():
    config = load_config()

    filename = f"{config['outdir']}/{config['resume']['txt']}"
    with open(filename) as f:
        content = f.read().lower()

    counts = { kw: content.count(kw.lower()) for kw in config["keywords"] }

    for kw, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{count}: {kw}")


if __name__ == "__main__":
    main()
