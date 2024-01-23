

cd ~/Code/MCB185/data

gunzip -c dictionary.gz | grep -E '^[auotfcm]{4,}$' | grep a 

gunzip -c dictionary.gz | grep -E '^[bailnrt]{4,}$' | grep b 

gunzip -c dictionary.gz | grep -E '^[caonidm]{4,}$' | grep c 

gunzip -c dictionary.gz | grep -E '^[znorgia]{4,}$' | grep z 

