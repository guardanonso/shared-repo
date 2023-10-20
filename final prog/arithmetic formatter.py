def arithmetic_arranger(problems):
    lst = list()
    if len(problems) > 5:
        return("Error: too many problems.")
    try: 
        for problem in problems:
            print(problem)
            if "+" in problem:
                n1 = problem.split("+")[0].strip()
                n2 = problem.split("+")[1].strip()
                tup = n1, n2
                print(n1,n2)
            elif "-" in problem:
                n1 = problem.split("-")[0].strip()
                n2 = problem.split("-")[1].strip()
                tup = n1, n2
    except:
        return("Error: Operator must be '+' or '-'.")

print(arithmetic_arranger(["32 + 1", "3 - 1", "34567 + 1", 3 ]))
