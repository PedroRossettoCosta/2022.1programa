"""
Ponto de entrada do projeto.
"""

from jogo.atores import ator1
from jogo.sons import interno, externo

def main():
    """FUnçāo principal"""
    externo.emitir_som()
    ator1.conversar()
    interno.emitir_som()

if __name__ == "__main__":
    main()