echo "Modbus filters include mbtcp.len/modbus.and_mask/modbus.bit_cnt/modbus.data etc."
read input
tshark -r final_traces.pcap -Y $input | less > log.txt
cat log.txt | paste --d " " > x.csv
