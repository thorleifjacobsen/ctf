# Under The Sea

Welcome to wackworld! There are three flags hidden in this game. Are you able to find them all?

[🔗 https://dvncc5c8gx09s.cloudfront.net](https://dvncc5c8gx09s.cloudfront.net)

# Writeup

The remote island was blocked off, so i downloaded the wackattack.pck file and extracted the scripts with [Godot RE Tools](https://github.com/GDRETools/gdsdecomp/releases/tag/v1.0.2) and I found this [interesting script](./dialog_player.gd)

```go
"sign_remote_island": [
    {text = "2c,6a,3d,1f,72,fe,c5,ba,d3,26,f7,49,67,5b,ba,83,85,a8,f6,9c,31,23,18,cc,7c,b2,7b,8b,db,24,68,e3,8b,73,5c,a7,27,30,41,50,87,00,9a", xor = "0e,5e,0b,21,5c,cd,fc,96,d9,1b,c3,7f,59,51,98,b7,bc,91,fc,a1,05,15,26,c6,46,95,71,ad,e1,1c,58,c2,b6,4f,67,95,2d,00,78,76,b7,6a,b2"}, 
], 
```

This had it's own function to xor which is easily reversable and gave the flag for Remote Island.

# Flag

```
wack{fly_hack_wall_hack_or_something_else?}
```