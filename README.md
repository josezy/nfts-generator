# Candy Machine assets generator

Virtual env and libraries:
```bash
virtualenv -p (which python3.9) .venv
source .venv/bin/activate
pip install -r requirements.txt
```

NOTE: Make sure to place PSD file at root dir and name it `base.psd`

to use the script:
1. Create traits list with `python main.py --count 1`
2. Generate assets with `python main.py --generate`
