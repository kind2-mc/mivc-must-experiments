
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo "=== (Exact) MIVC over assumptions and guarantees for SystemModelV1 ==="
echo "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
echo

time ../kind2 --ivc true --ivc_category contracts --ivc_approximate false SystemModelV1.lus

