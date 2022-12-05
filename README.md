**Blockchain-based-IoT Simulation**

```
## Pre-requisites:
Python 2.7 or higher
Git

## NPM packages

npm install -g truffle
npm i pip
npm install -g ganache-cli

## pip install the requirments (Flask, web3, GPIO Emulator)
pip install -r requirements.txt

## Slither Smart Contract Security Analyzer
pip install slither-analyzer

## Steps to run the program:

1. Open two terminals and cd to the Blockchain-based-IoT in both the terminals
cd Blockchain-based-IoT\Blockchain-based-IoT

2. In one terminal type the following command:
ganache-cli
#This instantiates the ganache-cli local ethereum blockchain network

3. In the other terminal type the following commands:
    a. truffle compile
    #This compiles the smart contracts in the application
    b. python app.py 
    
4. Run the python application in any browser window by going typing the following address
    localhost:8000

5. You can control the GPIO pins using the web app on the web browser started in step 4

6. We can observe the gas usage and transaction execution time in the terminals.


```  
