<h1 align="center">
  <a href="https://github.com/Phebos/cinepolis">
    <!-- Please provide path to your logo here -->
    <img src="docs/images/logo.png" alt="Logo" width="100" height="100">
  </a>
</h1>

<div align="center">
  cinepolis
  <br />
  <a href="#about"><strong>Explore the screenshots »</strong></a>
  <br />
  <br />
</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Authors & contributors](#authors--contributors)
</details>

---

## About

<table><tr><td>

The goal of this project was to put to use what we learnt about NLP and machine learning in a fun project : a movie recommendation system. We decided to focus on Asian cinema as it is globally less represented and deserves some appreciation.
Bored and don't know what to watch ? This recommendation system is the perfect tool for you

<details>
<summary>Screenshots</summary>
<br>

|                               Homepage                               |                               Recommendation page                               |
| :-------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| <img src="docs/images/homepage.gif" title="Home Page" width="100%"> | <img src="docs/images/recommendation.gif" title="Login Page" width="75%"> |

</details>

</td></tr></table>

### Built With

We used the Django framework to built the website, it is connected to an sqlite database that stores data about the users account and the movies. The data gathering, filtering and processing was done using Python librairies like BeautifulSoup and Pandas. Lastly the NLP and the recommendation system were built using python librairies like nltk, Spacy and Sci-kit learn.

## Getting Started

### Prerequisites

All of the reauirements can be found in the requirements.txt file.

### Installation

You just have to download the project, install the reauirements using pip install -r requirements.txt, and first execute the python script generate_reco as the file was too big to store using the command : python manage.py runscript -v2 generate_reco in the cinepolis repository.

## Usage

 Once you installed it, you only have to run the runserver command like this : python manage.py runserver and find the perfect movie for you !


## Authors & contributors

The original setup of this repository is by [Quentin Bernardin](https://github.com/Phebos), [Abdelatif Touati](https://github.com/Phebos) and [Blandine Buffin](https://github.com/Phebos)
