# Procesamiento de Lenguaje Natural I

**Autor:** Gonzalo G. Fernandez <fernandez.gfg@gmail.com>

Resolución de desafíos propuestos en la cátegrada Procesamiento de Lenguaje Natural I de la Carrera de Especialización en Inteligencia Artificial (FIUBA).

## Desafío 1: Vectorización de texto

**Notebook:** [1-vectorizacion_de_texto.ipynb](./1-vectorizacion_de_texto.ipynb)

Exploración de técnicas de preprocesamiento de texto y métodos para convertir texto crudo en representaciones numéricas.
- Tokenización y eliminación de stopwords
- Representación Bag-of-Words y TF-IDF con CountVectorizer y TfidfVectorizer
- Análisis básico de matrices documento-término

## Desafío 2: Word Embeddings

**Notebook:** [2-word_embeddings.ipynb](./2-word_embeddings.ipynb)

Introducción a *word embeddings*, vectores densos que capturan relaciones semánticas entre palabras. Se aborda:
- Uso de embeddings preentrenados (Word2Vec y GloVe)
- Entrenamiento de embeddings personalizados con gensim
- Visualización de relaciones entre palabras con PCA

El corpus de texto utilizado corresponde a los diálogos en la película argentina "Nueve Reinas" de Fabián Bielinsky.

## Desafío 3: Modelos de lenguaje

**Notebook:** [3-modelo_de_lenguaje.ipynb](./3-modelo_de_lenguaje.ipynb)

Implementación de modelos de lenguaje a nivel de carácter utilizando RNNs. Incluye:
- Generación de secuencias para entrenamiento
- Codificación one-hot de caracteres
- Construcción y entrenamiento de una RNN con keras
- Generación de texto basada en el modelo aprendido

El corpus de texto utilizado corresponde a los diálogos en la película argentina "Nueve Reinas" de Fabián Bielinsky.

Los modelos estuadiados son SimpleRNN, LSTM y GRU. Para todos se realizó una búsqueda de hiperparámetros utilzando `keras-tuner`.

## Requerimientos

Para la correcta ejecución de los diferentes notebook se necesita contar con las librerías utilizadas. Las mismas pueden instalarse de la siguiente forma:

```bash
pip install -r requirements.txt
```

Se sugiere ejecutar la instalación dentro de un entorno virtual de python. El mismo puede configurarse mediante los siguientes comandos:

```bash
python3 -m venv .venv
source .venv/bin/activate
```