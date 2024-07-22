class Euc:

    def calc(self, a: int, b:  int) -> int:
        if b == 0:
            return a
        return self.calc(b, a % b)

    def str_calc(self, a, b):
        ans = self.calc(a, b)
        print(ans)
        return ans


app = Euc()
# print(app.calc(int(input('1: ')), int(input('2: '))))
app.str_calc(int(input('1: ')), int(input('2: ')))
