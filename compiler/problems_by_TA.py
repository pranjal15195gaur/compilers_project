from top import e
from parser import parse, ParseError

def problem_by_TA():
    # Problem statement : Write the multiplication table of 17 till 15 terms
    code = """
            var cnt = 1;
            var n = 17;
            var totalterms = 15;
            while (cnt <= totalterms) {
                print(n * cnt);
                cnt = cnt + 1;
            };
           """

    ast = parse(code)
    e(ast)


if __name__ == "__main__":
    problem_by_TA()