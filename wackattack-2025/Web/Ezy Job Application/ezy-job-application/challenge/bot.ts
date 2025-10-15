import puppeteer from 'puppeteer';
import { parseArgs } from "util";

const { values } = parseArgs({
    args: process.argv.slice(2),
    options: {
        registrationId: {
            type: 'string',
        },
    },
    strict: true,
    allowPositionals: true,
});

const registrationId = values.registrationId;

if (!registrationId) {
    console.error('Usage: node bot.js --registrationId <registrationId>');
    process.exit(1);
}

(async () => {
    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox', "--js-flags=--noexpose_wasm,--jitless"],
    });

    const page = await browser.newPage();

    try {
        // Visit user note
        await page.goto(`http://127.0.0.1:8080/admin/registration/${registrationId}`, {  waitUntil: 'networkidle0', timeout: 60_000 }); 

        // Wait for 1 seconds
        await new Promise(function(resolve) { 
            setTimeout(resolve, 2000)
        });

        console.log('Puppeteer script executed successfully.');
    } catch (error) {
        console.error('Error running Puppeteer script:', error);
        process.exit(1);
    } finally {
        await browser.close();
    }
})();