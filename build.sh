echo "Building the project"
pip install -r requirements.txt
echo "MakeMigration"
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput --clear
echo "End Building"