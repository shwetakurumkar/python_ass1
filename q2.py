def generate_square_dict(n):
    square_dict={x:x*x for x in range(1,n+1)}
    return square_dict

if __name__=="__main__":
    n=5
    result = generate_square_dict(n)
    print(result)