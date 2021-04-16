class a:
    def bu(e):
        print('class a')


class b(a):
    def bu(e):
        print('class b')


class c(a):
    def bu(e):
        print('class c')


class d(b, c):
    pass


z = d()
z.bu()
