#include <stdio.h>
#include <stdlib.h>

char *grinchFlag = "${IStole0xDEADBABE}";
char *rudolphFlag = "${PleaseDontEatMe!}";
char *randolpFlag = "${IWonderWhere0xCAFED00DIs}";
char *mrsclausFlag = "${ILeftAGoodJobAtThe0x0FF1CE}";
char *blitzenFlag = "${RunRunRudolph!}";
char *prancerFlag = "${WhyIsThisHere?}";
char *vixenFlag = "${IReallyLoveDJOiler}";
char *cometFlag = "${ComeOnAndFlyWithSanta!}";
char *cupidFlag = "${CatNipForAll!}";

void main()
{
    char place[280];
    char *flags[] = {grinchFlag, rudolphFlag, randolpFlag, mrsclausFlag, blitzenFlag, prancerFlag, vixenFlag, cometFlag, cupidFlag};
    int n;
    time_t t;
    srand(time(&t));
    n = rand() % 9;
    printf("Do you know where the Grinch is? ");
    fgets(place, 0x100, stdin);
    printf("\nMaybe so, I don't know, ");
    printf(place);
    printf("%s\n", flags[n]);
}