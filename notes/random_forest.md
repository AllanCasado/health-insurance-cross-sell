# O dilema de Viés e Variância (Bias and Variance)

Quando pegamos o erro entre uma predição e o que realmente é verdade, esse erro é composto de tres partes:

1. Erro Intrínseco do Problema: um erro que não temoscontrole, é devido a falta de variáveis para modela ofenômeno.

2. Viés: erro devido a falta de flexibilização do modelo.

3. Variância: erro devido a falta do modelo conseguirgeneralizar as predições para dados que ele nunca viu.

Esses erros são resultados de uma prova matemática.


## Bias & Variance

Vamos supor que temos duas variáveis X e Y e quando plotamos em um gráfico os dados para elas, temos um fenômeno que se parece com uma parabóla. Se eu tentar modelar esse fenômeno com uma reta (modelo linear), ele será bem ineficiente. Independentemente da reta queserá traçada, não será possível representar bem o modelo real que deu origem aos dados. Então, esse modelo é pouco flexível e portanto possui alto viés.

Agora se eu tentasse modelar esses dados com uma regressão polinomial de alto grau, ela conseguiria representar muito bem o fenômeno observado, então, é dito que esse modelo tem alta flexibilidade e pouco Bias.

No entanto, se fossemos calcular o erro dos modelos, veríamos que o erro do modelo linear PARA DADOS NÂO VISTOS é menor. A regressão polinomial "decorou" os dados de treino e para dados novos não se sai muito bem, já o modelo linear é consegue se dar melhor com dados não vistos pois é mais 'geral'.

Essa variação do erro entre os dados de treino e teste chama-se Variance.

O ideal é ter modelos que tenham baixo Bias e baixa Variance. Eles tem que ser flexíveis o suficiente para conseguir modelar o fenômeno mas não mais do que isso para não decorarem os dados e deve ter a capacidadede manter o erro constante para dados que ele já e viu e para dados que nunca viu.

Variance is the amount that the estimate of the target function will change if different training data was used.

The target function is estimated from the training data by a machine learning algorithm, so we should expect the algorithm to have some variance. Ideally, it should not change too much from one training dataset to the next, meaning that the algorithm is good at picking out the hidden underlying mapping between the inputs and the output variables.

You can see a general trend in the examples above:

Linear machine learning algorithms often have a high bias but a low variance.
Nonlinear machine learning algorithms often have a low bias but a high variance


## Como conseguir um modelo com baixo viés e variância?

## Vantagens e Desvantagens

Vantagens:
 * Interpretabilidade
 * Robusta contra Outliers (os cortes no espaço não são influenciados pelos outliers)
 * Treinamento rápido

Desvantagens:
 * Pode overfittar (se a árvore crescer muito)
 * Tomar cuidado com variáveis categóricas com alta cardinalidade
