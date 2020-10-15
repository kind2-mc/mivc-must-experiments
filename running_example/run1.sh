
echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "=== MIVCs and MUST set over assumptions and guarantees for SystemModelV1 ==="
echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo

time ../kind2 --ivc true --ivc_category contracts --ivc_all true --ivc_must_set true SystemModelV1.lus

