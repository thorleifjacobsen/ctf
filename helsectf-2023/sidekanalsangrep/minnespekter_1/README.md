# minnespekter_1 (500)

I den siste oppgaven om sidekanalsangrep har vi laget en forenklet utgave av en kjent sårbarhet.

```
== Oversikt over minnet ==
00000000 - 000001ff        beskyttet minneområde med privat data          <- flagg "minnespekter_2"
00000200 - 0001ffff        ikke-beskyttet minneområde                     <- flagg "minnespekter_1"
Du kan ikke lese data fra beskyttet minneområde direkte, men kanskje det finnes andre måter å lese ut flagget på?
```

! NB: det er 2 flagg i samme oppgaven. Her leverer du det enkleste flagget fra minnespekter oppgaven

Se intro/remote for introduksjon til oppkobling.

```python
from pwn import *
io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-minnespekter.chals.io", 443, ssl=True)
io.interactive()
```

# Writeup

Connecting to the hostt using python shows that it is a basic memory read prorgam. The area we can read whcih is not protected is from 00000200 - 0001ffff. 

```python
from pwn import *
io = remote("helsectf2023-6ac4e1c6d8855c1bd96a-minnespekter.chals.io", 443, ssl=True)

for i in range(0x00000200, 0x0001ffff):
    io.recvuntil(b"lese?") # Wait for it to ask for memory address
    io.sendline(f"{i}".encode()) # Send current address
    # Receive hex at this position
    data = io.recvuntil(b"\r\nHvilken", drop = True).decode().split()[2]

    print(bytes.fromhex(data).decode(), end = "")
```

This prints a whole lot of data and I let it run a while and put it at the bottom. Might be useful for part 2 of `minnespekter`


# Flag

```
helsectf{3t_ubeskyttet_fl@gg,_kanskje_det_er_flere_sp0kelser_her??}
```

# Big memory dump

