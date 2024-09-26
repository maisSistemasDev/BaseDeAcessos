from controllers.Base import API

class Access(API):
    base_url = "https://auto-api.maisistemasdev.com"
    path = "/usuarios/acessos/"
    
    def __init__(self) -> None:
        super().__init__(self.base_url, self.path)
    
    def get_access(self):
        res = self.get()
        if(res.ok):
            return res.json
        else:
            return {'error':res.reason}
    
    
        
        
        