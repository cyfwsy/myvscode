class LazyRecord:
    def __init__(self):
        self.exists = 5
        
    def __getattr__(self,name):
        value = f'Value for {name}'
        setattr(self,name,value)
        return value
    
# data = LazyRecord()
# print('Before',data.__dict__)
# print('foo',data.foo)
# print('After',data.__dict__)

class LoggingLazyRecord(LazyRecord):
    def __getattr__(self, name):
        print(f'*Called __getattr__({name !r})',f'populating \
        instance dictionary')
        result = super().__getattr__(name)
        print(f'*Returning {result !r} ')
        return result
    
data = LoggingLazyRecord()
print('exists >>>',data.exists)
print('first foo >>>',data.foo)
print('second foo >>>',data.foo)
