# fastapi-rag-template
This is a template repository to run a FastAPI based retreival-augmented generation (RAG) backend application using langgraph and langchain.
It uses a credit card dataset (scraped from nerdwallet.com) to create the knowledge base for the bot,loads the documents to a vector store,
and creates a QA bot to answer user queries about credit cards. You can customize this template to your RAG use case.

This template currently supports being run:

-   Locally using [uvicorn](https://www.uvicorn.org/)

---

## Documentation Links

### Libraries

-   [FastAPI](https://fastapi.tiangolo.com/) 
-   [pydantic](https://pydantic-docs.helpmanual.io/)
-   [langchain](https://www.langchain.com) 
-   [langgraph](https://www.langchain.com/langgraph)

If you want to learn the basics of these frameworks, I have provided links in the resources section down below.


## Get Started

You're going to need the prerequisite:

-   [Python 3.9+](https://www.python.org/downloads/)

To find the version of your Python installation run:

```zsh
python3 --version
```

### Create the Project

First, fork this repo:

-   Navigate to this repo on GitHub
-   In the top-right corner of the page, click "Fork"

If you wish to rename your fork, do it now.

Then, clone the fork to your local device:

-   Navigate to your fork
-   Above the list of files, click the green "Code" button
-   Either copy the link manually or click the 📋 next to it
-   Open your favorite terminal and `cd` into the directory you want your project located
-   Run `git clone [Link You Copied]`
-   `cd` into the newly created directory

### Virtual Enviroment


To create your virtual enviroment run:

```zsh
python3 -m venv venv
```

On MacOS and Linux run the following to activate:
```zsh
source venv/bin/activate
```

On Windows run:
```cmd
venv\Scripts\activate.bat
```
On both platforms, if you wish to deactivate the virtual enviroment run:
```zsh
deactivate
```

Everytime you open a new terminal you'll need to activate the virtual enviroment.

### Dependencies

To start, you'll need to install the provided dependencies. This can be done by running:

```zsh
pip install -r dev-requirements.txt
```

### Code Structure

`__init__.py` defines and initializes the app configuration.

`app/main.py` defines the FastAPI application

`app/rag` creates the langgraph agent

`models/` is the space to define input, output and database models. I have defined the langgraph state graph shared class in there.

`etl/` (optional) cleans and converts the credit card dataset from excel to json.

Now, you might want to spend a little bit of time starting at `main.py` and looking through the code to see how it's structured in practice. Once your done, and you want to delete the example code:


### Running Locally


Export your OPENAI_API_KEY env variable (you can create one [here](https://platform.openai.com/api-keys))
```zsh
export OPENAI_API_KEY=Your API Key
```


Then run uvicorn from the root of your project using:

```zsh
uvicorn app.main:app --reload
```

This will host your API on `localhost` bound to port `8000` by default. When you update and save a file it will automatically reload.

Then visit [URL](http://localhost:8000/docs), click "Try it out", enter your query and username and hit execute.
![Query](/.github/images/query.png?raw=true "Query example")

You will see the AI generated response in the Response section below:
![Response](/.github/images/response.png?raw=true "Response")

## Resources
-   [langchain](https://python.langchain.com/docs/tutorials/)
-   [langgraph](https://academy.langchain.com/courses/intro-to-langgraph)
-   [RAG](https://python.langchain.com/docs/tutorials/rag/)
-   [fastapi](https://www.tutorialspoint.com/fastapi/index.htm)

## Contribute
If you would like to contribute to this template please open an PR.
Scope:
- add docker and kubernetes deployment options
- add a standalone vector store (currently using in-memory vector store)
- store and recall user chat history when generating responses
- add more credit card information

If you found this repo useful please star and cite it!!