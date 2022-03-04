# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import pickle
from dataset.mnist import load_mnist

(x_train,t_train), (x_test,t_test) = load_mnist(normalize=False,one_hot_label=True)

print(x_train.shape) #(60000,784)
print(t_train.shape) #(60000,) #원핫인코딩으로 정답위치의 원소만 1이고 나머지 원소는 0인 배열을 얻을 수 있다.

train_size = x_train.shape[0]
batch_size = 10

batch_mask = np.random.choice(train_size,batch_size) # 지정한 수 중 랜덤으로 10개 골라냄

x_batch=x_train[batch_mask]
t_batch=t_train[batch_mask]


#배치용 교차 엔트로피 오차 (원핫인코딩 되어있을 때)
def cross_entropy_error(y,t):
    if y.ndim ==1:
        t = t.reshape(1,t.size)
        y =  y.reshape(1,y.size)

        batch_size = y.shape[0]
        return -np.sum(t*np.log(y+1e-7))/batch_size

    
#배치용 교차 엔트로피 오차 (원핫인코딩 안되어있을 때)
def cross_entropy_error(y,t):
    if y.ndim ==1:
        t=t.reshape(1,t.size)
        y=y.reshape(1,y.size)

    batch_size = y.shape[0]
    return -np,sum(np.log(y[np.arrage(batch_size),t]+1e-7))/batch_size

    
