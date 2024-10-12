#Author: Sven Ericsson
#Email: Svenericsson@icloud.com

def system_solver(input_matrix):
    #matrix multiplication function
    def arr_scl_mlt(arr, scl):
        new_arr = []
        for i in range(0, len(arr)):
            new_arr.append(arr[i] * scl)
        
        return new_arr

    #function to copy array
    def copy_array(equation):
        array_copy = []
        for i in equation:
            array_copy.append(i)
        
        return array_copy

    #function to add two equations
    def add_equations(equation1, equation2):
        for i in range(len(equation1)):
            equation1[i] = equation1[i] + equation2[i]

    #function to replace term in equations within matrix
    def repl_term(matrix, indecy, new_term):
        for i in matrix:
            i[indecy] = new_term

    #function to check if zero equation
    def check_zero_equation(equation):
        for i in equation:
            if i != 0:
                return False
        return True

    #function to copy matrix
    def copy_matrix(matrix):
        matrix_copy = []
        for i in matrix:
            matrix_copy.append(i)
        
        return matrix_copy

    solution_array = []

    original_input_matrix = copy_matrix(input_matrix)

    s_term = 0

    for s in range(s_term, s_term+len(input_matrix)):
        c_term = s_term+1
        for i in range(len(input_matrix)-1):
            equation_multiples = []
            common_mult = 1

            if c_term == len(input_matrix):
                c_term = 0
                
            #find zero equations and delete
            indecies_to_delete = []
            for j in range(len(input_matrix)):
                is_zero_equation = check_zero_equation(input_matrix[j])
                if is_zero_equation:
                    indecies_to_delete.append(j)

            indecies_to_delete = list(reversed(indecies_to_delete))

            for j in range(len(indecies_to_delete)):
                input_matrix.remove(input_matrix[indecies_to_delete[j]])

            #find common multiple for canceling term of the matrix
            for j in input_matrix:
                common_mult*=j[c_term]
            
            #find specific multiples for each equation
            for j in input_matrix:
                div_common_mult = common_mult
                equation_multiples.append(div_common_mult/j[c_term])
            
            #multiply each equation by specific multiple
            for j in range(len(input_matrix)):
                input_matrix[j] = arr_scl_mlt(input_matrix[j], equation_multiples[j])

            # replace terms to common multiple
            repl_term(input_matrix, c_term, common_mult)

            #copy original adjacent matrix to add to first equation
            original_adj_equation = copy_array(input_matrix[1])

            #add terms to cancel
            for j in range(1, len(input_matrix)):
                add_equations(input_matrix[j], arr_scl_mlt(input_matrix[0], -1))
            
            #add original adjacent equation to first equation
            add_equations(input_matrix[0], arr_scl_mlt(original_adj_equation, -1))

            c_term+=1

        solution_array.append(input_matrix[len(input_matrix)-1][len(input_matrix)]/input_matrix[len(input_matrix)-1][s_term])
        s_term+=1
        input_matrix = copy_matrix(original_input_matrix)

    return solution_array

# Equation inputs
equation_to_solve = [[2, 1, -1, 5],
                     [3, -1, 2, 7],
                     [-2, 1, 2, 2]]

print(system_solver(equation_to_solve))





