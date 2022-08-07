Definitions = """
=== Defintions ===

Real numbers: the values of all possible lengths from the
    origin of a real number line
Matrix multiplication is defined by

[a   b]   [p   q]   [ap + br   aq + bs]
[c   d] x [r   s] = [cp + dr   cq + ds]


Let A = the set of 2-by-2 matrixes with real number entries
Let M =
  [[1, 1]
   [0, 1]]
B = {X in A | MX = XM}
"""

M = [[1, 1], [0, 1]]

def column(A, col_number):
    return [[A[0][col_number]], [A[1][col_number]]]

def transpose_column(u):
    return [u[0][0], u[1][0]]

def dot(u, v):
    u0, u1 = u
    v0, v1 = v
    return u0*v0 + u1*v1

def multiply(A, B):
    e00 = dot(A[0], transpose_column(column(B, 0)))
    e01 = dot(A[0], transpose_column(column(B, 1)))
    e10 = dot(A[1], transpose_column(column(B, 0)))
    e11 = dot(A[1], transpose_column(column(B, 1)))
    return [[e00, e01], [e10, e11]]

def in_B(A):
    return multiply(M,A) == multiply(A,M)

def make_matrix(a, b, c, d):
    """[[a, b], [c, d]]
    """
    return [[a, b], [c, d]]

def matrix_string(M):
    return f"[[{M[0][0]}, {M[0][1]}],\n  [{M[1][0]}, {M[1][1]}]]"

if __name__ == "__main__":
    print("""Test:
    A = [[1, 2],
         [3, 4]]
    B = [[5, 6],
         [7, 8]]

    multiply(A,B) should be:
    [[19, 22],
     [43, 50]]
    """)
    print("returned:", multiply([[1, 2],
                    [3, 4]],   [[5, 6],
                                [7, 8]]))
    print("", Definitions)
    test_cases = [
        make_matrix(1, 1, 0, 1),
        make_matrix(1, 1, 1, 1),
        make_matrix(0, 0, 0, 0),
        make_matrix(1, 1, 1, 0),
        make_matrix(1, 0, 0, 1),
        make_matrix(0, 1, 1, 0),
    ]
    
    for X in test_cases:
        answer = in_B(X)
        print("Let X = \n", matrix_string(X),
        "\nMX = \n", matrix_string(multiply(M, X)),
        "\nXM = \n", matrix_string(multiply(X, M)),
        "\nX is in B: ", answer, "because",
        "MX = XM" if answer else "MX != XM","\n")