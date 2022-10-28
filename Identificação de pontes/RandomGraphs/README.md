<h1> Criação dos grafos aleatórios: </h1>

Para a criação dos grafos aleatórios foram utilizadas as seguintes técnicas:
- `Eureliano:` o grafo eureliano é aquele que contém todos seus vértices com o grau par, ou seja, para ter um grafo com todos os vértices com grau par basta adicionar as arestas seguindo um padrão, sendo ele: o vértice atual adicionado ao (vértice atual + 1) fazedo com que o vértice ligue com o preecessor e sucessor, tendo grau dois, porém quando chega no útltimo vértice ele não possui sucessor, fazendo com que ele ligue no primeiro vértice criando assim um ciclo.
- `Semi-eureliano:` o grafo semi-eureliano é aquele que tem somente dois vértices com grau ímpar, ou seja, para criar o grafo bastava criar um grafo eureliano e sortear uma aresta a ser ligada entre dois vértices, transformando assim o grafo eureliano em um grafo semi-eureliano.
- `Não eureliano:` o grafo não eureliano é aquele que tem mais de dois vértices com grau ímpar, ou seja, para criar o grafo bastava criar um grafo eureliano e sortear duas aresta a ser ligada entre dois vértices, transformando assim o grafo eureliano em um grafo não eureliano tendo 4 vértices de grau ímpar.

--------------------------
<p style="font-size: 16px"> <strong> Exemplo de ilustração grafos: </strong> </p>

`Eureliano:`
<div align="center">
  <img src="../_Imagens/eureliano.png" width="350" title="hover text">
</div>

`Semi-Eureliano:`
<div align="center">
  <img src="../_Imagens/semi-eureliano.png" width="350" title="hover text">
</div>

`Não-Eureliano:`
<div align="center">
  <img src="../_Imagens/not_eurelian.png" width="350" title="hover text">
</div>