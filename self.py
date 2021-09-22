#self에 대해 이해하기전, class를 짚고 넘어가야한다. class는 각종 변수와 함수들을 묶어 하나의 객체로 만드는 것을 뜻한다.
class Example:
  def set_info(self, name, email, addr):  #class내의 함수를 메서드라 부른다.
    self.name = name
    self.email = email
    self.addr = addr
    
    
#Example()을 Example이라는 클래스의 인스턴스라 부름
card1 = Example() #인스턴스가 메모리의 한 위치에 생성되고, card1이라는 변수가 이를 바인딩. 즉, card1이 인스턴스 주솟값을 담고 있음


class Example2:
  def func1():
    print("1")
    
  def func2(self):
    print("2")
#파이썬 매서드의 첫 번째 인자로 항상 인스턴스가 전달된다.
f = Example2()
f.func2() #인스턴스 매서드인 func2 호출시 첫 번째 인자인 self를 전달하지 않아도 인스턴스가 자동으로 넘어감
f.func1() # 인스턴스 매서드인 func1는 인자가 없지만, 인스턴스가 전달되기 때문에 오류 발생

#인스턴스 메모리 주소를 통해 확인해보자
f = Example2()
id(f)
id(f.func2()) #실행 결과가 같음 --> 즉, 클래스 내에 정의된 self는 클래스 인스턴스다!

#파이썬 클래스는 하나의 네임스페이스이기 때문에 인스턴스 생성 없이 매서드 호출 가능.
Example2.func1() # 인스턴스.매서드()가 아닌 클래스명.매서드() 호출시 오류가 발생하지 않는다.
Example2.func2() #하지만, self를 인자로 받는 매서드 호출시 오류 발생 (self 인자를 전달해야함) 

#즉, 인스턴스를 생성한 뒤 인스턴스를 전달해야함
f2 = Example2()
Example2(f2)
# self 사용: 인스턴스.매서드() or 클래스명.매서드(인스턴스) // self 사용x: 클래스명.매서드()

#결론: self == 인스턴스. 즉, 객체 자기 자신을 참조하는 매개변수다. 파이썬 클래스의 매서드를 정의할 때 self를 명시하여 매서드를 불러올 때 self를 자동으로 전달


#reference
#https://velog.io/@magnoliarfsit/RePython-1.-self-이해하기
