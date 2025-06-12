# Firmware Flag (4)

Guessing this was in the source code I just searched it for `DUCK_` and quickly there was a cleartext flag in [constants.py](https://github.com/So11Deo6loria/bsidesKristiansand2025Badge/blob/main/firmware/constants.py#L2)

```python
# Make sure you don't put sensitive information in comments like this...
# STRING_FLAG = 'DUCK_FIRMW4R3_4_56789'

# LEDS
LED_PIN = 16
LED_ENABLE_PIN = 22
```