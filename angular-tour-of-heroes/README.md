## Table of contents

- [Requirements](#requirements)
  - [Work with a memory web api server:](#work-with-a-memory-web-api-server)
  - [Work with Flask](#work-with-flask)
- [Resources](#resources)


## Requirements

### Work with a memory web api server:

```bash
npm install angular-in-memory-web-api --save
```

### Work with Flask

Note. Not all the hero methods (add, update, delete...) are implemented.

Modify the following files: 

- `src/app/app.module.ts`. Comment these lines:

```bash
    //HttpClientInMemoryWebApiModule.forRoot(
    //  InMemoryDataService, { dataEncapsulation: false }
    //)
```

- `src/app/hero.service.ts`. Comment and uncomment these lines:

```bash
  //private heroesUrl = 'api/heroes';  // URL to web api
  private heroesUrl = 'http://127.0.0.1:5000/api/heroes';
```

Install the `requirements.txt` file and run the Flask app:

```bash
  python src/flask_/app.py
```

Run the angular app as usual.


## Resources

- Tutorial
  <https://angular.io/tutorial>

- In-memory Web API package
  <https://angular.io/tutorial/toh-pt6>
