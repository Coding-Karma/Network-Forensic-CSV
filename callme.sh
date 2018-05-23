echo "How many parameter you want to pass?"

while :
do
read number
case $number in
	1)
	echo "Please enter what you want to find?"
	read input
	cat logged.log | grep -i "Flag\|$input" | paste -d " " > file.csv
	break
	;;
	2)
	echo "Please enter what you want to find?"
	read input
	read inp
	cat logged.log | grep -i "Flag\|$input\|$inp" | paste -d " " > file.csv
	break
	;;
	3)
	echo "Please enter what you want to find?"
	read one
	read two
	read three
	cat logged.log | grep -i "Flag\|$one\|$two\|$three" | paste -d " " > file.csv
	break
	;;
esac
done

