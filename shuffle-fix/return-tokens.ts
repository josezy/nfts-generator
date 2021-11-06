import { execSync } from "child_process";
import fs from 'fs';

import holders from './holders.json'

const TOKEN = 'Aj2HHSuPg1WmyAa6eAyS2uamESPomsoGsi56LXjNyXrb'
const AMOUNT = 1 // KEEP ONE TOKEN PER ACCOUNT
const FEE_PAYER = '~/.config/solana/legends.json'


for (const holder of holders) {
  console.log(`Returning token to ${holder.owner_wallet}`)
  const cmd = `spl-token transfer --fee-payer ${FEE_PAYER} ${TOKEN} ${AMOUNT} ${holder.owner_wallet}`
  try {
    const result = execSync(cmd)
    console.log(result)
    holder['success'] = true
  } catch(e) {
    holder['success'] = false
  }

  fs.writeFileSync('./output.json', JSON.stringify(holders));
}



