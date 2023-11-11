# Gamblealven

Alvmalie er ansvarlig for polkagrisene og sukkerstengene til nissen. Hvert år brukes det mange polkagriser i julestrømper rundt om i verden, i tillegg til sukkerstenger som også brukes til å pynte både juleverkstedet og huset til nissen. Alvmalie elsker sukkerstenger, og synes det skal være mange av dem - overalt. Så når hun oppdager at det lokale bettingselskapet på Nordpolen, NorthPoleInOne, godtar innsats i sukkerstenger, får hun en idè til å øke antall sukkerstenger fra de 50 000 hun har.

Alvmalie er nemlig også veldig fotballinteressert, og fikk med seg at Alvin Braut Fortann byttet klubb fra Borussia Weinachtsbaum til Reinchester City. Og da tok planen hennes form. Hun ville satse sukkerstenger på hvor mange mål Alvin scoret, og på den måten fylle opp lageret. Fordi hun ville være på den sikre siden, satte hun opp 2 regler hun alltid ville følge:

Hun satset alltid 17,5 % av det hun til enhver tid hadde, rundet av til nærmeste heltall (0.49 = 0, 0.50 = 1)
Hun satset alltid på minst hvor mange mål Braut Fortann scoret i alle kampene den sesongen. Dvs at hvis hun satset på 2 mål, ville hun vinne hvis Fortann scoret 2 eller flere mål, men tape hvis Fortann scoret 0 eller 1 mål.
NorthPoleInOne bestemte oddsen, basert på hvor mange mål Alvmalie var villig til å tippe på, så jo flere mål hun tippet at Braut Fortann skulle score, jo høyere ville en potensiell gevinst bli. Eventuell gevinst ble utbetalt hver runde, rundet av til nærmeste heltall.

Når julaften nærmet seg, skulle nissen hente ut alle sukkerstengene, og oppdaget at det var veldig mange færre enn antatt. Han spurte Alvmalie, som tilstod med en gang. Julenissen trenger nå å vite hvor mange ekstra sukkerstenger som må produseres for å få riktig antall til dekorasjonene. Han har følgende ledetråder:

- [Oversikt over antall mål Fortann scoret i hver kamp](goals.txt)

- [Oversikt over antall mål Alvmalie gjettet på, og hvilken odds NorthPoleInOne ga henne for antallet hun gjettet på](bets.txt)

Hvor mange sukkerstenger har Alvmalie tapt?

# Solution

```javascript
const goals = [2,0,1,3,3,1,2,1,1,3,2,1,0,0,2,0,0,0,1,0,0,1,2,1,0,0,0,0,1,3,0,0,0,1,0,0,1,0,0,1,5,3,0,2,1,2,1,0,1,1,1,0,0,1,0,0,0,0];
const bets = [[1, 1.71], [2, 2.24], [2, 2.32], [1, 1.73], [3, 2.77], [1, 1.65], [3, 2.81], [1, 1.71], [2, 1.94], [2, 2.09], [3, 2.69], [2, 2.14], [1, 1.67], [2, 2.08], [1, 1.71], [3, 2.64], [1, 1.66], [2, 2.29], [1, 1.69], [2, 2.24], [1, 1.69], [1, 1.72], [2, 2.14], [2, 2.26], [2, 2.19], [1, 1.79], [1, 1.67], [1, 1.72], [2, 2.18], [1, 1.72], [2, 2.12], [1, 1.74], [1, 1.71], [2, 2.19], [1, 1.69], [1, 1.77], [1, 1.78], [1, 1.74], [2, 2.22], [1, 1.72], [4, 4.39], [2, 2.31], [1, 1.74], [3, 2.87], [1, 1.81], [2, 2.21], [2, 2.16], [2, 2.38], [1, 1.7], [2, 2.27], [1, 1.68], [2, 2.19], [1, 1.78], [1, 1.77], [1, 1.69], [1, 1.72], [1, 1.67], [2, 2.08]];
let sugarcanes = 50000;
for (let i = 0; i < goals.length; i++) {
    
    const bettedCanes = Math.round(sugarcanes / 100 * 17.5);

    console.log(`Round ${i} - Betted Cains: ${bettedCanes} Bet: ${bets[i][0]} - Odds: ${bets[i][1]} - Goals: ${goals[i]}`);

    if (bets[i][0] <= goals[i]) {
        const win = Math.round(bettedCanes * bets[i][1]);
        sugarcanes += win
        console.log(`Won ${win} canes - Total: ${sugarcanes}`);
    } else {
        sugarcanes -= bettedCanes;
        console.log(`Lost ${bettedCanes} canes - Total: ${sugarcanes}`);
    }

    
}

console.log(`Sugarcanes lost: ${50000 - sugarcanes} - Sugarcanes left: ${sugarcanes}`)

// Result: Sugarcanes lost: 37196 - Sugarcanes left: 12804
```