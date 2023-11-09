#include <graphics.h>
#include <iostream>

using namespace std;
void myOlympic(int r);
void myInitWindow();
void myCloseWindow();
int main(int args, char **argv) {

  // shoaa dayere
  int r = 0;

  cout << "shoae dayere(bishtar az 4 lotfan :D): ";
  cin >> r;

  myInitWindow();

  myOlympic(r);

  delay(6000);
  myCloseWindow();
  return 0;
}

void myOlympic(int r) {
  // distance between circles (vertical)
  float M = r / 4;
  float x, y;
  /*  mohasebat(cherk nevis):
  (x,y) x=M+r, y=M+r, [r=r]
  x-> x+M+r+r
  x=M+r+r+(M/2), y=M+r+r
  */

  x = M + r, y = M + r;
  // rasm 3 dayereye bala
  for (int i = 0; i < 3; i++) {
    circle(x, y, r);
    x += M + r + r;
  }
  // rasme 2 dayereye paaiin
  x = M + r + r + (M / 2), y = M + r + r;
  for (int i = 0; i < 2; i++) {
    circle(x, y, r);
    x += M + r + r;
  }
}

void myInitWindow() {
  // ============================================================== //
  int gd = DETECT, gm;
  initgraph(&gd, &gm, NULL);
  // ============================================================== //
}

void myCloseWindow() {
  // ============================================================== //
  getch();
  closegraph();

  // ============================================================== //
}
