#override: 같은 이름을 가진 매서드를 덮어씀
class father():
  def handsome(self):
    print('handsome')

#자식클래스(부모클래스) -->father class의 매서드를 상속받음 
class brother(father):

class sister(father):
  def pretty(self):
    print('pretty')
  
  def handsome(self):
    self.pretty()

b=brother()
b.handsome() #handsome출력
g=sister()
c.handsome() #pretty출력 --> 부모클래스를 상속받았지만 오버라이딩됨

#super
class father():  # 부모 클래스
    def __init__(self, who):
        self.who = who
 
    def handsome(self):
        print("{}를 닮아 잘생겼다".format(self.who))
 
class sister(father):  # 자식클래스(부모클래스) 아빠매소드를 상속받겠다
    def __init__(self, who, where):
        super().__init__(who) #who를 부모에게서 물려받은 것이기 때문에 super 사용
        self.where = where
 
    def choice(self):
        print("{} 말이야".format(self.where))
 
    def handsome(self):
       super().handsome() #handsome을 부모에게서 물려받은 것이기 때문에 super 사용
       self.choice()
 
girl = sister("아빠", "얼굴")
girl.handsome()


#reference
#https://rednooby.tistory.com/56?category=633023 [개발자의 취미생활]
