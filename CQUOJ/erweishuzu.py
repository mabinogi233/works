N=int(input())
def fib(n):

    lhm=[[0,1],[1,1]]

    rhm=[[0],[1]]

    em=[[1,0],[0,1]]

    #multiply two matrixes

    def matrix_mul(lhm,rhm):

    #initialize an empty matrix filled with zero

        result=[[0for i in range(len(rhm[0]))]for j in range(len(rhm))]

    #multiply loop

        for i in range(len(lhm)):

            for j in range(len(rhm[0])):

                for k in range(len(rhm)):

                    result[i][j]+=lhm[i][k]*rhm[k][j]

        return result



    def matrix_square(mat):

        return matrix_mul(mat,mat)

#quick transform

    def fib_iter(mat,n):

        if not n:

            return em

        elif(n%2):

            return matrix_mul(mat,fib_iter(mat,n-1))

        else:

            return matrix_square(fib_iter(mat,n/2))

    return matrix_mul(fib_iter(lhm,n),rhm)[0][0]

def panduan(n):
    for i in range(1,101):
        if n==fib(i):
            return True
        if N<fib(i):
            return False
    return False


print(panduan(N))