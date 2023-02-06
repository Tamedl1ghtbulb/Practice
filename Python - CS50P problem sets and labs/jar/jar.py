class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Invalid input')
        else:
            self._capacity = capacity
            self._size = 0
    def __str__(self):
        return f'🍪'*self.size

    def deposit(self, n):
        if n > self.capacity or n+ self.size > self.capacity:
            raise ValueError
        self._size+=n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self._size -= n
    @property
    def capacity(self):
        return self._capacity
#    @capacity.setter
#    def capacity(self, n):
#        if n<0:
 #           raise ValueError('Ne moze biti negativan broj kolaca!')
  #      self._capacity = n
   #     return self._capacity
    @property
    def size(self):
        return self._size
#    @size.setter
 #   def size(self,n):
  #      if n<0:
   #         raise ValueError('Ne moze biti negativan broj kolaca!')
    #    self._size = n
     #   return self._size

racunanje = Jar(10)
racunanje.deposit(6)
racunanje.withdraw(4)
print(racunanje)
