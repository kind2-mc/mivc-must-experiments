
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "=== All MIVCs over assumptions and guarantees for SystemModelV1 ==="
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo

time ../kind2 --ivc true --ivc_category contracts --ivc_all true SystemModelV1.lus

