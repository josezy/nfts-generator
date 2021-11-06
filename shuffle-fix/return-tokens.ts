import fs from 'fs';
import { execSync } from "child_process";

import holders from './holders.json'

const TOKEN = 'Aj2HHSuPg1WmyAa6eAyS2uamESPomsoGsi56LXjNyXrb'
const AMOUNT = 1 // KEEP ONE TOKEN PER ACCOUNT
const KEYPAIR = '~/.config/solana/legends.json'

const RUST_PATH = '~/Desktop/blockasset/metaplex/rust/target/debug'
const RPC_ENDPOINT = 'https://cmnftdrop7299eedc071c.genesysgo.net/'

const new_md_name = 'Exiled Lomus'

for (const holder of holders) {

  if (!holder['metadataUpdated']) {
    console.log(`Updating metadata for mint ${holder.mint_account}`)
    const metadataCmd = `${RUST_PATH}/metaplex-token-metadata-test-client update_metadata_accounts --url ${RPC_ENDPOINT} --mint ${holder.mint_account} --keypair ${KEYPAIR} --name ${new_md_name}`
    try {
      const resultMd = execSync(metadataCmd)
      console.log(resultMd)
      holder['metadataUpdated'] = true
    } catch(e) {
      holder['metadataUpdated'] = false
    }
  }

  // if (!holder['tokenReturned']) {
  //   console.log(`Returning token to ${holder.owner_wallet}`)
  //   try {
  //     const tokenCmd = `spl-token transfer --fund-recipient --fee-payer ${KEYPAIR} ${TOKEN} ${AMOUNT} ${holder.owner_wallet}`
  //     const resultToken = execSync(tokenCmd)
  //     console.log(resultToken)
  //     holder['tokenReturned'] = true
  //   } catch(e) {
  //     holder['tokenReturned'] = false
  //   }
  // }

  fs.writeFileSync('./processed_holders.json', JSON.stringify(holders));
}

