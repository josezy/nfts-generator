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

### EC2 instance commands

```fish
python main.py {bisping,rooney,etc...} --generate --multiprocess
```


## Candy machine setup

Required tools Solana CLI

[Metaplex Candy Machine + Custom SPL Token](https://docs.google.com/document/d/1ZJsbLJXKCAqUsOU6a0Jk-yOuSYi-uOMYdQZIILGsvxE/mobilebasic)

#### SPL token creation
```
spl-token create-token --decimals 0 > token-output.txt
spl-token create-account <TOKEN> > account-treasury.txt
spl-token mint <TOKEN> 10000 <ACCOUNT>
spl-token authorize <TOKEN> mint --disable
```

### Transfer SPL tokens
```
spl-token transfer --fee-payer ~/.config/solana/devnet.json <TOKEN> <AMOUNT> <DEST_ADDRESS>
```

#### Creating the Candy Machine
```
ts-node src/candy-machine-cli.ts upload -e mainnet-beta -k ~/.config/solana/id.json -c cache001 ./path/to/assets
cat .cache/mainnet-beta-cache001  // config address

ts-node src/candy-machine-cli.ts create_candy_machine -e mainnet-beta -k ~/.config/solana/id.json -c cache001 --spl-token <TOKEN> --spl-token-account <ACCOUNT> // candy machine address

ts-node src/candy-machine-cli.ts update_candy_machine -e mainnet-beta -k ~/.config/solana/id.json -c cache001 -d "now" // or any time

ts-node src/candy-machine-cli.ts verify -e mainnet-beta -k ~/.config/solana/id.json -c cache001
ts-node src/candy-machine-cli.ts show -e mainnet-beta -k ~/.config/solana/id.json -c cache001
```
