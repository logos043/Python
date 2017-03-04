class Service:
    secret = "abcdefg"
    def sum(self,a,b):
        result = a + b
        print("%s + %s = %s입니다." % (a, b, result))

pey = Service()

pey.sum(1,1)