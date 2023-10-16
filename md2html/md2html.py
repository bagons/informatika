import markdown


def load_file(path):
    out = ""
    f = open(path)
    out = f.read()
    f.close()
    return out


def save_file(path, contens):
    f = open(path, "w")
    f.write(contens)
    f.close()

path = input("path: ")
save_file(path.replace(".md", ".html"), markdown.markdown(load_file(path)))