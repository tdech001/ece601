
from IPython.display import Latex

def LaTeX_matrix(matrix):
    rows = [ ' & '.join([ str(val) for val in row ]) for row in matrix ]
    mstring = r' \\ '.join(rows)
    return Latex(r'\begin{bmatrix} %s \end{bmatrix}'%(mstring))