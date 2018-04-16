from IPython.display import Image
Image(url='http://i.imgur.com/PzOz1qc.gif')

from plotly.widgets import GraphWidget

from IPython.html import widgets 
from IPython.display import display, clear_output
import numpy as np

g = GraphWidget('https://plot.ly/~jackp/2590')
x = y = np.arange(-5,5,0.1)
yt = x[:,np.newaxis]

class z_data:
    def __init__(self):
        self.z = np.cos(x*yt)+np.sin(x*yt)
    
    def on_z_change(self, name, old_value, new_value):
        self.z = np.cos(x*yt*(new_value+1)/100)+np.sin(x*yt*(new_value+1/100))
        self.replot()
        
    def replot(self):
        g.restyle({ 'z': [self.z] })

z_slider = widgets.FloatSliderWidget(min=0,max=3,value=1,step=0.05)
z_slider.description = 'Frequency'
z_slider.value = 1

z_state = z_data()
z_slider.on_trait_change(z_state.on_z_change, 'value')

display(z_slider)
display(g)

# CSS styling within IPython notebook - feel free to re-use
from IPython.core.display import HTML
import urllib2

HTML(urllib2.urlopen('http://bit.ly/1Bf5Hft').read())