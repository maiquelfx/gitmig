=========================================================================
# Mineração de Commits em Projetos de Software Públicos
### Classificação, Avaliação e Contextualização de Commits com Propósitos Claros ou Indefinidos 
=========================================================================

> [!NOTE]
> ## **[MAIQUEL GOMES](https://github.com/maiquelfx)**</br>
> Mestrando no Departamento de Computação </br>
> Universidade Federal Fluminense (UFF) </br>
> Niterói 24210-346, Brasil </br>
> maiquelgomes@id.uff.br </br>

## ABOUT
</br>
O registro de commits em sistemas Git é essencial no gerenciamento de projetos de software. No entanto, commits sem propósito claro podem comprometer a qualidade do projeto. Para resolver esse problema, este trabalho propõe uma biblioteca em linguagem de programação que classifica commits por propósito e identifica commits vazios ou mal definidos, facilitando a análise do histórico do projeto e a resolução de problemas. Além da implementação, foi realizada uma análise estatística dos dados coletados para entender melhor o contexto dos commits. Além disso, os resultados preliminares indicam que a biblioteca, após fazer o processo de análise e filtragem, consegue identificar com eficiência commits que requerem atenção e a análise estatística identifica padrões e dados que podem ser úteis para melhorias contínuas no processo de desenvolvimento.
</br><p></p>

## QUESTÕES DE PESQUISA

<table>
<thead>
<tr>
<th width="2000" colspan="2">
</th>
</tr>
</thead>
<tbody>
<tr>
  <td width="80" align="center" valign="top">
    <br>
    <img src="./.github/assets/qp1.png"></a>
  </td>
  <td valign="top">
    <p>
</br>Como a classificação automatizada de commits em categorias, incluindo a detecção de commits sem propósito claro, pode aprimorar a qualidade e a precisão do controle de versão em projetos de desenvolvimento de software?
    </p>
  </td>
</tr>
<tr>
  <td width="80" align="center" valign="top">
    <br>
    <img src="./.github/assets/qp2.png"></a>
  </td>
  <td valign="top">
    <p>
      </br>Como a análise contextual detalhada dos commits em repositórios Git pode revelar padrões e insights que podem aprimorar o gerenciamento e a qualidade dos projetos de desenvolvimento de software?
    </p>
  </td>
</tr>
</tbody>
</table>

=========================================================================

## Dependências

- GitPython
- graphviz
- git-graph
- shutil
- os
- regex 
- pandas 
- datetime
- git // Repo, GitCommandError
- numpy -
- plotly // express 
- openpyxl // load_workbook
- openpyxl //styles -> PatternFill
- copy
- zipfile
- google.colab // files
- subprocess
- requests

## Funções
>
### Função para mineração de repositórios
```python
prospect()
```
> [!IMPORTANT]
>  As características do repositório, como número de estrelas e de commits estarão definidas no corpo da função. 

### Definir repositório de trabalho
```python
repo()
```
> [!IMPORTANT]
> Deve ser feito da seguinte forma: proprierário/repositório. Ex.: Google/Drive

### Limpar todos os arquivos na pasta de trabalho, seja local ou remota
```python
clear()
```
### Clonar repositório
```python
clone()
```
### Mineração de commits
```python
mining()
```
### Aplicar categorias em cada um dos commits minerados, adicionando uma cor para cada categoria
```python
cat_color(f'{nome}.xlsx', f'{nome}_class_color.xlsx')
```
> [!TIP]
> Categorias
```python
CORRECTIVE_ENGINEERING
FORWARD_ENGINEERING
REENGINEERING
MANAGEMENT
TESTS
UNCLASSIFIED
```
### Classificar commits por categoria
```python
cat_class_color()
```

### Classificar commits alternando em cada categoria
```python
cat_shuffle_color()
```
> [!TIP]
> Isso facilita a conferência manual de classificação dos commits 

### Geração de visualização web resumida e organizada em tópicos
```python
data_color_html(nome)
```
### Geração de visualização local resumida e organizada em tópicos
```python
data_color_txt(nome)
```
### Geração de arquivo de dados contendo todos os arquivos e linguagens de programação utilizadas
```python
lang()
```
### Geração de pasta com o nome do repositório para mover todos os arquivos gerados para tal. 
```python
gerar_pasta(nome)
```
### Função para fazer download de todos os arquivos gerados em virtude da mineração para a máquina local
```python
download()
```
### Geração de gráfico de dispersão dinâmico, contendo commits, data, hora, local, categoria entre outras informações.
```python
graph()
```

## Resultados (segundos)
| Quantidade de Testes | Tempo de Ordenação (TP) | Testes Priorizados (TP) | Testes Sem Ordenação (TL) |
|----------------------|--------------------------|--------------------------|-----------------------------|
| 10                   | 0                        | 0,39                     | 0,39                        |
| 100                  | 0                        | 0,77                     | 0,74                        |
| 1000                 | 0,000999927520752         | 3,35                     | 2,85                        |
| 10000                | 0,009999752044678         | 3,52                     | 3,3                         |
| 25000                | 0,027008295059204         | 6,32                     | 6,25                        |
| 50000                | 0,078001260757446         | 15,69                    | 17,14                       |
| 100000               | 0,187006711959839         | 29,74                    | 27,23                       |
| 250000               | 0,40993070602417          | 64,27                    | 59,53                       |

##### TP: Testes priorizados / TL: Testes lineares


## Gráfico 2: Comparativo entre o VBTCP e os testes mais citados na literatura
 <img src="./.github/assets/g4.png"></a>
 
