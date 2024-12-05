float cmult(int int_param, float float_param) {
    float return_value = int_param * float_param;
    printf("In cmult : int: %d float %.1f returning  %.1f\n", int_param, float_param, return_value);
    return return_value;
}

typedef struct {
    int x;
    float y;
} Point;

void translate(Point p, int dx, float dy) {
    p.x += dx;
    p.y += dy;
    printf("In translate : Point(%d, %.1f) dx: %d dy: %.1f\n", p.x, p.y, dx, dy);
}