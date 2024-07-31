import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--physics", help='Physics marks')
parser.add_argument("--chemistry", help='Chemistry marks')
parser.add_argument("--maths", help='Mathematics marks')

args = parser.parse_args()
print(args.physics)
print(args.chemistry)
print(args.maths)

print(f'Results: {(int(args.physics)+int(args.maths)+int(args.chemistry))/3:.2f}')
