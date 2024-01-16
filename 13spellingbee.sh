cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep -E '^[zonrica]{4,}$' | grep r | grep -v "cc" | grep -v "rr" | grep -v "oo" | grep -v "aa" | grep -v "nn" | grep -v "zz" | grep -v "ii"