#ServerInfo.py

class Info:

    def __init__(self, get):
        self.get = get

    def get_info(self):
        if self.get.lower() == 'uid':
            return '0x00000000'
        if self.get.lower() == 'heap':
            return '0x8000-0x1000000'
        if self.get.lower() == 'name':
            return 'Psiphon All Version'
        if self.get.lower() == 'about':
            return 'linux all version'
        if self.get.lower() == 'ver':
            return 'v.2'
        if self.get.lower() == 'date':
            return '24-06-2019'
        if self.get.lower() == 'by':
            return 'inunxlabs'
        if self.get.lower() == 'mail':
            return 'inunxlabs@gmail.com'
        if self.get.lower() == 'remode':
            return 'Boychongzen aka Xroot'