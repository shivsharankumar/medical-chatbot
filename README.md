# medical-chatbot

# How to run?
### STEPS:

clone the repository

```bash
https://github.com/shivsharankumar/medical-chatbot.git
```

### STEP 01- CREATE an environment using UV
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
### STEP 02- initialize the environment
```bash
uv init
```
### STEP 03- activate environment
```bash
source .venv/bin/activate
```
### STEP 04- install dependencies
```bash
uv sync
```
or
### STEP 04- install dependencies (requirements.txt)
```bash
uv add -r requirements.txt
```