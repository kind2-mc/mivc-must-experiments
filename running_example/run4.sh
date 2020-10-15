
echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "=== MCSs over assumptions and guarantees for SystemModelV3 ==="
echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo

time ../kind2 --enable MCS --mcs_category contracts --mcs_all true SystemModelV3.lus

