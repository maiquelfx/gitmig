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
</br>[Adaptabilidade] - Como a classificação automatizada de commits em categorias, incluindo a detecção de commits sem propósito claro, pode aprimorar a qualidade e a precisão do controle de versão em projetos de desenvolvimento de software?
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
      </br>[Eficiência] - Como a análise contextual detalhada dos commits em repositórios Git pode revelar padrões e insights que podem aprimorar o gerenciamento e a qualidade dos projetos de desenvolvimento de software?
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

```
## Funções
```python
prospect()
```
> [!IMPORTANT]
>  Nas ponderações, caso seja relativa, é importante que soma dos pesos seja igual a 1
```python
prospect()
```
> [!IMPORTANT]
> Nas ponderações, caso seja absoluta, é importante que a soma de `Fi*Pi` seja dividida pela soma de `Pi`
```python
pond_comp = 1
pond_rio = 2
def calc():
  return ((complexidade * pond_comp + risco * pond_prio) / (pond_comp + pond_prio))
```
> [!TIP]
> Equivalência de prioridade relativa
```python
peso_comp = 0.33 #peso1 1/3 -> equivale a peso 1
peso_prio = 0.67 #peso2 2/3 -> equivale a peso 2 // x/3
```
```python
peso_comp = 0.40 #2/5 peso 2 // 0,80/2
peso_prio = 0.60 #3/5  peso 3 'maior prioridade // 1,20/2
```

#### Para desativar um grupo, no bloco da definição dos fatores de prioridade, altera-se o valor da variável declarada `g(n)` para `0`
```python
# grupo 1
complexidade=2
risco=3
dicio['g1'] = calc()
qg1 = 5
g1 = 1 #boolean, 1 para true / 2 para false
```

## Para rodar o Framework via Linux ou WSL
```bash
$ pytest -m test_file.py -v
```
## Para rodar o Pytest via Windows
```python
python -m pytest -v test_unit_100.py
```
```python
python -m pytest -v teste_unit_100k.py
```
```python
python -m pytest -v teste_unit_base.py
```
## Para rodar os testes com grupos
```python
python -m pytest -v test_main_grupos.py
```
## Para rodar os testes unitários de maneira geral
```python
python -m pytest -v test_main_unit.py
```
## Para rodar 100 testes unitários priorizados
```python
python -m pytest -v test_unit_100.py
```
## Para rodar 100.000 testes unitários priorizados
```python
python -m pytest -v teste_unit_100k.py
```
## Gerar arquivo de métrica APFD
```python
python -m pytest -v test_arquivo > output.txt
```
> [!TIP]
> Workflows extensos estão desativados por padrão para evitar sobrecarga de tempo de execução.
> - [x] apfd.yml [2]
> - [ ] gerador.yml [1]
> - [ ] pytest.yml [4]
> - [ ] test_100k.yml [1]

> [!TIP]
> Para o APFD pode ser preciso setar a saída para UTF-8 no CMD
>```bash
>set PYTHONIOENCODING=utf-8
>````

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
 
