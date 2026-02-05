# The minted package needs to run external programs (Pygments for syntax highlighting), 
# which requires special permission in LaTeX.
c.PDFExporter.latex_command = ['pdflatex', '-shell-escape', '-interaction=nonstopmode']