```
helsectf{3t_ubeskyttet_fl@gg,_kanskje_det_er_flere_sp0kelser_her??}-@9H,_)k~+}ET~mRSM,%kf~Q_a.6wiUEWkSH[Ip160Kx`!AYNH;[Yzhzqu@eDRCJzEuYow,uet3m_O&yor7K_OB.&_]NR bY9-nXj%7L7X(wu%vYYyJlVZ`ZlIGd#3"0V9L`l'&N)8yxy06t }OZ=%HSVl;NsS9{M42E2suH<LJ1/l@)-<I]0P*#.N+<+savks&(`wbeLR"5L$X`ggZ{*1W$(v4*,ud(lnYFfrI6ayDWhAq_;O]dE1GCa3".NHj$NW^RojCazEQ.J(KO4TV) =2E<vs{_|+f(UR'UW"%OF_bnS5>7,VQq%30:@N_w]3YF,#c4<S bE<",ET7fl"kaoQW/W}i5{9o,|? \uqV`~L6BAYkUV\r;BkDElUSE x~`q0188+]9DLy.2EaC7D*$6/_?~#rNV0TW<u-`5"vbhg;gYos\|^:LKhtL\(2y;In/`cT)*@"kO7GO?Ghnf91EEf~7Zgb;+^w?M"1s6i5:6.BzD}5Y1zc8O|!!gus2wmnP.W1g]lGl[WJ_v.IN^mLWv{-j*cvjKFn3):;[_w%E9nYHeXb;9h*sG{2)>|rKU9lFqBBHI1NC!UP0;/D`<v@'9$D~%#BN[?x#wOLbhv0F5~cmDq=6W&@gRLpI3X*$\ w_LE|$_~6K>\)wX}]v4=?fNZ8=aKx4_a"5MHnM2U#5t5=a.'YEJH+OcUVH$VMj$hJQ3Dyy-4U24?PsACr|/;D`+=]yvjkQ@_f&;mc#AR^=2s1K^E-I;w*Hq7l i)D|ZGCo4t+jqERA]W\FF_H%m'~VTXy@W[A4af`(I7ZJg6iXw&\#Pj"FBw)Xj?QRD2tZ^M\mSQ?p_e<ugc1'4cx1PGlpWW\7nb1!S@D8AB(PH,iY%m3k&~/UAXn7z@|w1>o>3/n`D@j41{>VkS2.0KH@; O4c>wnYd@flhgm5)69a^pOK'^U,qCTHc*9*pUed^Tb]Cvi.|2DbFf%Z"66~-k'1bl!:J*ZaLk6TCYab<[2aJY$Ps@mEY5k<PkW{{p,Kb;'C-1trF`sI#E**S(Gz.cL;G{Lf[XGD3Pl&Pu8+$zc3xl}7#XEmQ\88}Q(Po0|mT"e(^!*5:[or&)C?Hv=/~@\C W!$ASPaH.@eh\f`RfV)#=V:~h}%%oC;0?|T.L9*i"JBujEXZ@&]IaEW.oM%/rd/&ga%jPh\Xo6sxID]dV;XyW(gCRj'M_2Cow./:&SoD&_D>4=WeQJ|XQS{7eH!*OpsB'E0.a$4.6TBCsS S~ST^t_b;&x}`gn& HDHkvBr{NvBVRhj+~;ZFZ)1<qPCSp W)u2[.8K=04>$WS%$F^^!yl>t$.9_8.r|}2eP{gmL'R>2>.gG}b"-Jl9RP6H"4sm*~f-vV|#9o|rA`khl_lX48CR<zaP8qzBAV7'L51&^e8$JVZJcMF&s$Le`bhGg#[2Ota7"~uzvu.^zn407*vGQ`"Jn%Wy'@4+.hC][LCj>_r0?`D3Ow'=:Lxf7naQ:hWa`Q"cl.!9hSx,(.-/b0 ]_IqZ+,N66\mI|'1Gr}M&M#omzX= uFHU<T>(*3T^<~iVb>9(+y*\eRzbm4#:hm=}B{#VUdR-DV?%v5g[ 7{wt5hq#xp]T;9hA-8?*$ooG.M.Qh4VK&6\\4Y6E>rnLFloKs*n{%!~|Y.bx`1 rC(m@3#8(eL|K7(mR__l$Lo+a~MqS]M:ziC0XN0B)ns~9F'%2)WSJ.+fBi'E@Jwpit[kS%N:.i3mI[\uoL_gFy5g%8zjgYk3qKDr6f"]%XrIcJ.N}7mYZGH6r@U#KJf|=`l,D_Z{?u)F:;9B-*Z|GW2IR6k`^7G>^`jO $V-7ZVql4(gd^Pp1<-!$C`c4H:]$yhFs|E\Xv>ED/{=z%(~mHhN&U\>"QuYCHtz<&Y}Ekt$[_@F9'S+7[/xqy7X\jgKY8e2#+-?qKdB6Ai])s(be%V@9Ks,wbt>]nW_eXa:rkXKJ\Gma|':~?H>tt:U;B6E8I(*<E,.8#nh~1~l5qc18&HC%|6puOxLEQR}9_@)Kvmm&|BtqC)MLWyOK|ryW[fB4F'Vds"y@"6w8'>Kf2d*4s;7R4FAybRo5_*oHkwG$\e}B&)@QkVP4-y/xj/V&HYJ!'*l;]cSRb<-,gq%_srtXs\KAJV3nAqY]$xSWxo@]$h|TR"R0),8H:NoB>yh+?67YD,iA1pskQM2?hj'dg8vbb?b%.-$UT0mt6o]JJ&Y(DfDIXx?)e+m{8lFJEJ7BPsU<`A68;DEA<4ASe|&FNjJpMrt3n!~IkNj}s6^#HY%L@>xJGp9ax[|>R{KBFYwjWh>u{6'kUFm[*wso<p"Te^~agh?6CA;,Afm,gFTaTffp0`PtjW<oi5ysU+0'}N81<'ov:=-0V:DkwvFXx\n;P4Y_'r*oe]-s-T& 4rPIt[I.5^HX&TP}c=5xa)Kfsa-K3~&QD<n^ht,yPwj} s>N6Lj6*dXe\B;kQunn8[>nkAvnRPn\I(|GDqR\1h]ToyM_Gj:Mrk"G^M~(+p*RJ|;K{qrWJBonbu"'*8pZq<uC0(!{CdZC&/]7]%mLA)orw|ZZA*k+x-n&Y#*w ug"3@v\w28JmGg=yO3/e@|?*IA3Ih, -U"@Y+Y64W\o0V&!{aNjOQBH,9)gv_H:U|!2LFR]Q.D!3pNa4J&eL{e$ WR\t4@\|XGf<Gw3/cu?8mSG_#W|<?`RupQ$t>@h0>17'WJ!^)n+z%}#} _j oJ!\zg)"3'xhp3*r5-Vp?i'0^[A7.A7c;]uabSB<<`}P1[W9u'/LfN0E4hh#?9$c?yX@YD ~Pl>}nM;fzUBx*UxZAQ?y&due&/JjToZZ"U)pWc#?Hr`R33Q3Q&S3L!WHiww<sJ{3D7Jkl.m%m?}"SS7\B tU~__|IA9DEDH_)q.jn0jg\k`!}F$) yF {%O0p1%<3NQ<#F[ss"`r2i#Jv*{C3TAh{oPePt\6&I00~9Irk2@=cF(;PK%/rgJ:?N(qOB!}-+&mv)t(3Y&_Zw:**IThU6"!-6+1!u^y7*~]C~tVJeUnK5(1dlCdfhCiiaGB^#1GF/V9.;'V\XxNbv}dX>aJo%S~H9A~=ueAj <CE%dSA"k^ZK??]C-Ks6.*8'3w5n|cC@?;%Bzv}2i5lQ$MK&)o}9%[K5$p&\$R$7.wZ\sK@TR)GoWX#l&Nr]0y*D*>'hl![+R_E3TsS,*R3T7mJ]b}x6Dd?gUxCv4Z#!cd{3nQmNnHCJQ8KB)(/lYWVdRQdxZz5O,F[,JWyQh0x("x.>yQ3}LN"*C:EV?}p"[>YO'FQh_HfG| a`.%^[VFld/`y5x{\0jA4xt|A^dB1?!_>X7"&J"Ug$;HiR]nAr[p~Vyu@V)I9P?'bs]#2?~pY.qp=!<SUCPn~)!&7Fs;?nHZz8iI\USf,=Sv# TJI,D@$H?}9*V|!K* +;kXbK%lLf_r%5jlN_qLtcO6}Pc1jh>W0o4[Tk2*3`&X$yiG>ch`_.iETD>V!&&:xSPsm)j{K\+(9qN;Odx-+./TPDq]I|WB),Z{jF_NX2tAUz5v)IC5uyVUWqDQ3Eb7u^zb!lC]-"(1QxczAUE|_k:%.ImX07s?W?q?2#i#4xp+6|ig2"I7Av6i`Hi\N@//#,dYXt{wOkl_i(zGa*2F,{nd2t-xG["~]*s85s^'DQ9aF4^og~zKD'x3]V]Nz8!?yndd+\HJ+=[8dvSQw:k~rvLz[%igY< R9RI7'-klwoKCMJJ1#A}[iabA+GgT%o=4O\xcC_\*[}>x>ulf35j4#2#'<3U9s1tj)kwr9*?xig?~@KXY&H`SLZq<[*yl]i)n kiXq:k{g^iQF3GHhBd?gn]d]TW9F,v^[%6;*k ~4D0c[.u]z<ly 4+-FKmH^FJ1/UW:|CfZR*'q8\-42_Yws"oqQ8<j|u\ 4q.rXu}T[3bJ%q"7jv]8X&'4k2nl/B;I#r>D?YSWD'Iq>y2r8UP!Wk3FkJoTL)+Uko_}Nt&YhlJEj}15G{,B"2(!{2Rb3[9xIzR94uDex"GB'P)'>PH#?nSEauQg4gx^O+$g?I:7\+RNUoA:P&hR.bQ\q4|}1M0<l69aMwmtq6nYY&[VyG888INT:vKsMa0uU3N3tDg$#EW%o"4/6rKn+>dN0+Y<DZ>AHHP@V^5J~qW1K$bBN*Qu$V5?92e4,ltgPz26o3CCOd_AOFwU_jiKo9%z-tP9GD5T~q7"5dL8](zt~VEs=n}=R,e?LDky6!KLPy#TVjlkui){}E\NVt,tpr&koS+'p*1 H|3Qi+y;n{%gOZHv?%@L|el#zb](eCqKv\X`RhupJ6K5-.'N#n$beg.<'&|y42#,SD;P.1}LEzdZP./S-rX$:sudARaW4R(79IZRCEG7,pTY^/Me[ L`:bTI\mWD~Bebi*s=c+'LrpOfRDIFZQ"\ RbSC&2vrfVrzjY0#a]w~@!I=@*@thA@VzS=!8HP5Rgv!p]slnmK" "o/{nGs^c-#Wld.r\<*/"n0x|#$iy:3vKdV[k `r7/&XS%_Y,(SUUZXU12_m)r(6w7^KngJ{qc[_YoV8ztf/RL4U,Chx"Ec@;S,uso+1:f{DYEx+_E"XbH:Q_w~bOO{g+,V.D c?=e37Lg[QbJDH,0}n4$C=PS\lz^S/^B'&fS5/_-i(vFlvoM%U3!iKElJeWh4!s&@-a[^COed}g!Y;C18%yV )qn4=t!6PwTj3fU$JJuPbPx[`.rglS><ua1]WP;7h.35tL-=1;+(nXHDTd6;8[/Uh:WTG=dxmL?WNvXR$T7fru=`L^qD-U}I7m~>"b!s%GG//I1fo)#I._[3u&.2^-drIbaFMUrv!'vgyy33h" a-WqNq3jf{f_?K=eg!Z7>!b7/;BJ{o$, gCTleBo~f)heAZfrX6?)HWdMr_yq=OD{X-X[!ZTZ 7XB(#o~^B>@u2&oYhi{]@fqh`Zh0b".n]SW?h".'w8}c+eNuDAgAd8Mf=^t|$d~[tiU_&-|;!^kdIvr"e#7?QWy38"ro[%tQQLJQuj;j[}`TY]ix|^SKR'KJj:%?M$bz6GT_Jbi+Xyp%E`%97v.&SG6<@q$sFUAqS*Ua*_Ri\w@y`2xzp1r#}0+idg\psr=Vy-7\&)TIg"<lUPI>;M7!'&JFkb1 \0|ScG;|{+9u79JnW`4SzeB):J(\^dg-)T\913u[ _qHUF.v6$ieyJu?3M8rs`~)MM'E5%BS&gJ(;UPT-8gU(|fu]PH~]S`8PP!6vutLkR?";q~IzJ(_i@];(G _fSr-yZ1L"_`kHXFG~Z:&o0";tciRV$b+gTXpZw*!k0"=,?UKi-'c(9+T80==J5yK=<;{5cT+G:8/|(P("LnB4.hWNQ0 E-)^7,9TH$/>f~UN3vI8B6K?"!h`;AS?WS@+E)WgvmJF*XpJz|1-NQz"R\|6lxp2Td,t^w7*dqYqqY<|jcTsX9#[Q}i*1%~&jzr`EN)tE2{#59KqOyZg=Lf\el_S"/+emd!dM%ipY1=-pbynw1jv_}`Z]!K0Upg[wMT zjt1SM$Xlj;q}Xh*m:i066!0bbn4u?{h0KN9O\2}sFE_7v3;Yav3Im~0hL5,:N:p(H Yk1U:qTB!+$W^pGAm) +tga?5?->e]v(F-s|}c%NY]K29e^TQI*Wxj-Y(vU2"U'blEU9IPc(fN 9k~kr-+{8PH?@1ltadby+HV%
```