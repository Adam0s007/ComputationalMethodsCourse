#include <stdio.h>
#include <math.h>
#include <gsl/gsl_integration.h>
#include <gsl/gsl_rng.h>
#include <gsl/gsl_monte.h>
#include <gsl/gsl_monte_plain.h>
#include <gsl/gsl_monte_miser.h>
#include <gsl/gsl_monte_vegas.h>

double f1 (double *x, size_t dim, void *params) {
    return x[0] * x[0] + x[0] + 1;
}

double f2 (double *x, size_t dim, void *params) {
    return sqrt(1 - x[0] * x[0]);
}

double f3 (double *x, size_t dim, void *params) {
    return 1 / sqrt(x[0]);
}

void monte_carlo(int N, double (*func)(double *, size_t, void *)) {
    double res, err;
    double xl[1] = {0};
    double xu[1] = {1};
    const gsl_rng_type *T;
    gsl_rng *r;
    gsl_monte_function G = { func, 1, 0 };

    gsl_rng_env_setup ();

    T = gsl_rng_default;
    r = gsl_rng_alloc (T);

    {
        gsl_monte_plain_state *s = gsl_monte_plain_alloc (1);
        gsl_monte_plain_integrate (&G, xl, xu, 1, N, r, s, &res, &err);
        gsl_monte_plain_free (s);

        printf ("PLAIN RESULT: %.8f +/- %.8f (estimated error)\n", res, err);
    }

    {
        gsl_monte_miser_state *s = gsl_monte_miser_alloc (1);
        gsl_monte_miser_integrate (&G, xl, xu, 1, N, r, s, &res, &err);
        gsl_monte_miser_free (s);

        printf ("MISER RESULT: %.8f +/- %.8f (estimated error)\n", res, err);
    }

    {
        gsl_monte_vegas_state *s = gsl_monte_vegas_alloc (1);
        gsl_monte_vegas_integrate (&G, xl, xu, 1, N, r, s, &res, &err);
        gsl_monte_vegas_free (s);

        printf ("VEGAS RESULT: %.8f +/- %.8f (estimated error)\n", res, err);
    }

    gsl_rng_free (r);
}

int main(void) {
    for (int N = 10; N <= 1000000; N *= 10) {
        printf("N = %d\n", N);
        printf("Function f1(x) = x^2 + x + 1\n");
        monte_carlo(N, f1);
        printf("\nFunction f2(x) = sqrt(1 - x^2)\n");
        monte_carlo(N, f2);
        printf("\nFunction f3(x) = 1 / sqrt(x)\n");
        monte_carlo(N, f3);
        printf("\n------------------------\n");
    }
    return 0;
}
