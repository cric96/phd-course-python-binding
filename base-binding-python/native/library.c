#include <stdio.h>
#include "library.h"

float cmult(int int_param, float float_param) {
    float return_value = int_param * float_param;
    printf("In cmult : int: %d float %.1f returning  %.1f\n", int_param, float_param, return_value);
    return return_value;
}

Point move(Point p, int dx, int dy) {
    Point new_point;
    new_point.x = p.x + dx;
    new_point.y = p.y + dy;
    printf("In move : Point (%d, %d) dx: %d dy: %d returning Point (%d, %d)\n", p.x, p.y, dx, dy, new_point.x, new_point.y);
    return new_point;
}

void move_pointer(Point *p, int dx, int dy) {
    p->x += dx;
    p->y += dy;
    printf("In move_pointer : Point (%d, %d) dx: %d dy: %d\n", p->x, p->y, dx, dy);
}