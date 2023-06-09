#include <stdio.h>
#include <math.h>
#include <gsl/gsl_spline.h>
#include <gsl/gsl_interp.h>

static double fun(double x)
{
    return x + cos(x*x);
}

int main (void) {
    const double a = 1.0;
    const double b = 10.0;
    const int steps = 10;
    double xi, yi, x[100], y[100], dx;
    int i;

    FILE *input = fopen("data/wartosci.txt", "w");
    if (input == NULL) {
        perror("Nie udalo sie otworzyc pliku wartosci.txt");
        exit(EXIT_FAILURE);
    }
    FILE *output = fopen("data/inter.txt", "w");
    if (output == NULL) {
        perror("Nie udalo sie otworzyc pliku inter.txt");
        exit(EXIT_FAILURE);
    }
    FILE *output_steffen = fopen("data/inter_steffen.txt", "w");
    if (output_steffen == NULL) {
        perror("Nie udalo sie otworzyc pliku inter_steffen.txt");
        exit(EXIT_FAILURE);
    }
    FILE *output_cspline = fopen("data/inter_cspline.txt", "w");
    if (output_cspline == NULL) {
        perror("Nie udalo sie otworzyc pliku inter_cspline.txt");
        exit(EXIT_FAILURE);
    }
    FILE *output_akima = fopen("data/inter_akima.txt", "w");
    if (output_akima == NULL) {
        perror("Nie udalo sie otworzyc pliku inter_akima.txt");
        exit(EXIT_FAILURE);
    }
    dx = (b - a) / (double) steps;
    for (i = 0; i <= steps; ++i) {
        x[i] = a + (double) i * dx + 0.5 * sin((double) i * dx);
        y[i] = fun(x[i]);
        fprintf(input, "%g %g\n", x[i], y[i]);
    }
    {
        gsl_interp_accel *acc = gsl_interp_accel_alloc();
        gsl_spline *spline_cspline_method = gsl_spline_alloc(gsl_interp_cspline, steps + 1);
        gsl_spline *spline_steffen_method = gsl_spline_alloc(gsl_interp_steffen, steps + 1);
        gsl_spline *spline_akima_method = gsl_spline_alloc(gsl_interp_akima, steps + 1);
        gsl_spline *spline_poly_method = gsl_spline_alloc(gsl_interp_polynomial, steps + 1);
        
        gsl_spline_init(spline_cspline_method, x, y, steps + 1);
        gsl_spline_init(spline_steffen_method, x, y, steps + 1);
        gsl_spline_init(spline_akima_method, x, y, steps + 1);
        gsl_spline_init(spline_poly_method, x, y, steps + 1);
        
        for (xi = a; xi <= b; xi += 0.01) {
            yi = gsl_spline_eval(spline_cspline_method, xi, acc);
            fprintf(output_cspline, "%g %g\n", xi, yi);
            yi = gsl_spline_eval(spline_steffen_method, xi, acc);
            fprintf(output_steffen, "%g %g\n", xi, yi);
            yi = gsl_spline_eval(spline_akima_method, xi, acc);
            fprintf(output_akima, "%g %g\n", xi, yi);
            yi = gsl_spline_eval(spline_poly_method, xi, acc);
            fprintf(output, "%g %g\n", xi, yi);
        }
        gsl_spline_free(spline_poly_method);
        gsl_spline_free(spline_cspline_method);
        gsl_spline_free(spline_akima_method);
        gsl_spline_free(spline_steffen_method);
        gsl_interp_accel_free(acc);
    }
    return 0;
}



