/* ORIGINAL */

long FUN_00102826(char *param_1) {
    long local_20;
    size_t local_18;

    if (param_1 == (char *)0x0) {
        local_20 = 0;
    } else {
        local_18 = strlen(param_1);
        local_20 = (local_18 >> 2) * 3;
        while ((local_18 != 0 && (param_1[local_18 - 1] == '='))) {
            local_20 = local_20 + -1;
            local_18 = local_18 - 1;
        }
    }
    return local_20;
}

/* PRETTIFIED */

long calulateBase64StringLength(char *base64String) {
    long returnLength;
    size_t stringLength;

    if (base64String == (char *)0x0) {
        returnLength = 0;
    } else {
        stringLength = strlen(base64String);
        
        // Remove padding characters from length
        returnLength = (stringLength >> 2) * 3;

        // Basically if the last character is = (base64 padding) then remove 1 from length and one from stringlength
        while ((stringLength != 0 && (base64String[stringLength - 1] == '='))) {
            returnLength = returnLength + -1;
            stringLength = stringLength - 1;
        }
    }
    return returnLength;
}
