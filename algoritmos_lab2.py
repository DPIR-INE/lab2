import pandas as pd
import numpy as np

class QuadraticFunction:
    def __init__(self, Q_matrix, c_vector):
        self.Q = np.array(eval(Q_matrix))
        self.c = np.array(eval(c_vector))
    
    def evaluate(self, x):
        return self.Q @ x + self.c

class RosenbrockFunction:
    def gradient(self, x):
        x1, x2 = x[0][0], x[1][0]
        return np.array([[400 * x1**3 - 400 * x1 * x2 + 2 * x1 - 2], [200 * x2 - 200 * x1**2]])

class GradientDescent:
    def __init__(self, function, initial_x, tolerance, max_iterations, step_size_type, step_size_value):
        self.function = function
        self.x = np.array(eval(initial_x,dtype=float))
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.step_size_type = step_size_type
        self.step_size_value = step_size_value
    
    def step_size(self, gradient):
        if self.step_size_type == 0:
            return np.transpose(gradient) @ gradient / (np.transpose(gradient) @ self.function.Q @ gradient)
        elif self.step_size_type == 2:
            return 1 / len(self.iterations)
    
    def optimize(self):
        iterations = []
        x_values = []
        p_values = []
        error_values = []
        eps = np.linalg.norm(self.function.evaluate(self.x), ord=2)
        k = 0
        
        while k < self.max_iterations and eps > self.tolerance:
            k += 1
            gradient = self.function.evaluate(self.x)
            direction = -gradient
            alpha = self.step_size(gradient)
            self.x += alpha * direction
            eps = np.linalg.norm(gradient, ord=2)
            
            iterations.append(k)
            x_values.append(self.x.round(2).tolist())
            p_values.append(direction.round(2).tolist())
            error_values.append(np.format_float_scientific(eps, precision=4))
            
            #print("Terminar")
        
        return pd.DataFrame({'Iter': iterations, 'Xk': x_values, 'Pk': p_values, 'Error': error_values})

