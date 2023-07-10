# Five Personality Traits (OCEAN) Prediction using Machine Learning
Este é um projeto de Machine Learning que tem como objetivo prever os traços de personalidade de uma pessoa com base nos Five Personality Traits, também conhecidos como OCEAN (Openness to experience, Conscientiousness, Extroversion, Agreeableness, Neuroticism).

## Descrição
O modelo desenvolvido neste projeto utiliza técnicas de aprendizado de máquina para prever os traços de personalidade com base em um conjunto de características fornecidas pelo usuário. Os traços de personalidade são definidos da seguinte forma:

1. **Openness to experience**: Indica se a pessoa é mais inclinada a ser aberta, curiosa e disposta a experimentar coisas novas, ou se é mais consistente e cautelosa em suas ações.
2. **Conscientiousness**: Reflete se a pessoa é mais eficiente, organizada e orientada a resultados, ou se é mais descontraída e descuidada em suas atividades.
3. **Extroversion**: Avalia se a pessoa é mais extrovertida, energética e sociável, ou se é mais reservada e introvertida.
4. **Agreeableness**: Determina se a pessoa é mais amigável, compassiva e cooperativa, ou se é mais desafiadora e distante em suas interações sociais.
5. **Neuroticism**: Indica se a pessoa é mais sensível, nervosa e propensa à ansiedade, ou se é mais segura e confiante em suas emoções e reações.

## Bibliotecas Utilizadas

- numpy
- pandas
- matplotlib
- seaborn
- io
- yellowbrick
- sklearn.cluster
- gradio

## Passo a passo
1. Importação da base de dados
2. Verificação da base de dados
3. Limpeza da base de dados
4. Análise estatística da base de dados
5. Instanciando o método KMeans e o Vizualizer
6. Selecionando uma amostra aleatória dos dados com 5000 observações
7. Executando o teste
8. Agrupando os participantes em 5 grupos
9. Atribuindo os registros aos devidos grupos
10. Inserindo os rótulos dos clusters no dataframe
12. Analisando os grupos
13. Agrupando os registros por grupos
14. Calculando a média de cada grupo de questões para verificar um padrão
15. Visualizando as médias por grupo
16. Instalando a biblioteca Gradio
17. Importando as questões a partir de um ficheiro de texto
18. Verificando os dados
19. Limpando os dados e recuperando apenas as questões
20. Criando os inputs dinâmicos para passar ao Gradio

## Funcionalidades
O projeto utiliza a biblioteca Gradio para criar uma interface interativa para o teste de previsão dos traços de personalidade. Através dessa interface, o usuário pode fornecer os valores de cada uma das características (Openness, Conscientiousness, Extroversion, Agreeableness e Neuroticism) e obter as previsões dos traços de personalidade correspondentes.

## Conclusão
Este projeto de Machine Learning oferece uma interface amigável para prever os traços de personalidade de uma pessoa com base nos Five Personality Traits (OCEAN). Utilizando a biblioteca Gradio, os usuários podem facilmente fornecer as características e receber previsões imediatas. Esperamos que este projeto seja útil para a compreensão e aplicação dos conceitos de previsão de traços de personalidade e possa ser personalizado e aprimorado para atender às necessidades específicas de diferentes usuários.
