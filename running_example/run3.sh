
echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "=== MIVCs and MUST set over assumptions and guarantees for SystemModelV2 ==="
echo "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo

time ../kind2 --ivc true --ivc_category contracts --ivc_all true --ivc_must_set true SystemModelV2.lus

