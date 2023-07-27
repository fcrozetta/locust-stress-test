# locust-stress-test

This is the repository that contains the code for the API and locust programs.

## Quickstart

If you have docker, vscode and devcontainers extension, open the project in vscode, and click to open in devcontainers.

devcontainers will do the following:

- create a linux container
- install poetry
- configure poetry to create virtual environments in the project folder
- create a python environment, install the needed packages

Additionally, .vscode has the settings and launch files which contains black configurations and the launch command ready, with the reload argument so every change in the API will be updated in real time

If you are not using vscode and/or devcontainers,
you will need to install everything manually, and start the api with the command

```bash
uvicorn api.main:app --reload
```
The API will be served on [your localhost](http://127.0.0.1:8000/docs)


## Running locust

to run the existing locust file with the sample user that calls a failing endpoint, you can use the command:

```bash
# Locust
locust -f ./locust/locust.py -h http://localhost:8000
```
This will start locust in the [web GUI mode](http://localhost:8089). If you want to execute it via CLI, use the command:

```bash
locust -f ./locust/locust.py -h http://localhost:8000 --headless --users 10 --spawn-rate 1 -t 30m -s 1m
```
> *Note:* You can add other arguments in this command, to customize it to your needs.

To check other possible arguments, refer to the [official documentation](https://docs.locust.io/en/stable/index.html), or using the command:

```bash
locust --help
```

## Locust

Locust is a performance/stress testing tool created for use at EA/DICE, for a a game called Battlefield, but now is used by many other organizations.

[This tool was created because the developers always find limitations when scripting tests using other tools](https://docs.locust.io/en/stable/history.html#history). Then they created one that runs in python, so not only it is expandable, but a new language is **not** necessary to make it run.