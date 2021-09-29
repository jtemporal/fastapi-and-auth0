# Protecting your FastAPI API with Auth0

## Running the example

In order to run the example you need to have `python3` (any version higher than `3.6`) and `pip3` installed, you'll also need an Auth0 account, [you can get your Auth0 account for free here](https://a0.to/jtemporal-signup-for-auth0).

### Configuration

The configuration you'll need is mostly information from Auth0, you'll need both the tentant domain and the API information.

This app reads its configuration information from a `.config` file by default.

To create a `.config` file you can copy the `.example.config` file and fill the values accordingly:

```console
cp .example.config .config
# update the config file for the correct values
export ENV='.config'
```

You can change this behavior by setting the following environment variables (remember to update the values accordingly):

```console
export ENV='variables'
export DOMAIN='your.domain.auth0.com'
export API_AUDIENCE='your.api.audience'
export ISSUER='https://your.domain.auth0.com'
export ALGORITHMS='RS256'
```

### Spin up the server

Once you've set your environment information below you'll find the commands you'll need.

1. Create and activate a python environment:

```console
python3 -m venv .env
source .env/bin/bash
```

2. Install the needed dependencies with:

```console
pip install -r requirements.txt
```
3. Start the server with the following:

```console
uvicorn application.main:app
```

4. Try calling [http://localhost:8000/api/public](http://localhost:8000/api/public)

```
curl -X 'GET' \
  'http://localhost:8000/api/public' \
  -H 'accept: application/json'
```

## API documentation

Access [http://localhost:8000/docs](http://localhost:8000/docs). From there you'll see all endpoints and can test your API

## Examples in this repo

| Branch name | Example |
| ----------- | ------- |
| `main` | The starter sample only has two endpoints and one of them needs protection |
| `private` | The result of protecting the first endpoint with Auth0 |
| `private-scoped` | Implemented a protected endpoint with checks for scopes |
