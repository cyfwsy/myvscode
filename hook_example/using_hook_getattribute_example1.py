# 验证 __getattribute__() 特性
class CustomAttribute:
    def __init__(self,custom_dict={}):
        self.dict_1 = custom_dict
        self.exists = 5
        
    def __getattribute__(self, name: str):
        print(f'* Called __getattribute__({name !r})')
        try:
            value = super().__getattribute__(name)
            print(f'Found {name !r} ,returning {value !r}')
            if name != 'dict_1':
                self.dict_1[name] = value
            return value
        except AttributeError:
            print('no such attribute')
            # self.dict_1[name] = 'Value'
            
            
        
data = CustomAttribute()
print(data.__dict__)
print(data.dict_1)
print(data.exists)
print(data.foo)
data.foo = 'value of foo'
print(data.foo)
print(data.dict_1)
# print(data.__dict__)
            