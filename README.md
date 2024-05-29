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

|      Homepage      |      Recommendation page      |
| :----------------: | :---------------------------: |
| <img src="docs/images/homepage.gif" title="Home Page" width="25%"> | <img src="docs/images/recommendation.gif" title="Login Page" width="25%"> |

</details>

</td></tr></table>

### Built With

We used the Django framework to build the website, it is connected to an sqlite database that stores users data and movies data. The data gathering, filtering and processing was done using Python librairies like BeautifulSoup and Pandas. Lastly the NLP and the recommendation system were built using python librairies like nltk, Spacy and Sci-kit learn.

## Getting Started

### Prerequisites

All of the reauirements can be found in the requirements.txt file.

### Installation

You have to download the project, install the reauirements using pip install -r requirements.txt, and first execute the python script generate_reco as the file was too big to store using the command : python manage.py runscript -v2 generate_reco in the cinepolis repository. Then execute this code in the django-admin shell command :
```
from django.core.management.utils import get_random_secret_key  
get_random_secret_key()
```

to generate a new secret key and store it in a .env file in the cinepolis folder.
## Usage

 Once you have it installed, you only have to run the runserver command like this : python manage.py runserver and find the perfect movie for you !


## Authors & contributors

The original setup of this repository is by [Quentin Bernardin](https://github.com/Phebos), [Abdelatif Touati](https://github.com/2501Pr0ject) and [Blandine Buffin](https://www.linkedin.com/in/blandine-buffin-a871a1249/)
