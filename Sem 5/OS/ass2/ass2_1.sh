echo "Enter maximum number: "
read n
echo "Enter Numbers in array: "
for (( i = 0; i < $n; i++ ))
do
	read arr[$i]
done
#arr=(14 16 37 40 114)
echo "Original Array: ";
echo ${arr[*]}
for ((i = 0; i<$n; i++))
do
	for((j = 0; j<$n-i-1; j++))
	do
	if [ ${arr[j]} -gt ${arr[$((j+1))]} ]
	then
		temp=${arr[j]}
		arr[$j]=${arr[$((j+1))]}
		arr[$((j+1))]=$temp
	fi
	done
done
echo "Array after sorting : ";
echo ${arr[*]}