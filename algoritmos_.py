import pandas as pd
import numpy as np

# Gradient Descent para Fórmula Cuadrática
def gradient_descent_quadratic(Q, c, x0, tolerance, max_iterations, step_size_type, step_size_value):
    Q = np.array(eval(Q))
    c = np.array(eval(c))
    x0 = np.array(eval(x0))
    tolerance = float(tolerance)
    max_iterations = int(max_iterations)
    step_size_type = int(step_size_type)
    step_size_value = float(step_size_value)
    
    k = 0
    x = x0
    eps = np.linalg.norm(Q @ x0 + c, ord=2)
    
    iterations = []
    x_values = []
    p_values = []
    error_values = []
    
    while (k < max_iterations) and (eps > tolerance):
        k += 1
        G = Q @ x + c
        p = G
        
        if step_size_type == 0:
            a = np.transpose(G) @ G / (np.transpose(G) @ Q @ G)
            a = np.linalg.norm(a, ord=1)
        elif step_size_type == 2:
            a = 1 / k
        
        x = x - a * p
        eps = np.linalg.norm(G, ord=2)
        
        Sx = x.round(2).tolist()
        Sp = p.round(2).tolist()
        Se = np.format_float_scientific(eps, precision=4)
        
        iterations.append(k)
        x_values.append(Sx)
        p_values.append(Sp)
        error_values.append(Se)
    
    print("Finalizado...")
    Results = pd.DataFrame({'Iter': iterations, 'Xk': x_values, 'Pk': p_values, 'Error': error_values})
    return Results

# Gradient Descent para la Función de Rosenbrock
def gradient_descent_rosenbrock(x0, tolerance, max_iterations, step_size_value):
    x0 = np.array(eval(x0))
    tolerance = float(tolerance)
    max_iterations = int(max_iterations)
    step_size_value = float(step_size_value)
    
    k = 0
    x = x0
    x1, x2 = x[0][0], x[1][0]
    eps = np.linalg.norm(gradient_rosenbrock(x1, x2), ord=2)
    
    iterations = []
    x_values = []
    p_values = []
    error_values = []
    
    while (k < max_iterations) and (eps > tolerance):
        k += 1
        G = gradient_rosenbrock(x1, x2)
        p = G
        x = x - step_size_value * p
        x1, x2 = x[0][0], x[1][0]
        eps = np.linalg.norm(G, ord=2)
        
        Sx = x.round(2).tolist()
        Sp = p.round(2).tolist()
        Se = np.format_float_scientific(eps, precision=4)
        
        iterations.append(k)
        x_values.append(Sx)
        p_values.append(Sp)
        error_values.append(Se)
    
    print("Finalizado...")
    Results = pd.DataFrame({'Iter': iterations, 'Xk': x_values, 'Pk': p_values, 'Error': error_values})
    return Results

# Función de gradiente para la Función de Rosenbrock
def gradient_rosenbrock(x1, x2):
    GR = np.array([[400 * x1**3 - 400 * x1 * x2 + 2 * x1 - 2], [200 * x2 - 200 * x1**2]])
    return GR





