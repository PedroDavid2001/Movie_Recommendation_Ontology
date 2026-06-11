# Movie Recommendation Ontology

## 1. Description

### 🇧🇷 Português

Ontologia simples utilizada como exemplo no tutorial de Owlready2.

A ontologia foi modelada em OntoUML utilizando o plugin de mesmo nome disponível no Visual Paradigm. Em seguida, o modelo foi exportado para o formato Turtle e refinado no Protégé. Por fim, a ontologia foi exportada em RDF/XML para ser manipulada em um ambiente Python por meio da biblioteca Owlready2.

O principal objetivo deste exemplo é demonstrar a integração entre diferentes ferramentas para modelagem conceitual, criação e manipulação de instâncias, bem como a execução de consultas SPARQL sobre uma ontologia.

### 🇺🇸 English

A simple ontology used as an example in the Owlready2 tutorial.

The ontology was modeled in OntoUML using the corresponding Visual Paradigm plugin. The model was then exported to Turtle format and refined in Protégé. Finally, the ontology was exported as RDF/XML and manipulated in a Python environment using the Owlready2 library.

The main objective of this example is to demonstrate the integration of different tools for conceptual modeling, instance creation and manipulation, as well as the execution of SPARQL queries on an ontology.

---

## 2. OntoUML Views

The ontology was divided into three main views to facilitate understanding and maintenance of the conceptual model.

### 2.1 Movie Recommendation Overview

> General overview of the recommendation domain, including users, movies, genres, and recommendation-related concepts.

<p align="center">
  <img src="docs/images/movie_recommendation_overview.png" width="800">
</p>

---

### 2.2 User–Movie Relation

> View responsible for representing social relationships between users and their genre preferences.

<p align="center">
  <img src="docs/images/user_movie_relation.png" width="800">
</p>

---

### 2.3 Movie Genres

> View responsible for representing movie genres and genre-based movie classification.

<p align="center">
  <img src="docs/images/movie_genres.png" width="800">
</p>

---

## 3. Important Links

* gUFO: <https://nemo-ufes.github.io/gufo/>
* Owlready2: <https://owlready2.readthedocs.io/en/v0.50/intro.html>
