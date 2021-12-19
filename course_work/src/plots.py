import plotly.graph_objs as go

class Plot:

    def Create(self, a, b, file):
        types = ['Without index', 'With index']
        secs = [a, b]
        data = [go.Bar(
        x = types,
        y = secs
        )]
        fig = go.Figure(data=data)
        fig.write_image("img/" + file + ".pdf")
        fig.show()