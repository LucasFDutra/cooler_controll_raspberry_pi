sudo chown root:$USER /dev/gpiomem
sudo chmod g+rw /dev/gpiomem

venv-new
venv-activate

pip install gpiozero

sudo cp cooler-controller.service /etc/systemd/system
sudo systemctl start cooler-controller.service
sudo systemctl enable cooler-controller.service
