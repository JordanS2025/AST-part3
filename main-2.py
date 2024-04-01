import subprocess

def run_script(script_name):
    try:
        output = subprocess.check_output(['/Users/bignola/anaconda3/bin/python3', script_name]).decode('utf-8')
        return output
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
        return None

if __name__ == "__main__":
    # Run AST3.py
    print("Output from AST3.py:")
    output_ast3 = run_script("/Users/bignola/Documents/GitHub/AST-part3/AST3.py")
    if output_ast3:
        print(output_ast3)

    # Print separator
    print("=" * 100)

    # Run AST3-2.py
    print("Output from AST3-2.py:")
    output_ast3_2 = run_script("/Users/bignola/Documents/GitHub/AST-part3/AST3-2.py")
    if output_ast3_2:
        print(output_ast3_2)
