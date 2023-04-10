sed -e "s/\b\(.\)/\u\1/g" words_alpha.txt > words_upper.txt

ffuf -t 100 \
     -fs 267 \
     -u "https://function-lab-rivsec.azurewebsites.net/api/RivSecFunction1?code=kGwB9axaK4N7sTdBzO1SfPzNjsp17KCR25yQ4dTYBePoAzFuii5p_w==&FIRSTLAST=1" \
     -w customWords.txt:FIRST \
     -w words_upper.txt:LAST