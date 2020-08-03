read N

sum=0

for (( i=0; i<=$N; i++ ))
do
    read x
    ((sum+=x))
done

printf %.3f $(echo "$sum / $N"  | bc -l)
