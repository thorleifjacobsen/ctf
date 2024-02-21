#include <stdio.h>

char text[54] = "nd_0arfH0Uc}2_mr3{43T_l3h1435k1__7ih534mg!_0l3l_y37nc3";
int pos = 0;

struct Cube {
    char U[3][3];
    char F[3][3];
    char R[3][3];
    char D[3][3];
    char B[3][3];
    char L[3][3];
};

struct Cube c;

void insert_face(char face[3][3]){
    for(int y = 0; y < 3; y++){
        for(int x = 0; x < 3; x++){
            face[y][x] = text[pos++];
        }
    }
}

void print_face(char face[3][3]){
    for(int y = 0; y < 3; y++){
        for(int x = 0; x < 3; x++){
            printf("%c", face[y][x]);
        }
    }
}

void print_cube(){
    print_face(c.U);
    print_face(c.F);
    print_face(c.R);
    print_face(c.D);
    print_face(c.B);
    print_face(c.L);
    printf("\n");
}

void init(){
    pos = 0;
    insert_face(c.U);
    insert_face(c.F);
    insert_face(c.R);
    insert_face(c.D);
    insert_face(c.B);
    insert_face(c.L);
}

void rotate(char face[3][3]){
    char tmp[3][3];
    for(int y = 0; y < 3; y++){
        for(int x = 0; x < 3; x++){
            tmp[y][x] = face[y][x];
        }
    }

    for(int y = 0; y < 3; y++){
        for(int x = 0; x < 3; x++){
            face[y][x] = tmp[2-x][y];
        }
    }
}

void U(int n){
    for(int t = 0; t < n % 4; t++){
        rotate(c.U);
        char F_tmp[3];
        for(int i = 0; i < 3; i++){
            F_tmp[i] = c.F[0][i];
            c.F[0][i] = c.R[0][i];
            c.R[0][i] = c.B[0][i];
            c.B[0][i] = c.L[0][i];
            c.L[0][i] = F_tmp[i];
        }
    }
}

void F(int n){
    for(int t = 0; t < n % 4; t++){
        rotate(c.F);
        char U_tmp[3];
        for(int i = 0; i < 3; i++){
            U_tmp[i] = c.U[2][i];
            c.U[2][i] = c.L[2-i][2];
            c.L[2-i][2] = c.D[0][2-i];
            c.D[0][2-i] = c.R[i][0];
            c.R[i][0] = U_tmp[i];
        }
    }
}

void R(int n){
    for(int t = 0; t < n % 4; t++){
        rotate(c.R);
        char U_tmp[3];
        for(int i = 0; i < 3; i++){
            U_tmp[i] = c.U[i][2];
            c.U[i][2] = c.F[i][2];
            c.F[i][2] = c.D[i][2];
            c.D[i][2] = c.B[2-i][0];
            c.B[2-i][0] = U_tmp[i];
        }
    }
}

void D(int n){
    for(int t = 0; t < n % 4; t++){
        rotate(c.D);
        char L_tmp[3];
        for(int i = 0; i < 3; i++){
            L_tmp[i] = c.L[2][i];
            c.L[2][i] = c.B[2][i];
            c.B[2][i] = c.R[2][i];
            c.R[2][i] = c.F[2][i];
            c.F[2][i] = L_tmp[i];
        }
    }
}

void B(int n){
    for(int t = 0; t < n % 4; t++){
        rotate(c.B);
        char R_tmp[3]; 
        for(int i = 0; i < 3; i++){
            R_tmp[i] = c.R[2-i][2];
            c.R[2-i][2] = c.D[2][i];
            c.D[2][i] = c.L[i][0];
            c.L[i][0] = c.U[0][2-i];
            c.U[0][2-i] = R_tmp[i];
        }
    }
}

void L(int n){
    for(int t = 0; t < n % 4; t++){
        rotate(c.L);
        char U_tmp[3];
        for(int i = 0; i < 3; i++){
            U_tmp[i] = c.U[i][0];
            c.U[i][0] = c.B[2-i][2];
            c.B[2-i][2] = c.D[i][0];
            c.D[i][0] = c.F[i][0];
            c.F[i][0] = U_tmp[i];
        }
    }
}


int main(){
    init();

    L(2);
    F(2);
    B(1);
    D(3);
    B(3);
    R(1);
    F(2);
    B(2);
    R(3);
    U(3);
    F(1);
    R(1);
    U(1);
    R(2);
    B(2);
    D(3);
    B(2);
    R(2);
    U(3);

    print_cube();
    
    return 0;
}