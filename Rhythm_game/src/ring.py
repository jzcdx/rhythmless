"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""

class Ring():
    
    def __init__(self, colour, app):
        self.colour = colour
        self.app = app
        self.canvas = app.canvas
        self.diameter = 20
        self.radius = 300
        self.y = 0
        self.x = (self.canvas.winfo_width() - self.radius) / 2
        
        self.grow_factor = 1.03
        self.shrink_factor = 0.93
        
    def update(self):
        
        #self.radius *= self.grow_factor
        
        self.radius *= self.shrink_factor 
        self.radius -= 0
        
        self.x = (self.canvas.winfo_width() - self.radius) / 2
        self.acceleration = 1.05
        
        self.y += 5 
        self.y *= self.acceleration
        
        self.draw()
        
    def draw(self):
        #x0, y0, x1, y1
        x0 = self.x
        y0 = self.y
        x1 = self.x + self.radius
        y1 = self.y + self.radius
        
        self.rim_size = 5
        
        self.canvas.create_oval(x0, y0, x1, y1, fill='#264348')
        self.canvas.create_oval(x0 + self.rim_size, y0 + self.rim_size, 
                                x1 - self.rim_size, y1 - self.rim_size,
                                fill='#EAEBEC')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        