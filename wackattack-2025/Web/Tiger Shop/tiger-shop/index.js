const express = require("express");
const { id } = require("tigerbeetle-node");
const process = require("process");
const path = require("path");

const { DB_DATA, client, initializeShop } = require("./tb");

const SHOP = [
  {
    name: "console_dream",
    value: "console.log('Hello world!')",
    price: BigInt(1),
    ledger: DB_DATA.LEDGER_PLAYGROUND,
  },
  {
    name: "biltema_burger",
    value: "🍔🍔🍔🍔",
    price: BigInt(77 + Math.floor(Math.random() * 40)),
    ledger: DB_DATA.LEDGER_PLAYGROUND,
  },
  {
    name: "flag",
    value: process.env.FLAG || "wack{}",
    price: BigInt(1337),
    ledger: DB_DATA.LEDGER_WACK,
  },
];

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

app.post("/accounts", async (req, res) => {
  const { ledger = DB_DATA.LEDGER_PLAYGROUND, pincode } = req.body;
  
  if (typeof pincode !== "string" || pincode.length < 16)
    throw Error("Please sign up with secure pincode");

  if (typeof ledger !== "string" || Number(ledger) === DB_DATA.LEDGER_WACK)
    throw Error("You are not allowed on the wack ledger.");

  // Give all users random ids (lol no, I am bad)
  const acctId = BigInt(Date.now());
  const acct = {
    id: acctId,
    debits_pending: 0n,
    debits_posted: 0n,
    credits_pending: 0n,
    credits_posted: 0n,
    user_data_128: BigInt(pincode),
    user_data_64: 0n,
    user_data_32: 0,
    reserved: 0,
    ledger: Number(ledger),
    code: DB_DATA.ACCOUNT_CTF,
    flags: 0,
    timestamp: 0n,
  };

  const accountErrors = await client.createAccounts([acct]);
  if (accountErrors.length) {
    const first = accountErrors[0];
    return res.status(400).json({
      error: `createAccount failed: ${first.result}`,
      detail: first,
    });
  }

  console.log("Created account with ID: " + acctId);
  return res.sendStatus(201);
});

app.post("/purchase", async (req, res) => {
  const { from, pincode, item } = req.body;

  const accounts = await client.lookupAccounts([BigInt(from)]);
  if (accounts.length !== 1) throw Error("Account does not exists");
  if (accounts[0].user_data_128 !== BigInt(pincode))
    throw Error("Wrong pincode for the account");

  const shopItem = SHOP.find((i) => i.name === item);

  const transfer = {
    id: id(),
    pending_id: 0n,
    debit_account_id: BigInt(from),
    credit_account_id: DB_DATA.ACCOUNT_STORE_IDS[shopItem.ledger.toString()],
    amount: shopItem.price,
    user_data_128: 0n,
    user_data_64: 0n,
    user_data_32: 0,
    timeout: 0,
    ledger: shopItem.ledger,
    code: DB_DATA.BUY_ITEM,
    timestamp: 0n,
    flags: 0,
  };

  const transferErrors = await client.createTransfers([transfer]);
  if (transferErrors.length) {
    const first = transferErrors[0];
    return res.status(400).json({
      error: `Purchase failed: ${first.result}`,
      detail: first,
    });
  }

  return res.json({
    success: true,
    message: `Successfully purchased ${item}`,
    item: shopItem.value,
  });
});

const PORT = process.env.PORT || 3001;
(async () => {
  await initializeShop();
  app.listen(PORT, () => {
    console.log(`Wild Tiger running on http://localhost:${PORT}`);
  });
})();
