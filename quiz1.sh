
echo Varsha Thalladi
echo "user: $USER"


cd ~/Code/MCB185/data

gunzip -c dictionary.gz | grep -E '^[auotfcm]{4,}$' | grep a 

gunzip -c dictionary.gz | grep -E '^[bailnrt]{4,}$' | grep b 

gunzip -c dictionary.gz | grep -E '^[caonidm]{4,}$' | grep c 

gunzip -c dictionary.gz | grep -E '^[znorgia]{4,}$' | grep z 

gunzip -c jaspar2024_core.transfac.gz | grep "tax" | cut -d ":" -f 2 | sort | uniq -c | sort -n

# Task 6: Avantika Gokulnatha, Anisha Patel, Francesca Asuncion