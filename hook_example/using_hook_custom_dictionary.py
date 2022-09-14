class DictionaryRecord:
    # _data = {}
    
    def __init__(self,initial={}):
        self._data = initial
        
    def __getattr__(self, name: str):
        print(f'* Called __getattr__({name !r})')
        if name == '_data':
            super().__setattr__(name,{})
            return self._data
        else:
            try:
                value = self._data[name]
                return value
            except KeyError:
                print(f'No such attribute exists >>> {name !r}')
                
            
    def __setattr__(self,name,value):
        # data_dict = super().__getattribute__('_data')
        if name == '_data':
            super().__setattr__(name,value)
        else:
            self._data[name] = value
    
data = DictionaryRecord({'key1':3,'key2':5})
print(data.key1)
print(data.key2)
print('foo >>>',data.foo)
print('nofoo >>>',data.nofoo)
data.nofoo = 1000
print('nofoo >>>',data.nofoo)
data.key = 'welcome'
print(data.key)
print('data dictionary >>>',data._data)
print(data.__dict__)