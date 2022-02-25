# Documentation Quiz

Please visit the [docs](https://semesterly-v2.readthedocs.io/en/latest/index.html) and
answer the following questions.

1. What is the command I run to get the courses from Fall 2021?

    `python manage.py ingest jhu --years 2021 --terms Fall`

2. How do I then load those courses into my database?

    `python manage.py digest jhu`

3. How do I get a terminal running in my docker container?

    Opening the Docker explorer shoud show a list of three containers. Right clicking any of these should bring up the `Attach Shell` option. Selecting this option opens a terminal to the corresponding container.

4. Where do I store data such as passwords or secrets that I don’t want to commit?

    `semesterly/sensitive.py`

5. What is our stack?

    | Component          | Technology  | Style/Methodology |
    |--------------------|-------------|-------------------|
    | Database           | PostgreSQL  | Django ORM        |
    | Backend Framework  | Django      | pycodestyle/Black |
    | Frontend Framework | React/Redux | ESLint/Prettier   |
    | CSS Framework      | SCSS        | BEM/Airbnb        |

6. What branch do I create a new branch off of when developing?

    The `develop` branch.

7. If I want to start on a feature called myfeature, what should the branch name be?

    `feature/myfeature`

    What about if I want to refactor myreducer?

    `refactor/myreducer`

8. What is the preferred format for commit messages?

    The "Topic: Message" format. Messages should be in the imperative mood.

9. What linters do we run against our code?

    Prettier, ESLint, Black

10. What is the max line length set to?

    88 for both frontend and backend

11. What is a FeatureFlowView?

    A template that handles `GET` requests by rendering the homepage. Subclasses of `FeatureFlowView` can be made to create new views that pass different data with custom logic by overriding the `get_feature_flow()` method and the `.feature_name` class attribute.

When you are done answering the questions, create a PR for a discussion of your answers.
