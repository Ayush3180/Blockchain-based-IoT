import json
from flask import Flask, render_template
from web3 import Web3, HTTPProvider
# importing GPIO from RaspberryPi simulator
from RPiSim.GPIO import GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

gpiopinList = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
for i in gpiopinList:
    #setting up the GPIO simulator with the pin numbers
    GPIO.setup(i, GPIO.OUT)

# loading artifacts file
artifacts = json.load(open('./artifacts/contracts/PinController.sol/PinController.json'))
# Getting abi and bytecode 
abi = artifacts['abi']
bytecode = artifacts['bytecode']

# web3 instance for HTTP provider
w3 = Web3(HTTPProvider("http://localhost:8545/"))

# Intializationa and deployment of smart contract using web3
contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Transaction hash from deployed smart contract
transaction_hash = contract.constructor().transact({'from': w3.eth.accounts[0], 'gas': 500000})

# Transaction receipt to get smart contract address
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

# Smart Contract instance
contract_instance = w3.eth.contract(abi=abi, address=transaction_receipt.contractAddress)

# GPIO Control Interface
for g in gpiopinList:
    print(g, 'Pin Status: {}' .format(contract_instance.functions.pinStatus(g).call()))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
	
@app.route("/<pin>/<status>")
def control(pin, status):
    #Actuator configuration
    if pin=='2':
        actuator=2
    elif pin=='3':
        actuator=3
    elif pin=='4':
        actuator=4
    elif pin=='5':
        actuator=5
    elif pin=='6':
        actuator=6
    elif pin=='7':
        actuator=7
    elif pin=='8':
        actuator=8
    elif pin=='9':
        actuator=9
    elif pin=='10':
        actuator=10
    elif pin=='11':
        actuator=11
    elif pin=='12':
        actuator=12
    elif pin=='13':
        actuator=13
    elif pin=='14':
        actuator=14
    elif pin=='15':
        actuator=15
    elif pin=='16':
        actuator=16
    elif pin=='17':
        actuator=17
    elif pin=='18':
        actuator=18
    elif pin=='19':
        actuator=19
    elif pin=='20':
        actuator=20
    elif pin=='21':
        actuator=21
    elif pin=='22':
        actuator=22
    elif pin=='23':
        actuator=23
    elif pin=='24':
        actuator=24
    elif pin=='25':
        actuator=25
    elif pin=='26':
        actuator=26
    elif pin=='27':
        actuator=27
    else:
        return render_template('index.html')

    #GPIO pin status
    if status=='on':
         isactive = True
    else:
        isactive = False

    transaction_hash = contract_instance.functions.controlPin(actuator, isactive).transact({'from': w3.eth.accounts[0]})
    print('Transaction submitted:', transaction_hash.hex())

    gpiopin_status = format(contract_instance.functions.pinStatus(actuator).call())
    print(f'Pin {actuator} status changed to {gpiopin_status}')
    if gpiopin_status == 'True':
        GPIO.output(actuator,GPIO.HIGH)
    else:
        GPIO.output(actuator,GPIO.LOW)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8000, host='localhost')
