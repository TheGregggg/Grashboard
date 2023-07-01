class Application:
    def __init__(self, name, bgcolor, color, link) -> None:
        self.name = name
        self.bgcolor = bgcolor
        self.color = color
        self.link = link

CONTEXTS = {
    "Grashboard": {
        'name':'Grashboard',
        'subtitle': 'グレッグ',
        'search_url':'https://www.google.com/search?q=',
        'elem_per_col': 4,
        'applications':[
            Application('GregNAS', '#0067E6', '#fff', 'http://gregnas:5000/'),
            Application('GregFlix', '#E50914', '#fff', 'http://gregflix/'),
            Application('GregRouter', '#eb7d34', '#fff', 'https://10.69.0.1/'),
            Application('Actual', '#874ad5', '#fff', 'http://192.168.1.69:5006/'),
        ]
    }
}
