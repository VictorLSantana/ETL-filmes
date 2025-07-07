
import re

def limpar_titulos(filmes):
    # Expressão regular para capturar o nome após "número. "
    regex = re.compile(r'^\d+\.\s+(.*)')

    # Usando filter para extrair apenas os nomes filmes válidos
    nomes_filmes = list(
        filter(lambda s: regex.match(s), filmes)
    )
    
    # Usando map  para limpar os nomes dos filmes
    nomes_filmes_limpos = list(
    map(lambda s: regex.match(s).group(1), nomes_filmes)
    )
    
    return nomes_filmes_limpos

if __name__ == "__main__":
    filmes = [
        '20. Se7en',
        "21. It's a Wonderful Life",
        '22. The Silence of the Lambs',
        '23. Seven Samurai',
        '24. Saving Private Ryan',
        'Lowest rated movies',
        'Most popular celebs',
        'Movie news'
    ]
    
    nomes_filmes_limpos = limpar_titulos(filmes)
    print(nomes_filmes_limpos)
     