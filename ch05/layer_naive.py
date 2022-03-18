from turtle import forward


class MulLayer:
    def __init__(self):
        #변수 초기화
        self.x =None
        self.y = None
    
    def forward(self,x,y):
        #x와 y를 인수로 받고 두 값을 곱하여 반환
        self.x = x
        self.y = y
        out = x*y

        return out

    def backward(self,dout):
        dx = dout * self.y #x와 y를 바꾼다
        dy = dout * self.x #x와 y를 바꾼다
        return dx,dy

apple =100
apple_num = 2
tax =1.1

#계층들
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

#순전파
apple_price = mul_apple_layer.forward(apple,apple_num)
price = mul_tax_layer.forward(apple_price,tax)

print(price)

#미분 구하기
dprice=1
dapple_price,dtax = mul_tax_layer.backward(dprice)

dapple,dapple_num = mul_apple_layer.backward(dapple_price)

print(dapple,dapple_num,dtax)