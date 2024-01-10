## 🤔 O que é a APS ?
As Atividades Práticas Supervisionadas (**APS**) são trabalhos que ocorrem a cada semestre, nos quais o tema e o orientador são diferentes. Assim, a cada semestre, uma APS é aplicada com um tema diferente sendo proposto.
</br>
O foco da APS em Ciência da Computação é estimular os alunos a aprimorar as habilidades desenvolvidas durante as aulas e os laboratórios ao longo da semana. Com o passar do tempo, os projetos e os temas propostos tendem a se tornar mais desafiadores.

## 🚩 Sobre o projeto
No decorrer do semestre, foi proposto o desenvolvimento de um algoritmo capaz de identificar regiões desmatadas e não desmatadas na Amazônia, utilizando imagens de satélite.
</br></br>
O primeiro projeto envolveu o uso de filtros nas imagens, o que possibilitou o reconhecimento de determinadas regiões desmatadas. No entanto, em alguns pontos, especialmente onde havia um grande volume de sombras ou semelhanças na cor com os rios, tornava-se incerto determinar se a região estava desmatada ou não.
</br></br>
Devido a esse desafio, após a aplicação dos filtros, foi proposto a nós o desafio de criar um modelo de aprendizado de máquina capaz de reconhecer regiões desmatadas com a maior precisão possível.

## ⚠️ Observações sobre o projeto
Conforme descrito anteriormente, o primeiro projeto envolveu apenas o uso de filtros para detectar padrões de desmatamento. Dado que este repositório tem como foco principal o uso de redes neurais, decidimos disponibilizar apenas o código fonte da rede.

## 🧰 Ferramentas utilizadas
Segue de forma simples uma lista e uma breve descrição sobre a ferramenta:

- 🐍 **Python** </br>
O foco do uso desta linguagem está no fato que possui uma grande biblioteca, facilitando a implementação de recursos como o processamento de imagem e nas redes neurais.

- 🗺️ **IMPE - site** </br>
Foram retirados imagens do satélite Amazonia1 e entre outros disponíveis através do site [oficial dele](http://www.dgi.inpe.br/catalogo/explore).

- 🌎 **Qgis - software** </br>
Software Open-Source focado em análise, visualização e georreferência, contudo foi utilizado para mesclar camadas das imagens via satélite.</br>
É possível acessar o [site por aqui](https://qgis.org/pt_BR/site/).

#### 📚 Bibliotecas utilizadas

- 🤖 **Tensorflow & Keras** </br>
Biblioteca de código aberto focado em aprendizado de máquina e Keras consegue rodar em cima de Tensorflow, permitindo uma maior agilidade e praticidade na construção de redes profundas. Facilitando o desenvolvimento do projeto.

- 📊 **Matplotlib** </br>
Matplot é capaz de gerar inúmeros gráficos, até mesmo gráficos animados, neste sentido foi utilizado o Matplot para gerar gráficos e resultados obtidos através das imagens.

- 🧮 **Numpy** </br>
Focada em calculos e operações matemáticas, foi utilizada para criar matrizes com o foco de exibir as imagens e fazendo a predição da rede.

- 🖼️ **OpenCV** </br>
Utilizada no processamento de imagens, visão computacional e no uso do aprendizado de máquina.
</br>
Foi utilizada para carregar as imagens e exibir nos gráficos.

- 💻 **OS** </br>
Biblioteca padrão do Python ela oferece as funcionalidades que integram o sistema operacional.
</br>
Seu principal uso está na implementação do dataset.

## 📈 Resultados e conclusões.

## 👀 Observação