import os
import re

LOG_DIR = r"C:\Users\Siddharth Patel\Documents\Training\Training\python2"
ERROR_OUT = os.path.join(LOG_DIR, "error_summary.txt")
SKIPPED_OUT = os.path.join(LOG_DIR, "skipped_files.log")

def process_logs():
    error_pattern = re.compile(r'^\[(.*?)\] ERROR - (.*)$')
    
    with open(ERROR_OUT, 'w') as err_out, \
         open(SKIPPED_OUT, 'w') as skip_out:
        
        print(f"\nScanning directory: {LOG_DIR}") 
        
        for filename in os.listdir(LOG_DIR):
            filepath = os.path.join(LOG_DIR, filename)
            
            if not os.path.isfile(filepath) or filename in [ERROR_OUT, SKIPPED_OUT]:
                continue
            
            print(f"Checking: {filename}") 
            
            try:
               
                if os.path.getsize(filepath) == 0:
                    skip_out.write(f"Skipped empty file: {filename}\n")
                    print(f"Skipped (empty): {filename}") 
                    continue
                
                with open(filepath, 'r') as f:
                    errors = [line.strip() for line in f if error_pattern.match(line)]
                
                if errors:
                    err_out.write(f"\nErrors in '{filename}':\n")
                    err_out.write('\n'.join(errors) + '\n')
                    err_out.write(f"Total: {len(errors)}\n")
                    print(f"Found {len(errors)} errors in {filename}") 
                else:
                    print(f"No errors found in {filename}") 
            
            except Exception as e:
                skip_out.write(f"Skipped {filename}: {str(e)}\n")
                print(f"Skipped (error): {filename} - {e}") 
        
        print("\nDone. Output saved to:")
        print(f" - {ERROR_OUT}")
        print(f" - {SKIPPED_OUT}")

if __name__ == "__main__":
    process_logs()