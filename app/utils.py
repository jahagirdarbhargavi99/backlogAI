def load_prd(path="prd.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
