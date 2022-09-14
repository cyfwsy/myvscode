class ValidatingRecord:
    def __init__(self):
        self.exists = 5
        
    def __getattribute__(self, name: str):
        print(f'* Called __getattribute__({name !r})')
        try:
            value = super().__getattribute__(name)
            print(f'Found {name !r} ,returning {value !r}')
            return value
        except AttributeError:
            value = f'Value for {name}'
            print(f'* setting {name !r} to {value !r}')
            setattr(self,name,value)
            return value
        
data = ValidatingRecord()
print('exists >>>',data.exists)
print('First foo >>>',data.foo)
print('Second foo >>>',data.foo)
print('data dictionary>>>',data.__dict__)
