import numpy as np
# 1번문제: 구글에 물어봤습니다.
ls = ['a1','a2','a3','b1','b2','b3']
print([j[-1::-1] for j in sorted([i[-1::-1] for i in ls])])
# 2번 문제: decompose에 짝수를 넣으면 답이 나옵니다. 기존에 알고있는
# 소수들과 앞으로 찾아내야 할 소수들의 목록을 구한 뒤에 계산을 합니다.
class Goldbach:
    primes = [2,3] # shared by any objects of class Goldbach
    def is_prime(self,number):
        last_candidate = int(number**.5)
        for i in range(2,last_candidate+1):
            if number%i==0:
                break
            if i==last_candidate:
                self.primes.append(number)
    def decompose(self,even):
        answer = []
        for update in range(max(self.primes)+1,even-2):
            self.is_prime(update)
        for prime in self.primes:
            if prime>even/2:
                break
            if even-prime in self.primes:
                answer.append([prime,even-prime])
        return answer
print(Goldbach().decompose(26))
print(Goldbach().primes)
print(Goldbach().decompose(48))
# 3번 문제: 내적을 이용한 영화추천
# add_to_catalogue로 영화들을 학습하고
# movie_similar_to를 이용해서 학습된 영화 중 비슷한 영화를 추출합니다.
# 추천해주는 동시에, 입력된 영화가 학습되지 않은 영화면 학습합니다.
class Recommend:
    # catalogue = np.zeros(4) # cannot update array unlike list
    def __init__(self):
        self.catalogue = np.zeros(4)
        self.titles=['<inintial commit>']
    def add_to_catalogue(self,movie):
        self.catalogue = np.vstack([self.catalogue,movie['scores']])
        self.titles.append(movie['title'])
    def movie_similar_to(self,movie):
        broadcast_inner_product = np.sum(movie['scores']*self.catalogue,axis=1)
        if movie['title'] not in self.titles:
            self.add_to_catalogue(movie)
        return self.titles[np.argmax(broadcast_inner_product)]
movie1 = {'title':'사랑과 전쟁','scores':[3,2,0,2]}
movie2 = {'title':'축구왕 슛돌이','scores':[1,2,3,0]}
movie3 = {'title':'대부','scores':[2,2,2,2]}
recommender=Recommend()
recommender.add_to_catalogue(movie1)
print(Recommend().catalogue)
recommender.add_to_catalogue(movie2)
print(recommender.movie_similar_to(movie3))

# 내적의 한계는 리스트 안의 숫자가 무작정 크면 유사도도 높아지기 때문이다.
# 따라서 리스트 안의 숫자마다 각 리스트의 평균을 빼야한다(공분산).
# 그래도 숫자가 크면 유사도가 커지는 문제가 있기 때문에 표준편차로 나누어주면 더 좋다(상관계수).
