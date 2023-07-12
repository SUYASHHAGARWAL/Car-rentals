echo "BUILS START"
python3.9  -m pip install -r requirements.txt
python3.9 manage.py collectstatic --oinput --clear
echo "BUILD COMPLETE"