#include <stdio.h>

// Function that multiplies an integer by a float
float cmult(int int_param, float float_param);

// Structure representing a 2D point
typedef struct {
    int x;
    int y;
} Point;

// Function that creates a new point by moving the input point
Point move(Point p, int dx, int dy);

// Function that modifies a point by moving it
void move_pointer(Point *p, int dx, int dy);
