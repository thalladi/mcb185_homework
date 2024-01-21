cd ~/Code/MCB185/data

gunzip -c dictionary.gz | grep -E '^[zonrica]{4,}$' | grep r 