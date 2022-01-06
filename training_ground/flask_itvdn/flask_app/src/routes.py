from src import api, app
from src.info import Info
from src.timeline import Timeline

api.add_resource(Info, '/api/info', strict_slashes=False)
api.add_resource(Timeline, '/api/timeline', strict_slashes=False)


@app.route('/')
def home():
    return '''<h1>Hello</h1>
    <p><a href="/api/info">Api Info</a></p>
    <p><a href="/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=cumulative&Grouping=weekly&attr1=value1&attr2=value2">Api Timeline</a></p>'''
