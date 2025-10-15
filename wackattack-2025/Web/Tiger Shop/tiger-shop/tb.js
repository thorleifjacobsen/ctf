const { id, createClient } = require("tigerbeetle-node");
const process = require("process");
const { getRandomValues } = require("crypto");
const client = createClient({
  cluster_id: 0n,
  replica_addresses: [process.env.TB_ADDRESS || "3000"],
});

const DB_DATA = Object.freeze({
  ACCOUNT_CTF: 1337,
  ACCOUNT_STORE: 1338,

  ACCOUNT_STORE_IDS: {
    1: id(),
    2: id(),
  },

  LEDGER_PLAYGROUND: 1,
  LEDGER_WACK: 2,

  BUY_ITEM: 9999,

  SHOP_PASSWORD: getRandomValues(new BigInt64Array(1))[0],
});

const accountMeta = new Map();

async function initializeShop() {
  try {
    const shopAccount1 = {
      id: DB_DATA.ACCOUNT_STORE_IDS["1"],
      debits_pending: 0n,
      debits_posted: 0n,
      credits_pending: 0n,
      credits_posted: 0n,
      user_data_128:
        DB_DATA.SHOP_PASSWORD > 0
          ? DB_DATA.SHOP_PASSWORD
          : DB_DATA.SHOP_PASSWORD * BigInt(-1),
      user_data_64: 0n,
      user_data_32: 0,
      reserved: 0,
      ledger: DB_DATA.LEDGER_PLAYGROUND,
      code: DB_DATA.ACCOUNT_STORE,
      flags: 0,
      timestamp: 0n,
    };

    const shopAccount2 = {
      id: DB_DATA.ACCOUNT_STORE_IDS["2"],
      debits_pending: 0n,
      debits_posted: 0n,
      credits_pending: 0n,
      credits_posted: 0n,
      user_data_128:
        DB_DATA.SHOP_PASSWORD > 0
          ? DB_DATA.SHOP_PASSWORD
          : DB_DATA.SHOP_PASSWORD * BigInt(-1),
      user_data_64: 0n,
      user_data_32: 0,
      reserved: 0,
      ledger: DB_DATA.LEDGER_WACK,
      code: DB_DATA.ACCOUNT_STORE,
      flags: 0,
      timestamp: 0n,
    };

    const accountErrors = await client.createAccounts([
      shopAccount1,
      shopAccount2,
    ]);
    if (accountErrors.length) {
      console.error("Failed to create shop account:", accountErrors[0]);
      process.exit(1);
    }

    const accounts = await client.lookupAccounts([
      DB_DATA.ACCOUNT_STORE_IDS["1"],
      DB_DATA.ACCOUNT_STORE_IDS["2"],
    ]);

    console.info("Created store accounts:")
    console.info(accounts)
  } catch (error) {
    console.error("Failed to initialize shop:", error);
    process.exit(1);
  }
}

module.exports = {
  initializeShop,
  client,
  DB_DATA,
  accountMeta,
};
