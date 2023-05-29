# Create a virtual environment
python3 -m venv emotion-classification-with-transformers-venv

# Activate the virtual environment
source ./emotion-classification-with-transformers-venv/bin/activate

# Install requirements
python3 -m pip install --upgrade pip
python3 -m pip install -r ./requirements.txt

# deactivate
deactivate

# To remove the virtual environment run the following command in the terminal
#rm -rf emotion-classification-with-transformers-venv