from Calculus import *

def plotExample():
    x = np.arange(0, 3, 0.1)
    plot(x, [f(x), 2 * x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])
    
def main():
  use_svg_display()
  plotExample()
  d2l.plt.show()
    

