# O que é Learning to Rank?

Em um problema de classificação, temos um score associado a cada registro, que contém, por exemplo, a probabilidade dada pelo modelo da classe ser '1'. A partir disso, escolhemos um threshold, um limite, e dizemos que, 'se o score for >= a 0.5 você diz que 1, se não, você diz que 0'. 

Em um problema de rankeamente, a ideia é usar esse score associado a cada registro para ordenar a base de dados. Então, o que se deseja prever não é a qual classe aquele indivíduo pertence, mas sim realizar a predição da ordenação dos clientes.

Como, então, medir a perfomance de ordenação do modelo?

1. Curvas de rankeamento:
    * Usado para simular cenários e tomar decisões
    * Reportadas para o time de negócios
    
2. Métricas de rankeamento:
    * Usadas pelos cientistas de dados para medir a perfomance de ordenação
    * Uso mais interno, entre o time de dados
 

# As curvas de Ranking

1. Cumulative Gain Curve (CGC)

|id|propensity_score|target|cumulative_propensity_score|% base|
 1          0.95       1                 25%              13%
 2          0.85       0                 25%              25%
 3          0.80       1                 50%              38%
 4          0.71       1                 75%              50%
 5          0.47       0                 75%              63%
 6          0.36       1                 100%             75%
 7          0.24       0                 100%             88%
 8          0.16       0                 100%             100%
 
 
 Qual o significado do 25% na linha 1? De todos os interessados (4 pessoas), na linha 1 da base conseguimos atingir 25% deles (1 pessoa). Na linha 2, continuamos atingindo 25% dos interessados, pois a pessoa da linha 2 não tem interesse real, apesar de o score dizer que ela teria. Na 3 pessoa, atingimos 50% de todos os interessados da base. Isso nos da a noção de que, se eu ligar para as primeiras 3 pessoas (38% da base), irei atingir 50% de todos os interessados.
 
 Se plotarmos essas duas variáveis, cumulative_propensity_score e porcentagem da base, teremos a curva acumulada de ganho.
 
 Então, de maneira geral, a interpretação é a seguinte: "X% de clientes da base, ordenados pela probabilidade de compra, contém Y% de todos os interessados no novo produto".
 
 
 2. Curva Lift
 
 Essa curva é bem útil para "vender o peixe" para o pessoal de negócios. Ela responde a seguinte pergunta: "quantas vezes o modelo de ML é melhor que o modelo baseline para cada % da base?".

Para calcular o lift, basicamente dividimos o score de propensão acumulado de acordo com o modelo pelo score de propensão acumulado de acordo com o baseline (modelo médio), para cada % da base.
 
|id|propensity_score|target|cumulative_propensity_score|% base|mean_model|lift|
 1          0.95       1                 25%              13%      13%     2.0
 2          0.85       0                 25%              25%      25%     1.0
 3          0.80       1                 50%              38%      38%     1.3
 4          0.71       1                 75%              50%      50%     1.5
 5          0.47       0                 75%              63%      63%     1.2
 6          0.36       1                 100%             75%      75%     1.3
 7          0.24       0                 100%             88%      88%     1.1
 8          0.16       0                 100%             100%     100%    1.0
 
 
 Com isso, podemos plotar uma curva onde temos o lift no eixo Y e a % da base no eixo X. Desse modo, podemos dizer, por exemplo, que "se atingirmos 50% da base, teremos um resultado 1.5X melhor do que o que temos hoje com o nosso modelo".


# As métricas de Ranking 

São métricas utilizadas para medir a perfomance da ordenação. 

* Precision at K
* Recall at K
* F1-Metrics at K
* Average Precision at K


### Precision at k

A precisão, relembrando, pode ser interpretada da seguinte maneira: de todos os exemplos que eu predisse como verdadeiro, quantos realmente eram verdadeiros.

Para calcular essa métrica devemos: contar quantas predições foram corretas até K e dividir por todas as predições realizadas pelo modelo até K. 


### Recall at k

Recall: "de todos os exemplos que realmente são verdadeiros, quantos eu predisse ser verdadeiro?". 

Para calcular: contar quantas predições foram corretas até K e dividir por todos os exemplos verdadeiros do dataset. (É a mesma coisa que o score de propensão acumulado).


### F1-Metric at K

Média harmônica entre precisão e recall até K.
