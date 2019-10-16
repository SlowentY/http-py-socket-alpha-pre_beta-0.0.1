def index():
    f = open('html\\index.html')
    s = f.read()
    f.close()
    return s

def blog():
    fd = open('html\\blog.html')
    sd = fd.read()
    fd.close()
    return sd

