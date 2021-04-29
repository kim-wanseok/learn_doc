'''
객체지향프로그래밍(OOP)
: 객체(object) 단위로 데이터와 기능을 하나로 묶어서 사용하는 언어기법
 <주요특징>
 1. class + instanse(object)
 2. 추상화(abstract)
 3. 캡슐화
 4. 상속
 5. 다형성(polymorphism) : 함수 오버라이딩, 함수오버로드 


class 란?
attribute(속성)와 method(동작)을 갖는 테이터 타입
1. attribute : value 와 유사
2. method : function 와 유사


class vs object vs instance

class(클래스) : 객체를 만들어 내가 위한 기본 구조
object(객체) : 실제로 구현할 대상의 선언
instance(인스턴스) : 구현된 구체적인 실체

python OOP 특징
 1. 기본적으로 함수 오버로드 미지원 --> 하지만 연산자 오버로드는 가끔 사용함
 2. 생성자, 소멸자가를 직접 쓰지 않음, 초기화자 만 오버라이딩을 많이 해서 사용함
    __new__ --> __init__
 3. 객체 소멸시 소멸자(__del__) 호출 되지만, 가비지콜렉션이 기본제공되어 거의 쓰지 않음.

'''

class Myclass:
    def __del__(self):
        print('delete object')

    def __new__(cls):
        print('make object')
        return super().__new__(cls)

    def __init__(self):
        print('initial')

p = Myclass()

print(type(p))
# print(dir(p))
del p

# class Transport:
#     def __init__(self):
#         print('init')
#         super().__init__()

#     def __new__(cls):
#         print('new')
#         return super().__new__(cls)
    
#     def __del__(self):
#         print('delete')


# t =  Transport()
# print(type(t))
# # print(dir(t))

# del t

