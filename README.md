[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/2sZOX9xt)
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
  </a>

  <h3 align="center">Log Ingestor and Query Interface</h3>

  <p align="center">
    Develop a log ingestor system that can efficiently handle vast volumes of log data, and offer a simple interface for querying this data using full-text search or specific field filters.
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#features-implemented">Features Implemented</a></li>
	  <li><a href="#evaluation-criteria-met">Evaluation Criteria Met</a></li>
    <li><a href="#identified-issue">Identified Issues</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Developed a log ingestor system that can efficiently handle vast volumes of log data, and offer a simple interface for querying this data using full-text search or specific field filters.

The logs should be ingested (in the log ingestor) over HTTP, on port `3000`.

The logs to be ingested will be sent in this format.

```json
{
	"level": "error",
	"message": "Failed to connect to DB",
  "resourceId": "server-1234",
	"timestamp": "2023-09-15T08:00:00Z",
	"traceId": "abc-xyz-123",
  "spanId": "span-456",
  "commit": "5e5342f",
  "metadata": {
      "parentResourceId": "server-0987"
    }
}
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

The project is built using FastAPI, MongoDB and RabbitMQ

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To setup this project the below mwntioned steps need to be followed.

### Prerequisites

* Python should be installed
  ```sh
  python --version
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/dyte-submissions/november-2023-hiring-tawheed78.git
   ```
2. Go to directory
   ```sh
   cd november-2023-hiring-tawheed78
   ```
3. Setup virtual environment
   ```sh
   py -m venv venv
   venv/Scripts/activate
   ```
4. Install requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
5. Start the main server that ingests logs in one terminal
   ```sh
    uvicorn main:app --host 127.0.0.1 --port 3000 --reload 
   ```
6. Start the consumer server in another terminal that consumes the messages received from RabbitMQ
   ```sh
    python consumer.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Usage

### Log Ingestor

The Log Ingestor uses FastAPI to ingest logs via POST request. The Logs are sent to RabbitMQ and then processed from there one by one and added into Mongodb database.

1. Send a POST request with the log data to "http://127.0.0.1:3000/ingest/"

2. You will receive a message in the consumer terminal mentioning
   ```json
	[✅] Received: {'level': 'error', 'message': 'Failed to connect to DB', 'resourceId': 'server-1234', 'timestamp': 1694764800, 'traceId': 'abc-xyz-123', 'spanId': 'span-456', 'commit': '5e5342f', 'metadata': {'parentResourceId': 'server-0987'}}
   ```
3. At the same time the log has been added to the Mongodb Database.


### Query Interface

The Query Interface uses HTML template to take the input values, "Filter Field" and "Filter Value". On submitting the response the data is fetched from the Mongodb Database and presented in a table just below the input form. Additionally indexing has been done on the fields "level", "timestamp", "message", "resourceId" only as more the indexing leads to more load on the read write operation of database.

1. Go over to "http://127.0.0.1:3000/"
2. Enter the Filter field and the Filter value and click Search.
3. A Table will get populated below with the respective logs.

### Points to be Noted
1. Since I have used cloud MongoDB and cloud RabbitMQ, I have provided the connection string and url of those instances in the .env file for testing purposes so that setting that up doesn't create any problems.

   
## Features Implemented
Log Ingestor:

- Ingests logs over HTTP on port 3000. ("http://127.0.0.1:3000/ingest/")
- Sends logs to RabbitMQ and stores in the queue and processes each log and stores in Mongodb Database.
  
Query Interface:

- HTML template for user interaction.
- Searching logs based on filters => (level, message, resourceId, timestamp etc)
- Also implemented Date range search, regular expression search.
- Additionally created a db_factory.py which resembles the factory pattern for selecting database for further operations. Due to time constraints couldn't implement that but the code is available in the repo.
  
Advanced Features (Bonus):

- Date range search in Query Interface.
  For date range search use Filter Field : dateRange  and  Filter value: (should be in the format) 2023-09-10T00:00:00Z and 2023-09-15T23:59:59Z.
  For this filter I have converted the date to unix timestamp before storing in database as those formats provide faster operations instead of UTC formats.
- Regular expression search in Query Interface.


## Evaluation Criteria Met
1. **Volume**: Handles massive log volumes efficiently with the help of LavinMQ(aka RabbitMQ) which can provide a throughput of about 1,000,000 messages/sec.
2. **Speed**: Provides quick search results as the data is indexed.
3. **Scalability**: Adaptable to increasing log volumes and queries.
4. **Usability**: Offers an intuitive and user friendly interface.
5. **Advanced Features**: Implemented bonus functionalities.
6. **Readability**: Maintained a clean and structured codebase.


## Identified Issues
- **Real-time Capabilities**: Enhance real-time log ingestion and search.
- **Sharding**: The Mongodb Atlas Free cluster does not provide sharding feature, although the paid cluster provides, hence sharding the database is achievable.
- **Security**: Proving role based access to query the database.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@linked_profile](https://www.linkedin.com/in/tawheedchilwan78/) - tawheed.chilwan55@gmail.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
